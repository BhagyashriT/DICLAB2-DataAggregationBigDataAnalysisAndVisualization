from nytimesarticle import articleAPI
import time
import json

subtopics = ['marvel','Game of Thrones','disney','Star Wars','Drama']
api = articleAPI('x2beLM42clH2nOepY4t3M1DC06t7zLQi')
no_of_articles = 100
for topic in subtopics:
    i = 0
    f = open(topic+'.json', mode='w')
    print("========================= Searching for topic: "+topic+" ====================================")
    while True:
        articles = api.search(q=topic,
                              # fq="{'source': ['Reuters', 'AP', 'The New York Times','Washington Post','Google']}",
                              begin_date=20190101, end_date=20190420,
                              facet_filter=True, page=i)
        # print(articles)
        print(len(articles['response']['docs']))
        if len(articles['response']['docs']) == 0:
            break
        for j in articles['response']['docs']:
            print(j['headline'])
            jsonToWrite = json.dumps(j)
            f.write(jsonToWrite+"\n")
            # json.dump(j._json,open('nyt_data.json','wb'))
        i += 1

        print("<========================================================================================================>")
        time.sleep(7)
