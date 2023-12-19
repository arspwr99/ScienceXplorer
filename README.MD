# Welcome to ScienceXplorer Python Library

## Download Code
```bash
git clone https://github.com/arspwr99/ScienceXplorer.git
```

## Overview

ScienceXplorer is a powerful Python library designed to assist you in navigating the vast world of scientific knowledge. With its versatile features, ScienceXplorer allows you to explore academic papers, authors, and more. Below are some of the key functionalities that ScienceXplorer offers:

## Functionalities

### 1. Analyzing a Paper Using Its ID

Use this command to analyze a specific paper by providing its unique ID. This script retrieves essential information about the paper, such as its title, authors, citations, and more.

```bash
python3 analyze_paper.py --paper_id="CorpusID:235266322"
```
The output of this script will be similar to the following:

```bash
----------------------------------------
Paper title: Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models
This paper has 4 authors:
  Tongshuang Sherry Wu
  Marco Tulio Ribeiro
  Jeffrey Heer
  Daniel S. Weld
The paper has 150 citations of which 8 contain self-citing authors and 142 are external citations.
  Tongshuang Sherry Wu in citing paper "LLMs as Workers in Human-Computational Algorithms? Replicating Crowdsourcing Pipelines with LLMs"
  Jeffrey Heer, Marco Tulio Ribeiro, Daniel S. Weld, Tongshuang Sherry Wu in citing paper "ScatterShot: Interactive In-context Example Curation for Text Transformation"
  Tongshuang Sherry Wu in citing paper "Capabilities for Better ML Engineering"
  Marco Tulio Ribeiro in citing paper "ExSum: From Local Explanations to Model Understanding"
  Tongshuang Sherry Wu in citing paper "NL-Augmenter: A Framework for Task-Sensitive Natural Language Augmentation"
  Tongshuang Sherry Wu in citing paper "AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts"
  Tongshuang Sherry Wu in citing paper "Tailor: Generating and Perturbing Text with Semantic Controls"
  Marco Tulio Ribeiro in citing paper "Adaptive Testing and Debugging of NLP Models"
The paper has 66 references of which 6 contain self-referencing authors.
  Marco Tulio Ribeiro in referenced paper "Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance"
  Marco Tulio Ribeiro in referenced paper "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList"
  Marco Tulio Ribeiro in referenced paper "Errudite: Scalable, Reproducible, and Testable Error Analysis"
  Marco Tulio Ribeiro in referenced paper "Semantically Equivalent Adversarial Rules for Debugging NLP models"
  Scott M. Lundberg in referenced paper "A Unified Approach to Interpreting Model Predictions"
  Marco Tulio Ribeiro in referenced paper "“Why Should I Trust You?”: Explaining the Predictions of Any Classifier"
----------------------------------------
```

### 2. Analyzing a Paper Using a Query
Discover papers related to your area of interest by entering a query. You can also save the results in a JSON file for future reference.

```bash
python3 analyze_paper_query.py --query="Search Engine for scientific articles" --filepath="dataset.json"
```
The output of this script will be similar to the following and also will save a json file dataset.json in the current directory:

```bash
Will retrieve an estimated 130 documents
Retrieved 130 papers...
Done! Retrieved 130 papers total
0: News from the European Journal of Therapeutics: A new issue and a new editorial board
1: effects of increased body mass index on preconception health
2: Systematic Literature Review: Pengaruh Indeks Pembangunan Manusia (IPM) Terhadap Pertumbuhan Ekonomi
3: Single vs. Multi-Label: The Issues, Challenges and Insights of Contemporary Classification Schemes
4: SİMÜLASYON TEMELLİ TIP EĞİTİMİN BÜTÇEYE SAĞLADIĞI KLİNİK VE EKONOMİK FAYDALAR
5: Magnitude, Associated Risk Factors, and Trend Comparisons of Urinary Tract Infection among Pregnant Women and Diabetic Patients: A Systematic Review and Meta-Analysis
6: Internet User Awareness Assessment on the Impact of Microplastics on Health
7: Creative heritage of Dimitry Dan and its international perception
8: Analysis of professional competencies in the characterization of the teacher of the future: global challenges of the present
9: the specificity of female addictions in morocco (A cross-sectional analytical study)
10: Criteria for the selection, evaluation and application of traditional knowledge in contemporary health practice, education, research and policy: A systematic review.
Select one paper to analyze (just a number), press N to continue to the next page, or press 'q' to quit:1
----------------------------------------
Paper title: effects of increased body mass index on preconception health
This paper has 3 authors:
  Petra Petročnik
  M. Prosen
  A. P. Mivšek
The paper has 0 citations of which 0 contain self-citing authors and 0 are external citations.
The paper has 0 references of which 0 contain self-referencing authors.
```


