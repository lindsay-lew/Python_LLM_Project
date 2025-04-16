# Project: Python LLMs


## What my docsum.py file does:
This project focuses on understanding how to use LLMs from Python. My ```docsum.py``` file takes either a file path or a URL as a command line argument, then summarizes its contents using the Groq API. It can work with ordinary text documents, html files, pdf files, and images (both stored locally and inside URLs). 


## How to run my docsum.py file:
```
$ python3 docsum.py docs/news-mx.html
The text contains a mix of code snippets, articles, and metadata from various sources, including JSON objects, HTML/CSS code, and news articles. The code snippets seem to be from different web applications, while the news articles discuss topics like immigration and the US Supreme Court.
```

```
$ python3 docsum.py docs/constitution-mx.txt
The Mexican Constitution recognizes the country's unique identity and grants indigenous peoples autonomy, self-determination, and cultural preservation. The Constitution outlines the rights and freedoms of individuals, including freedom of expression, education, healthcare, and property rights, as well as the structure and powers of government institutions, including the Congress, the President, and the judiciary. The Constitution also establishes regulations for labor rights, religious associations, and governance, including the transition plan for the newly established government.
```

```
$ python3 docsum.py docs/research_paper.pdf
The paper proposes a new unsupervised pretraining method called DOCSPLIT, which is designed to improve large document embeddings by considering the entire global context. Experimental results show that models pretrained with DOCSPLIT outperform models pretrained with other methods on document classification, few shot learning, and document retrieval tasks. DOCSPLIT achieves improvements in few-shot text classification compared to other pre-trained language models, such as BERT, Longformer, and BigBird.
```

```
$ python3 docsum.py https://elpais.com/us/
The text appears to be a collection of CSS styles and HTML layout information, used to design and layout a website. It defines various styles and classes for elements such as headings, paragraphs, lists, and forms, as well as layouts for specific sections of the page. The text may also include JavaScript code for tracking and collecting data on user behavior, but the majority of the text is CSS code.
```

```
$ python3 docsum.py https://www.cmc.edu/sites/default/files/about/images/20170213-cube.jpg
The image depicts a modern glass-walled structure situated beside a serene water feature and surrounded by other buildings. The structure, likely a lounge or meeting space, features a glass enclosure with a flat roof, supported by slender pillars, and is furnished with orange and yellow chairs and tables. The surrounding area includes a pool of water that reflects the building's interior lighting, creating a sense of calm and sophistication.
```
