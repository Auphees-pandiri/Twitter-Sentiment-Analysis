# Twitter-Sentiment-Analysis
In these days twitter is being used largely.Everyday there are a lot of trends creating on the twitter.So in order to know whether they are positive or negative I developed this project.I extracted the data from twitter using tweepy and then I applied sentiment analysis on this data to find whether the tweet is positive or negative. In this way I analyzed the tweets..

# Creating a twitter app
First go to https://developer.twitter.com/en/apps this link.Then login into your account.And then click on create an app.Then fill all the details of yours.Now you will have consumer api key, consumer api secret key and also access token and access token secret.
Note down these details and include them in your program.

# steps involved in twitter sentiment analysis 

step1: Import the libraries   
step2: Store the consumer api key,consumer api secret key,access token and access token secret in variables    
step3: Authentication and accessing  
step4: Give some word to args.Tweets related to this word are retrieved  
step5: Unpickling the tfidfmodel and classifier files   
step6: Preprocessing on the tweets    
step7: Predicting the sentiment of the tweet   