### 3. Analyzing an Author Using Author ID
Explore the works of a specific author by providing their unique ID. This script retrieves all the papers authored by the selected individual, along with detailed citation information for each paper. It also calculates self and external citations for the entire body of work by the scientist.

```bash
python3 analyze_author.py --author "29961755"
```
The output of this script will be similar to the following:

```bash
Author's name: Aristomenis A. Sotiropoulos, id: 29961755, url: https://www.semanticscholar.org/author/29961755
Aristomenis A. Sotiropoulos has published 15 papers:
0/15: A low-dose, 6-week bovine colostrum supplementation maintains performance and attenuates inflammatory indices following a Loughborough Intermittent Shuttle Test in soccer players has:
   22 citations which 0 are self citations and 22 are external citations.
1/15: Multiarticular Isokinetic High-Load Eccentric Training Induces Large Increases in Eccentric and Concentric Strength and Jumping Performance has:
   30 citations which 0 are self citations and 30 are external citations.
2/15: The Effect of High vs. Low Carbohydrate Diets on Distances Covered in Soccer has:
   26 citations which 0 are self citations and 26 are external citations.
3/15: The Relationship of Group Cohesion with the Antecedents for Soccer Teams has:
   2 citations which 0 are self citations and 2 are external citations.
4/15: Effects of Two Different Half-Squat Training Programs on Fatigue During Repeated Cycling Sprints in Soccer Players has:
   29 citations which 1 are self citations and 28 are external citations.
5/15: INVESTIGATION OF POSSIBLE CHANGES TO BIOCHEMICAL INDICES REGARDING SPECIFIC FORMS OF EXERCISE (SOCCER, SWIMMING ETC) IN CHILDHOOD has:
   1 citations which 0 are self citations and 1 are external citations.
6/15: Changes in Homocysteine and 8-iso-PGF2a Levels in Football and Hockey Players After a Match has:
   10 citations which 0 are self citations and 10 are external citations.
7/15: Relationship Between the 20-m Multistage Shuttle Run Test and 2 Soccer-Specific Field Tests for the Assessment of Aerobic Fitness in Adult Semi-professional Soccer Players has:
   32 citations which 0 are self citations and 32 are external citations.
8/15: The Effect of a 4-Week Training Regimen on Body Fat and Aerobic Capacity of Professional Soccer Players During The Transition Period has:
   40 citations which 0 are self citations and 40 are external citations.
9/15: CHANGES IN HORMONAL AND LIPID PROFILE AFTER A SOCCER MATCH IN MALE AMATEUR PLAYERS has:
   10 citations which 0 are self citations and 10 are external citations.
10/15: SOCCER, MINORITIES AND NATIONAL IDENTITY has:
   0 citations which 0 are self citations and 0 are external citations.
11/15: Prevalence of Dehydration in Young Soccer Players During a Summer Soccer Camp: 727 has:
   2 citations which 0 are self citations and 2 are external citations.
12/15: COACHING P-082 Opinion of soccer players about off-season in Turkish super league has:
   0 citations which 0 are self citations and 0 are external citations.
13/15: Strength and Speed Characteristics of Elite, Subelite, and Recreational Young Soccer Players has:
   180 citations which 0 are self citations and 180 are external citations.
14/15: MUSCLE‐CONTRACTION PROPERTIES IN OVERARM THROWING MOVEMENTS has:
   24 citations which 0 are self citations and 24 are external citations.
----------------------------------------
Conclusion:
   Aristomenis A. Sotiropoulos has published 15 papers:
   Has in total: 408 citations
   1 are self citations and 407 are external citations.
----------------------------------------
```


