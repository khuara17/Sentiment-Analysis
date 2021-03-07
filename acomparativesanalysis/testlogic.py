from TwitterClientAlgo import TwitterClient
def main(tag):
	# creating object of TwitterClient Class
	api = TwitterClient()
	# calling function to get tweets
	tweets = api.get_tweets(query = tag, count = 200)

	# picking positive tweets from tweets
	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
	# percentage of positive tweets
	print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
	# picking negative tweets from tweets
	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	ramnuetral = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
	neutral = len(tweets)-(len(ptweets) + len(ntweets))
	# percentage of negative tweets
	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
	print("Neutral tweets percentage: {} %".format(100*neutral/len(tweets)))

	# printing first 5 positive tweets
	print("\n\nPositive tweets:")
	for tweet in ptweets[:10]:
		print(tweet['text'])

	# printing first 5 negative tweets
	print("\n\nNegative tweets:")
	for tweet in ntweets[:10]:
		print(tweet['text'])

    # printing first 5 Neutral tweets
	print("\n\nNeutral  tweets:")
	for tweet in ramnuetral[:10]:
		print(tweet['text'])

if __name__ == "__main__":
    tag = 'Sachin'
    main(tag)
	# calling main function


