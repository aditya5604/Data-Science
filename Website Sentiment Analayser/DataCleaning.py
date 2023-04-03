from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


def collect_website_data(url):
    
    only_a_tags = SoupStrainer("p")
    try:
      index_page = urlopen(url) 
      scrape_data = BeautifulSoup(index_page, "html.parser", parse_only = only_a_tags ).prettify() # BeatifulSoup Object
    except:
        scrape_data = "PAGE NOT FOUND"
    return scrape_data

def collect_website_title(url):
    only_t_tags = SoupStrainer("h1")
    try:
      index_page = urlopen(url) 
      scrape_data = BeautifulSoup(index_page, "html.parser", parse_only = only_t_tags ).prettify() # BeatifulSoup Object
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

URL = 'https://insights.blackcoffer.com/how-small-business-can-survive-the-coronavirus-crisis/'

data_para = collect_website_data(URL)
data_para = clean_data(URL)
data_title = collect_website_title(URL)
data_title = clean_data(data_title)
newfile = open('ERROR.txt', "w+")
newfile.write(data_title)
newfile.write(data_para)
newfile.close() 
