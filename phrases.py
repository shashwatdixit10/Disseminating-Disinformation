import requests
from bs4 import BeautifulSoup
import csv

url = "https://pkbnews.in/cristiano-ronaldo-dead/"
def check_phrases(url):


    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    # Extract the title of the news article
    title = soup.find('h1').text

    # # Extract the date of the news article
    # date = soup.find('div', {'class': 'article-date'}).text

    # Extract the content of the news article

    point = 0
    content = ""
    article_content = soup.find('div')
    for paragraph in article_content.find_all('p'):
        content += paragraph.text

    

    with open('phrases.csv','r') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] in title.lower():
                # for chk1 in open("title_check.csv").read():
                #     if(chk1 in title.lower()):
                #         point=3

                #     else:
                #         point=1

                #     break
                with open('title_check.csv') as file2:
                    reader_new = csv.reader(file2)
                    for r in reader_new:
                        if r[0] in title.lower():
                            point=3
                        
                        else:
                            point=1
            
            elif row[0] in content.lower():
                point = 1
            
    return point
            



check_phrases(url)

    

# # Print the extracted data
# print("Title:", title)
# # print("Date:", date)
# print("Content:", content)
