from bs4 import BeautifulSoup
import html5lib
import re
import csv
import urllib
import requests
from collections import Counter
import sys
import string
import nltk
nltk.download('stopwords')
from nltk import word_tokenize
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
stopwords.add("'s")
stopwords.add("'ve")
stopwords.update(string.punctuation)


#Abstract
def ABS(soup):
    for abs in soup.find_all("b"):
        if abs.next_element == "Abstract":
            AbsContent = abs.next_element.next_element.next_element.string.replace("\n","").replace("  ","")
            AbsContent = AbsContent.lower()
    return (AbsContent)


#word count
def wordcountABS(soup):
    AbsContent = ABS(soup)
    AbsContent = word_tokenize(AbsContent.strip())
    NewContent = []
    for word in AbsContent:
        if word not in stopwords:
            NewContent.append(word)
    wordCount = Counter(NewContent)
    return (NewContent)

#application date
def Appdate(soup):
    for date in soup.find_all('th',attrs = {'scope':'row','valign':'top','align':'left','width':'10%'}):
        if "Filed" in date.next_element:
            for b in date.next_element.next_element('b'):
                return (b.string)

#CPC
def CPC (soup):
    for date in soup.find_all('td',attrs = {'valign':'top','align':'right','width':'70%'}):
        if "Current CPC Class" in date.previous_element.previous_element:
            str = date.next_element.encode("utf8").decode("cp950","ignore")
            #str = str.replace(";",">").replace(" ","<") + ">"
            cpc = ', '.join((re.sub('<[^>]+>',' ',str).split()))
            cpc = cpc.replace(";",'\n').replace(",","").replace(" H","H")
            return (cpc)

#IPC
def IPC (soup):
    for date in soup.find_all('td',attrs = {'valign':'top','align':'right','width':'70%'}):        
        if "Current International Class" in date.previous_element.previous_element:
            str = date.next_element.encode("utf8").decode("cp950","ignore")
            #str = str.replace(";",">").replace(" ","<") + ">"
            ipc = ', '.join((re.sub('<[^>]+>',' ',str).split()))
            ipc = ipc.replace(";",'\n').replace(",","").replace(" H","H")
            return (ipc)
#Title
def TTL (soup):
    for tl in soup.find_all('font',attrs = {'size':'+1'}):
        return (tl.string.replace("\n"," "))
if __name__ == '__main__':
    
    usptobase = "http://patft.uspto.gov/netacgi/nph-Parser?Sect2=PTO1&Sect2=HITOFF&p=1&u=/netahtml/PTO/search-bool.html&r=1&f=G&l=50&d=PALL&RefSrch=yes&Query=PN/"

    with open(r'pn.csv') as csvr:
        with open(r'result.csv','w',newline = '') as csvw:
            patreader = csv.reader(csvr)
            writer = csv.writer(csvw)
            writer.writerow (["Patent No.","Title","Application Date","CPC","IPC","Word Count","Abstract"])
            for row in patreader:
                #patent no.
                patnum = row[0]

                ptourl = usptobase + patnum
                uspto_link = ptourl
                requested = urllib.request.urlopen(uspto_link)
                source = requested.read()
                pto_soup = BeautifulSoup(source,"html5lib")

                #title
                tl = TTL(pto_soup)

                #application date
                Adat = Appdate(pto_soup)

                #CPC
                cpc = CPC(pto_soup)

                #ipc
                ipc = IPC(pto_soup)

                #wordcound
                wc = wordcountABS(pto_soup)

                #Abstract
                abs = ABS(pto_soup)

                writer.writerow([patnum, tl, Adat, cpc, ipc, wc, abs])

    with open(r'pn.csv') as csvr:
        patreader = csv.reader(csvr)
        for row in patreader:
            #patent no.
            patnum = row[0]

            ptourl = usptobase + patnum
            uspto_link = ptourl
            requested = urllib.request.urlopen(uspto_link)
            source = requested.read()
            pto_soup = BeautifulSoup(source,"html5lib")

            #Abstract
            abs = ABS(pto_soup)

            with open(r'p'+ patnum + '.csv','w',newline = '') as csvabs:
                    
                writer = csv.writer(csvabs)
                writer.writerow([abs])

