import tweepy
import re
import pickle
from tweepy import OAuthHandler

consumer_key='wDxWsBbddRAPIpDGENi0xT293'
consumer_secret='mIluDhb0OnKhH7RqUwQs1k1YuOc5S605XpSzs33OlxKvO6PsDc'
access_token='977211089598537729-CebElt3VJlhH4mg7AAQJWoMrKCN71Gx'
access_secret='sycX3R2QShMlOtRAgQaUNZRudjYvFiMtU2NubJquDZXVc'

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
args=['redmi note6']
api=tweepy.API(auth,timeout=10)

list_tweets=[]
query=args[0]
if len(args)==1:
    for status in tweepy.Cursor(api.search,q=query+" -filter:retweets",lang='en',result_type='recent').items(100):
        list_tweets.append(status.text)
        
with open('tfidfmodel.pickle','rb') as f:
    vectorizer=pickle.load(f)
    
with open('classifier.pickle','rb') as f:
    clf=pickle.load(f)
    
    
sent_list=[]
for tweet in list_tweets:
    tweet=re.sub(r"^https://t.co/[a-zA-Z0-9]*\s"," ",tweet)
    tweet=re.sub(r"\s+https://t.co/[a-zA-Z0-9]*\s"," ",tweet)
    tweet=re.sub(r"\s+https://t.co/[a-zA-Z0-9]*$"," ",tweet)
    tweet=tweet.lower()
    tweet=re.sub(r"that's","that is",tweet)
    tweet=re.sub(r"there's","there is",tweet)
    tweet=re.sub(r"what's","what is",tweet)
    tweet=re.sub(r"where's","where is",tweet)
    tweet=re.sub(r"it's","it is",tweet)
    tweet=re.sub(r"who's","who is",tweet)
    tweet=re.sub(r"i'm","i am",tweet)
    tweet=re.sub(r"she's","she is",tweet)
    tweet=re.sub(r"he's","he is",tweet)
    tweet=re.sub(r"they're","they are",tweet)
    tweet=re.sub(r"who're","who are",tweet)
    tweet=re.sub(r"ain't","am not",tweet)
    tweet=re.sub(r"wouldn't","would not",tweet)
    tweet=re.sub(r"shouldn't","should not",tweet)
    tweet=re.sub(r"can't","can not",tweet)
    tweet=re.sub(r"couldn't","could not",tweet)
    tweet=re.sub(r"won't","will not",tweet)
    tweet=re.sub(r"\W"," ",tweet)
    tweet=re.sub(r"\d"," ",tweet)
    tweet=re.sub(r"s+[a-z]\s+"," ",tweet)
    tweet=re.sub(r"\s+[a-z]$"," ",tweet)
    tweet=re.sub(r"^[a-z]\s+"," ",tweet)
    tweet=re.sub(r"\s+"," ",tweet)
    sent=clf.predict(vectorizer.transform([tweet]).toarray())
    sent_list.append(sent)
