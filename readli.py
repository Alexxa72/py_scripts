book_id = str(1111111) #number in string format
book_pages = 100 # last page number


import pandas as pd
from bs4 import BeautifulSoup
import requests

# function to extract html document from given url 
def getHTMLdocument(url): 
      
    # request for HTML document of given url 
    response = requests.get(url) 
      
    # response will be provided in JSON format 
    return response.text 

lnk =  "https://readli.net/chitat-online/?b="+book_id+"&pg="

fn = book_id+'.txt'

# Open the file in append mode
file = open(fn, 'a')


for i in range(1, book_pages+1):
# assign required credentials 
# assign URL 
    url_to_scrape = lnk + str(i)
  
    # create document 
    html_document = getHTMLdocument(url_to_scrape) 
    
    # create soap object 
    soup = BeautifulSoup(html_document, 'html.parser') 
 
    for k in soup.find("div", class_ ="reading__text").find_all(['h3', 'p']):
        #Append content to the file
        file.write(str(k))

# Close the file
file.close()
