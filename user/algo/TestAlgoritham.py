'''import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import nltk.classify.util
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import roc_curve, auc
from nltk.classify import NaiveBayesClassifier
import numpy as np
import re
import string
import nltk
'''
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer, PorterStemmer
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob

amz_reviews = pd.read_csv("7817_1.csv")

amz_reviews.shape
amz_reviews.columns
#Index(['id', 'asins', 'brand', 'categories','colors', 'dateAdded', 'dateUpdated', 'dimension', 'ean', 'keys','manufacturer','manufacturerNumber','name','prices', 'reviews.date','reviews.doRecommend','reviews.numHelpful', 'reviews.rating','reviews.sourceURLs','reviews.text','reviews.title','reviews.userCity', 'reviews.userProvince', 'reviews.username', 'sizes','upc','weight'],dtype='object')

#columns = ['id','name','keys','manufacturer','dateAdded', 'reviews.date','reviews.numHelpful', 'reviews.userCity', 'reviews.userProvince', 'ean', 'reviews.doRecommend','asins','sizes', 'weight', 'reviews.sourceURLs', 'reviews.title']

df = pd.DataFrame(amz_reviews)

df['reviews.rating'].value_counts().plot(kind='bar')
## Change the reviews type to string
df['reviews.text'] = df['reviews.text'].astype(str)
## Before lowercasing
df['reviews.text'][2]
## Lowercase all reviews
df['reviews.text'] = df['reviews.text'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df['reviews.text'][2] ## to see the difference

## remove punctuation
df['reviews.text'] = df['reviews.text'].str.replace('[^ws]','')
df['reviews.text'][2]

stop = stopwords.words('english')
df['reviews.text'] = df['reviews.text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
df['reviews.text'][2]

st = PorterStemmer()

df['reviews.text'] = df['reviews.text'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))
df['reviews.text'][2]
def senti(x):
    vx = TextBlob(x).sentiment
    #print(vx)
    return vx

df['senti_score'] = df['reviews.text'].apply(senti)

print(df.senti_score.head())




'''
#%matplotlib inline
temp = pd.read_csv("7817_1.csv")
temp.head()
print(temp.head())
permanent = temp[['reviews.rating' , 'reviews.text' , 'reviews.title' , 'reviews.username','brand']]
print(permanent.isnull().sum()) #Checking for null values
permanent.head()
check =  permanent[permanent["reviews.rating"].isnull()]
check.head()
senti= permanent[permanent["reviews.rating"].notnull()]
permanent.head()
#senti["senti"] = senti["reviews.rating"]>=4
#senti["senti"] = senti["senti"].replace([True , False] , ["pos" , "neg"])
'''