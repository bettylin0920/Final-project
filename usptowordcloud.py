#encoding=utf-8
import csv
import nltk
from nltk import word_tokenize
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

#取出 result 內所有內容
allpn = []

file = open('result.csv', 'r')
csvabs = csv.reader(file)

for row in csvabs:
    allpn.append(row)

#取出 wordcount 部分
allpnabs = []

for row in allpn:
    allpnabs.append(row[5])

#去掉部分字詞
allpnabsstr = str(allpnabs).replace('"','').replace("'Word Count'","").replace("'",'').replace("[","").replace("]","").replace(",","")
allpnabsstr = word_tokenize(allpnabsstr.strip().lower())

WordABS = Counter(allpnabsstr)

for name, count in WordABS.most_common(40):
    print('{0} {1}'.format(count, name))

f = open("count.csv", "w", newline="")
writer = csv.writer(f)
writer.writerows(WordABS.most_common(40))
f.close()

#文字雲
cut_text = '\n'.join(' '.join(word_tokenize(sent)) for sent in allpnabsstr)
# lower max_font_size
wordcloud = WordCloud(max_font_size=60).generate(cut_text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()