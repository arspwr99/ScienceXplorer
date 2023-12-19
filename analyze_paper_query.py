import requests
import json
import argparse
from analyze_paper import analyze_paper_by_id



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='This program analyzes a paper using a query and not the paper ID.')
    parser.add_argument('--query', type=str, help='query', required=True)
    parser.add_argument('--S2_API_KEY', type=str, help='Name of the scientist', required=False, default='B16vCpZ2ka346nksEYHlO7ZJMIRQmOFQ24QI5fok')
    parser.add_argument('--filepath', type=str, help='query', required=False, default='None')
    args = parser.parse_args()
    query = args.query
    filepath = args.filepath
    S2_API_KEY = args.S2_API_KEY


    fields = "title,year"
    url = f"http://api.semanticscholar.org/graph/v1/paper/search/bulk?query={query}&fields={fields}&year=2023-"
    r = requests.get(url).json()

    print(f"Will retrieve an estimated {r['total']} documents")
    retrieved = 0


    papers = []
    while True:
        if "data" in r:
            retrieved += len(r["data"])
            print(f"Retrieved {retrieved} papers...")
            for paper in r["data"]:
                papers.append(paper)
        if "token" not in r:
            break
        r = requests.get(f"{url}&token={r['token']}").json()
    print(f"Done! Retrieved {retrieved} papers total")


    if filepath != None:
        # save json file 
        with open(filepath, 'w') as outfile:
            json.dump(papers, outfile)

    # sort paper by year
    papers.sort(key=lambda x: x['year'], reverse=True)

    idx = None

    for i in range(len(papers)):
        print (f"{i}: {papers[i]['title']}")

        if i%10 == 0 and i != 0:
            idx = input("Select one paper to analyze (just a number), press N to continue to the next page, or press 'q' to quit:")
            if idx.lower() == "q" or idx.isdigit():
                break 
    
    if len(papers) == 0:
        exit()
    
    if idx == None:
        idx = input("Select one paper to analyze (just a number) or press 'q' to quit:")

    if idx == "q":
        print ("Quitting...")
        exit()
    elif idx.lower() == "n":
        print ("No more pages. Quitting...")
    elif idx.isdigit():
        idx = int(idx)
    if idx >= len(papers):
        print ("Invalid index. Quitting...")
        
    analyze_paper_by_id(papers[idx]["paperId"], S2_API_KEY)
    