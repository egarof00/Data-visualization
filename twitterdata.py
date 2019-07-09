import json
from textblob import TextBlob
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud


polarity=[]
subjectivity=[]
polardic={}
#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
for each in tweetData:
    tb = TextBlob(each["text"])
    polarity.append(tb.polarity)
    averagep=sum(polarity)/len(polarity)
    polardic[tb] = tb.polarity
    # print("Average of polarity=",averagep)
    subjectivity.append(tb.subjectivity)
    averages=sum(subjectivity)/len(subjectivity)
    # print("Average of subjectivity=",subjectivity)
print("Average of polarity=", averagep)
print("Average of subjectivity=", averages)
string = str(polardic.keys())

num_bins=5
n, bins, patches = plt.hist(polarity, num_bins, facecolor='purple', alpha=.75)
plt.show()
n, bins, patches=plt.hist(subjectivity, num_bins, facecolor='red', alpha=1)
plt.show()

word_count={}
twt_str=""

for each in tweetData:
     twt_str+=(each["text"])
     twt_str=twt_str.lower()
twtblob= TextBlob(twt_str)
tweet_list=twtblob.words
for each in tweet_list:
    if len(each)>3 and each != "https" and each.isalpha():
        if each not in word_count:
            word_count[each] = 1
        else:
            word_count[each]+=1
wc=WordCloud(background_color="white", width=900, height=500, relative_scaling=1).generate_from_frequencies(word_count)
plt.imshow(wc, interpolation ='bilinear')
plt.show()

for each in polardic:
    if polardic.values() <0:
        string = str(polardic.keys())
