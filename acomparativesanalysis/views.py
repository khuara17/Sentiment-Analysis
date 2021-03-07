from django.shortcuts import  render,HttpResponse
from .TwitterClientAlgo import TwitterClient
from .models import trendingtopicsmodel
import csv
import string
import random
from django.conf import settings

def index(request):
    return render(request,"base.html",{})


def searchahashtags(request):
    return render(request,'searchtags.html',{})

def searchresults(request):
    dict = {"key1":'Ram'}
    dict1 = {}
    pdict = {}
    ndict = {}
    if request.method =='POST':
        tagname = request.POST.get('cf-name')
        limit = request.POST.get('cf-limit')
        print('Tag Name is ',tagname)
        request.session['tgname'] = tagname
        api = TwitterClient()
        # calling function to get tweets
        #tweets = api.get_tweets(query=tagname, count=200)
        tweets = api.get_tweets(query=tagname, count=limit)
        print("Tw Type ",type(tweets))
        if len(tweets)== 0:
            return  HttpResponse("No tweets Found")

        # picking positive tweets from tweets
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        pcount = 0
        for tw in ptweets:
            pcount +=1
            pdict.update({pcount:tw['text']})
        #dict.update({'positive':ptweets})
        # percentage of positive tweets
        print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
        # picking negative tweets from tweets
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        ncount =141
        for tw in ntweets:
            ncount +=1
            ndict.update({ncount:tw['text']})

        #dict.update({'negative':ntweets})
        ramnuetral = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
        count = 0
        for tw in ramnuetral:
            count += 1
            dict1.update({count:tw['text']})


        #print ('DICT IS ',dict)
        #dict.update({'neutral':ramnuetral})

        neutral = len(tweets) - (len(ptweets) + len(ntweets))
        neutralperc = format(100 * neutral / len(tweets))
        # percentage of negative tweets
        print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
        print("Neutral tweets percentage: {} %".format(100 * neutral / len(tweets)))
        neutralperc = float(format(100 * neutral / len(tweets)))
        positiveperc = float(format(100 * len(ptweets) / len(tweets)))
        negitiveperc = float(format(100 * len(ntweets) / len(tweets)))


        dict.update({'positiveperc':float(round(positiveperc,2))})
        dict.update({'negitiveperc': float(round(negitiveperc, 2))})
        dict.update({'neutralperc': float(round(neutralperc, 2))})

        # printing first 5 positive tweets
        #print("\n\nPositive tweets:")
        #for tweet in ptweets[:10]:
            #print(tweet['text'])

        # printing first 5 negative tweets
        #print("\n\nNegative tweets:")
        #for tweet in ntweets[:10]:
            #print(tweet['text'])

        # printing first 5 Neutral tweets
        #print("\n\nNeutral  tweets:")
        #for tweet in ramnuetral[:10]:
            #print(tweet['text'])
            #dict.update({'neutral': tweet['text']})
    #return HttpResponse("Works FIne")
    try:
        trendingtopicsmodel.objects.create(tagname=tagname)
    except:
        check = trendingtopicsmodel.objects.get(tagname=tagname)
        tcount = check.tagcount
        tcount = tcount+1
        trendingtopicsmodel.objects.filter(tagname=tagname).update(tagcount=tcount)

    #print('Positive Dictionary = ',pdict)
    #print('Negitive Dictionary ',ndict)
    #pdict.update({'sentiment':0})
    #ndict.update({'sentiment':1})
    #dict3 = pdict
    #dict3.update(ndict)
    #print("Generator dictionaty is",dict3)
    var = randomFileName(8)
    file_name = settings.MEDIA_ROOT +'/'+var+ '!'+tagname+'.csv'

    with open(file_name,'w',encoding='UTF-8' ) as f:
        for key in pdict:
            f.write("%s,%s,%s\n"%(key,'0',pdict[key]))
    with open(file_name,'a',encoding='UTF-8') as f:
        for key in ndict:
            f.write("%s,%s,%s\n"%(key,'1',ndict[key]))

    return render(request,'TweetsSearchView.html',{'dict':dict,'nndict':dict1,'pdict':pdict,'ndict':ndict})

def trendingtopics(request):
    dict = trendingtopicsmodel.objects.all().order_by('-tagcount')
    return  render(request,"trending.html",{'objects':dict})

def getTrending(request):
    dict = {"key1": 'Ram'}
    dict1 = {}
    pdict = {}
    ndict = {}
    if request.method == "GET":
        tgname = request.GET.get('tgname')
        request.session['tgname'] = tgname
        api = TwitterClient()
        # calling function to get tweets
        tweets = api.get_tweets(query=tgname, count=200)

        # picking positive tweets from tweets
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        pcount = 0
        for tw in ptweets:
            pcount += 1
            pdict.update({pcount: tw['text']})
        print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
        # picking negative tweets from tweets
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        ncount = 0
        for tw in ntweets:
            ncount += 1
            ndict.update({ncount: tw['text']})

        ramnuetral = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
        count = 0
        for tw in ramnuetral:
            count += 1
            dict1.update({count: tw['text']})

        neutral = len(tweets) - (len(ptweets) + len(ntweets))
        neutralperc = format(100 * neutral / len(tweets))
        # percentage of negative tweets
        print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
        print("Neutral tweets percentage: {} %".format(100 * neutral / len(tweets)))
        neutralperc = float(format(100 * neutral / len(tweets)))
        positiveperc = float(format(100 * len(ptweets) / len(tweets)))
        negitiveperc = float(format(100 * len(ntweets) / len(tweets)))

        dict.update({'positiveperc': float(round(positiveperc, 2))})
        dict.update({'negitiveperc': float(round(negitiveperc, 2))})
        dict.update({'neutralperc': float(round(neutralperc, 2))})

    return render(request, 'TweetsSearchView.html', {'dict': dict, 'nndict': dict1, 'pdict': pdict, 'ndict': ndict})

def user(request):
    return render(request,'user/user.html',{})
def admins(request):
    return render(request,'admins/admins.html',{})

def logout(request):
    return render(request,'base.html',{})
def randomFileName(stringLength=8):
    """Generate a random file Name  of fixed length """
    letters= string.ascii_lowercase
    return ''.join(random.sample(letters,stringLength))