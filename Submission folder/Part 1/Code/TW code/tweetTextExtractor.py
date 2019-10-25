import json
import emoji
import re
names = ['Game of Thrones','Star Wars','Marvel','Drama Movies','Disney']
POSITIVE = ["*O", "*-*", "*O*", "*o*", "* *",
                ":P", ":D", ":d", ":p",
                ";P", ";D", ";d", ";p",
                ":-)", ";-)", ":=)", ";=)",
                ":<)", ":>)", ";>)", ";=)",
                "=}", ":)", "(:;)",
                "(;", ":}", "{:", ";}",
                "{;:]",
                "[;", ":')", ";')", ":-3",
                "{;", ":]",
                ";-3", ":-x", ";-x", ":-X",
                ";-X", ":-}", ";-=}", ":-]",
                ";-]", ":-.)",
                "^_^", "^-^"]

NEGATIVE = [":(", ";(", ":'(",
                "=(", "={", "):", ");",
                ")':", ")';", ")=", "}=",
                ";-{{", ";-{", ":-{{", ":-{",
                ":-(", ";-(",
                ":,)", ":'{",
                "[:", ";]"
                ]
all_emojis = POSITIVE + NEGATIVE
# emoji_pattern = re.compile("["
#         u"\U0001F600-\U0001F64F"
#         u"\U0001F300-\U0001F5FF"
#         u"\U0001F680-\U0001F6FF"
#         u"\U0001F1E0-\U0001F1FF"
#                            "]+", flags=re.UNICODE)
emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u'\U00010000-\U0010ffff'
                u"\u200d"
                u"\u2640-\u2642"
                u"\u2600-\u2B55"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\u3030"
                u"\ufe0f"
    "]+", flags=re.UNICODE)
for name in names:
    seen = set()
    tweetFile = open(name+'.json', 'r')
    textFile = open('./tweetTexts/'+name+'.txt','w',encoding='utf-8')
    for i in range(500):
        tweet = tweetFile.readline()
        if tweet != "":
            tweetJson = json.loads(tweet)
            tweetText = tweetJson['text']
            if tweetText != "":
                tweetText = tweetText.replace('\n', '').replace('\r', '')
                tweetText = tweetText.split(" ")
                finalString = ""
                for word in tweetText:
                    if "https://" in word or "http://" in word:
                        continue
                    if "@" in word:
                        continue
                    if word.encode('utf-8') in emoji.UNICODE_EMOJI or word.encode('utf-8') in emoji.EMOJI_UNICODE or word.encode('utf-8') in emoji.UNICODE_EMOJI_ALIAS \
                            or word.encode('utf-8') in emoji.EMOJI_ALIAS_UNICODE:
                        continue
                    if word in all_emojis:
                        continue

                    finalString = finalString + word + " "
                    finalString = emoji_pattern.sub(r'', finalString)
                print(finalString)
                if finalString not in seen:
                    textFile.write(finalString+"\n")
                    seen.add(finalString)