### 4. Analyzing an Author Using Author Name
If you prefer to search for an author using a more flexible, fuzzy approach, this script is your go-to tool. It searches for authors based on the provided name, and if multiple matches are found, it selects the first one. For a specific author, find their ID using the Semantic Scholar platform and then use the analyze_author_id script for a more detailed analysis, including self and external citations.

```bash
python3 analyze_author.py --author "Aristomenis"
```
The output of this script will be similar to the following:
```bash
Multiple authors matched "Aristomenis". Selecting the first one:
Author's name: Aristomenis A. Sotiropoulos, id: 29961755, url: https://www.semanticscholar.org/author/29961755
Aristomenis A. Sotiropoulos has published 15 papers:
0/15: A low-dose, 6-week bovine colostrum supplementation maintains performance and attenuates inflammatory indices following a Loughborough Intermittent Shuttle Test in soccer players has:
   22 citations which 0 are self citations and 22 are external citations.
1/15: Multiarticular Isokinetic High-Load Eccentric Training Induces Large Increases in Eccentric and Concentric Strength and Jumping Performance has:
   30 citations which 0 are self citations and 30 are external citations.
2/15: The Effect of High vs. Low Carbohydrate Diets on Distances Covered in Soccer has:
   26 citations which 0 are self citations and 26 are external citations.
3/15: The Relationship of Group Cohesion with the Antecedents for Soccer Teams has:
   2 citations which 0 are self citations and 2 are external citations.
4/15: Effects of Two Different Half-Squat Training Programs on Fatigue During Repeated Cycling Sprints in Soccer Players has:
   29 citations which 1 are self citations and 28 are external citations.
5/15: INVESTIGATION OF POSSIBLE CHANGES TO BIOCHEMICAL INDICES REGARDING SPECIFIC FORMS OF EXERCISE (SOCCER, SWIMMING ETC) IN CHILDHOOD has:
   1 citations which 0 are self citations and 1 are external citations.
6/15: Changes in Homocysteine and 8-iso-PGF2a Levels in Football and Hockey Players After a Match has:
   10 citations which 0 are self citations and 10 are external citations.
7/15: Relationship Between the 20-m Multistage Shuttle Run Test and 2 Soccer-Specific Field Tests for the Assessment of Aerobic Fitness in Adult Semi-professional Soccer Players has:
   32 citations which 0 are self citations and 32 are external citations.
8/15: The Effect of a 4-Week Training Regimen on Body Fat and Aerobic Capacity of Professional Soccer Players During The Transition Period has:
   40 citations which 0 are self citations and 40 are external citations.
9/15: CHANGES IN HORMONAL AND LIPID PROFILE AFTER A SOCCER MATCH IN MALE AMATEUR PLAYERS has:
   10 citations which 0 are self citations and 10 are external citations.
10/15: SOCCER, MINORITIES AND NATIONAL IDENTITY has:
   0 citations which 0 are self citations and 0 are external citations.
11/15: Prevalence of Dehydration in Young Soccer Players During a Summer Soccer Camp: 727 has:
   2 citations which 0 are self citations and 2 are external citations.
12/15: COACHING P-082 Opinion of soccer players about off-season in Turkish super league has:
   0 citations which 0 are self citations and 0 are external citations.
13/15: Strength and Speed Characteristics of Elite, Subelite, and Recreational Young Soccer Players has:
   180 citations which 0 are self citations and 180 are external citations.
14/15: MUSCLE‐CONTRACTION PROPERTIES IN OVERARM THROWING MOVEMENTS has:
   24 citations which 0 are self citations and 24 are external citations.
----------------------------------------
Conclusion:
   Aristomenis A. Sotiropoulos has published 15 papers:
   Has in total: 408 citations
   1 are self citations and 407 are external citations.
----------------------------------------
```


Explore the depths of scientific literature and gain valuable insights using ScienceXplorer. Whether you're a researcher, student, or simply a curious mind, our Python library provides the tools you need to unravel the wonders of science.


