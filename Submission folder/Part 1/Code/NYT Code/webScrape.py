import html2text
import json
import nltk
from nltk.stem import WordNetLemmatizer
import urllib
# from newspaper import Article
import requests
from bs4 import BeautifulSoup
lemmatizer = WordNetLemmatizer()
subtopics = ['marvel','Game of Thrones','disney','Star Wars','Drama']
for topic in subtopics:
    print("================================ Scraping for topic "+topic+" ==============================================")
    f = open(topic+".json","r")
    f1 = open("./nytText/"+topic+".txt","w",encoding="utf-8")

    # page = urllib.request.urlopen(url).read()
    # h = html2text.HTML2Text()
    # h.ignore_links = True
    # h.ignore_images = True
    # print(h.handle(str(page)))

    # article = Article(url)
    # article.download()
    # article.parse()
    # print(article.text)

    line = f.readline()
    while(line != ""):
        jsonString = json.loads(line)
        url = jsonString['web_url']
        if(url == ""):
            line = f.readline()
            continue
        print(url)
        response = requests.get(url)
        doc = BeautifulSoup(response.text, 'html.parser')
        story = doc.find_all('p')
        for story in story:
            articleText = story.text
            if("follow the new york times" in articleText.lower()):
                continue
            word_list = nltk.word_tokenize(articleText)
            finalPara = ""
            for w in word_list:
                lemma = lemmatizer.lemmatize(w)
                finalPara = finalPara + " " + lemma
            # print(finalPara)
            f1.writelines(finalPara + "\n")
        line = f.readline()