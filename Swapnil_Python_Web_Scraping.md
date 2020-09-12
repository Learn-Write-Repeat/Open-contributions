![PYHTON](./extras/Untitled.svg)
# Python Web Scraping

## What is Web Scraping ?
Web scraping is the technique for extracting the relevant information from a webpage. web scraping allows user to get the relevant information from any websites and it can be done manually as well as with the help of bots as well.

## Why Python for Web Scraping ?
Python has become one of the widely used programming language and with its easy to learn syntax and huge number of libraries such as BeautifulSoup, Scrapy , Pandas etc, it is one of the most preferred programming language for web scraping.



# Getting Started

## Libraries Required

## 1. Requests
it is the library which is used to make HTTP requests from python program 


### Installation

Python 3 ```pip3 install requests``` \
Python 2.x ```pip install bs4```
## Methods for requests mode 
### get()
get function sends the get requests to the given url which then returns a response object<br>
### Example
``` python
import requests
source = requests.get(url)
```
<br>
<br>
<br>

## 2. Beautifulsoup
BeautifulSoup is a python library used for parsing the HTML and XML data

Python 3 - ```pip3 install requests``` \
Python 2.x - ```pip install bs4```

### Using BeautifulSoup Library
### Example
``` python
import requests
import bs4
source = requests.get(url)
soup = bs4.BeautifulSoup(source.text,lxml)
```
## select ()
1 - Using select() to grab the title of the webpage
```python
    title = soup.select('title')
```
## output:
```python 

```
## find()
1 - Using find() to grab the text from the specific classes and id
```python
    id = soup.find(id="")
```
## output:
```python 

