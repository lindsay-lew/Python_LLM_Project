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
```
```
$ python3 docsum.py docs/research_paper.pdf
```
```
$ python3 docsum.py https://elpais.com/us/
```
```
$ python3 docsum.py https://www.cmc.edu/sites/default/files/about/images/20170213-cube.jpg
The image depicts a modern building complex, likely an office or educational facility, at dusk. The main focus is on a glass-walled structure with a flat roof and a pool of water in front of it.\n\n* **Glass-walled structure:**\n\t+ Located in the center of the image\n\t+ Has a flat roof and a glass wall on all sides\n\t+ Contains several tables and chairs inside\n\t+ Appears to be well-lit from within\n* **Pool of water:**\n\t+ Located in front of the glass-walled structure\n\t+ Reflects the lights from the building and the sky\n\t+ Has a dark gray stone floor around it\n* **Other buildings:**\n\t+ A large building with many windows and balconies is visible to the right\n\t+ A smaller building with a flat roof and several windows is visible to the left\n\t+ Both buildings appear to be well-lit from within\n* **Sky:**\n\t+ Dark blue with some clouds\n\t+ Indicates that the photo was taken at dusk or dawn\n\nOverall, the image presents a serene and modern architectural scene, with a focus on clean lines, glass, and water features.'
```
