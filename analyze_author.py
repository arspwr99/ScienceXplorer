import argparse
import re
import sys
from analyze_paper import get_citations, filter_self_citing
import requests

def resolve_author(desc: str):
    req_fields = 'authorId,name,url'

    if re.match('\\d+', desc):  # ID given
        rsp = requests.get(f'https://api.semanticscholar.org/graph/v1/author/{desc}',
                           params={'fields': req_fields})
        rsp.raise_for_status()
        return rsp.json()

    else:  # search
        rsp = requests.get('https://api.semanticscholar.org/graph/v1/author/search',
                           params={'query': desc, 'fields': req_fields})
        rsp.raise_for_status()

        results = rsp.json()
        if results['total'] == 0:  # no results
            print(f'Could not find author "{desc}"')
            sys.exit(1)
        elif results['total'] == 1:  # one unambiguous match
            return results['data'][0]
        else:  # multiple matches
            print(f'Multiple authors matched "{desc}". Selecting the first one:')
            # print (results['data'][0])
            return  results['data'][0]
            # for author in results['data']:
            #     print(author)


def get_author_papers(author_id):
    rsp = requests.get(f'https://api.semanticscholar.org/graph/v1/author/{author_id}/papers',
                       params={'fields': 'title,url,year,authors', 'limit': 1000})
    rsp.raise_for_status()
    return rsp.json()['data']


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Return the number of citations (self and external) for a scientist.')
    parser.add_argument('--author', type=str, help='Name or Id of the author', required=True)
    parser.add_argument('--S2_API_KEY', type=str, help='Name of the scientist', required=False, default='B16vCpZ2ka346nksEYHlO7ZJMIRQmOFQ24QI5fok')
    args = parser.parse_args()

    author_name = args.author
    S2_API_KEY = args.S2_API_KEY
    author = resolve_author(author_name)

    print (f'Author\'s name: {author["name"]}, id: {author["authorId"]}, url: {author["url"]}')

    papers = get_author_papers(author['authorId'])
    print (f"{author['name']} has published {len(papers)} papers:")

    total_self_citations, total_external_citations, total_citations = 0, 0, 0
    exceptions = []
    for i, paper in enumerate(papers):
        try:
            citations = get_citations(paper["paperId"], S2_API_KEY)
            self_citations = list(filter_self_citing([author], citations))
            external_citations = len(citations) - len(self_citations)

            print (f"{i}/{len(papers)}:", paper["title"], "has:")
            print (f"   {len(citations)} citations which {len(self_citations)} are self citations and {external_citations} are external citations.")
            
            total_self_citations += len(self_citations)
            total_external_citations += external_citations
            total_citations += len(citations)
        except Exception as e:
            print ("Warning: There was an error while processing the paper:", paper["title"])
            exceptions.append(paper["title"])
            print (e) 


    print ("----"*10)
    print ("Conclusion:")
    print (f"   {author['name']} has published {len(papers)} papers:")
    print (f"   Has in total: {total_citations} citations")
    print (f"   {total_self_citations} are self citations and {total_external_citations} are external citations.")
    if len(exceptions) > 0:
        print (f"There were errors while processing {len(exceptions)} papers:")
    print ("----"*10)