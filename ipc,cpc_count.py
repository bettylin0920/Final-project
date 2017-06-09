#encoding=utf-8
import csv
from collections import Counter
import string


#取出 result 內所有內容
allpn = []

file = open('result.csv', 'r')
csvabs = csv.reader(file)

for row in csvabs:
    allpn.append(row)

#IPC print
allipcs = []
for x in allpn:
    allipcs.append(x[4])
allipcs = str(allipcs).replace(" ","").replace('"','').replace("n",' ').replace("",'').replace("IPC","").replace("'",'').replace("[","").replace("]","").replace(",","")
allipcs = allipcs.split(" ")
print (allipcs)

#拉出前4個字元IPC
resultipc = []
a = len(allipcs)
for ipc in range(0,a):
    resultipc.append(allipcs[ipc][0:4])
print (resultipc)
wordipc = Counter(resultipc)
print (wordipc)
print ("IPC count")
for ipcname, count in wordipc.most_common(40):
    print('{0} {1}'.format(count, ipcname))

#cpc print
allcpcs = []
for x in allpn:
    allcpcs.append(x[3])
allcpcs = str(allcpcs).replace(" ","").replace('"','').replace("n",' ').replace("",'').replace("IPC","").replace("'",'').replace("[","").replace("]","").replace(",","")
allcpcs = allcpcs.split(" ")
print (allcpcs)

#拉出前四個字元CPC
resultcpc = []
a = len(allcpcs)
for cpc in range(0,a):
    resultcpc.append(allcpcs[cpc][0:4])
print (resultcpc)
wordcpc = Counter(resultcpc)
print (wordcpc)
print ("CPC count")
for cpcname, count in wordcpc.most_common(40):
    print('{0} {1}'.format(count, cpcname))

with open('ipccount.csv', 'w') as csvfile:
    # set up header
    fieldnames = ['IPC分類', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for word, count in wordipc.most_common(40):
        writer.writerow({'IPC分類': word, 'count': count})

with open('cpccount.csv', 'w') as csvfile:
    # set up header
    fieldnames = ['CPC分類', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for word, count in wordcpc.most_common(40):
        writer.writerow({'CPC分類': word, 'count': count})

