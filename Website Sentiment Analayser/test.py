from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from nltk.tokenize import word_tokenize

url = 'https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-2/'

def collect_website_data(url):
    
    only_a_tags = SoupStrainer("p")
    try:
      index_page = urlopen(url) 
      scrape_data = BeautifulSoup(index_page, "html.parser", parse_only = only_a_tags ).prettify() # BeatifulSoup Object
    except:
        scrape_data = "PAGE NOT FOUND"
    return scrape_data

def clean_data(a):
    a = a.replace('</a>', ' ')
    a =a.replace('href', ' ')
    a =a.replace('<p>', ' ')
    a = a.replace('</p>', ' ')
    a = a.replace('class', ' ')
    a = a.replace('entry-title', ' ')
    a = a.replace('td-module-title', ' ')
    a = a.replace('<a', ' ')
    a = a.replace('>', ' ')
    a = a.replace('<p', ' ')
    a = a.replace('rel = bookmark', ' ')
    a = a.replace('rel="bookmark"', ' ')
    a = a.replace('title', ' ')
    a = a.replace('https://insights.blackcoffer.com/', ' ')
    a = a.replace('/', ' ')
    a = a.replace('=', ' ')
    a = a.replace('"', ' ')
    a = a.replace('<strong', ' ')
    a = a.replace('</strong', ' ')
    a = a.replace('< strong', ' ')
    a = a.replace('tdm-descr', ' ')
    a = a.replace('Contact us:  ', ' ')
    a = a.replace('mailto:contact@yoursite.com', ' ')
    a = a.replace('contact@yoursite.com', ' ')
    a = a.replace('@', ' ')
    a = a.replace('Newspaper', ' ')
    a = a.replace('WordPress', ' ')
    a = a.replace('Theme', ' ')
    a = a.replace('Tagdiv', ' ')
    a = a.replace(':', ' ')
    a = a.replace('-', ' ')
    a = a.replace('<h1', " ")
    a = a.replace('</h1>', " ")
    a = a.replace('>', " ")
    a = a.replace('"entry-title"', " ")
    a = a.replace('< h1', " ")
    a = a.replace('₹', " ")
    a = a.replace('%', "percent")
    a = a.replace('<em', " ")
    a = a.replace('</em>', " ")
    a = a.replace('< em', " ")
    a = a.replace(';', " ")
    a = a.replace('#_ftn1', " ")
    a = a.replace('[1]', " ")
    a = a.replace(' ≈', " ")
    return a


val = clean_data(collect_website_data(url))
print(val)
val = val.word_tokenize()
#file = open('data.txt', 'w+')
#file.write(val)
#file.close()
