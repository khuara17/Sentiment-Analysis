from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import userregistermodel,useralgorithammodels
from .forms import userregisterform
from django.contrib import messages
from django.conf import settings
import os
from .algo.dpNaiveBayes import NaivebayesDPH
from .algo import svm
from .algo import randomforest
from .algo import decisiontree
from datetime import datetime
from .deeplearning.lstmdesc import lstmScore

from django.db.models import Count,Avg


# Create your views here.

def userregister(request):
    if request.method == 'POST':
        form = userregisterform(request.POST)
        if form.is_valid():
            try:
                rslt = form.save()
                print("Form Result Status ", rslt)
                messages.success(request, 'You have been successfully registered')
            except:
                messages.success(request, 'Email Already Registerd')
            return HttpResponseRedirect('user/userregister.html')
        else:
            print("Invalid form")
    else:
        form = userregisterform()
    return render(request, 'user/userregister.html', {'form': form})

def userlogincheck(request):
    if request.method == "POST":
        email = request.POST.get('cf-email')
        pswd = request.POST.get('cf-password')
        dict = {}
        print("Email = ",pswd)
        try:
            check = userregistermodel.objects.get(email=email, password=pswd)
            request.session['id'] = check.id
            request.session['loggeduser'] = check.name
            request.session['email'] = check.email
            status = check.status
            if status == "activated":
                print("User id At", check.id, status)
                dirName = settings.MEDIA_ROOT
                listOfFile = getListOfFiles(dirName)
                #print('List Files ',listOfFile)
                count = 0;
                for x in listOfFile:
                    count += 1
                    x1 = os.path.basename(x)
                    dict.update({count:x1})
                    #print ('Files = ',dict)
                return render(request, 'user/userpage.html',{'dict':dict})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'user/user.html')

            return render(request, 'user/userpage.html',{'dict':dict})
        except:
            pass
    messages.success(request, 'Invalid Email id and password')
    return render(request, 'user/user.html')


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def usernaivebayes(request):
    dict = {}
    dirName = settings.MEDIA_ROOT
    listOfFile = getListOfFiles(dirName)
    # print('List Files ',listOfFile)
    count = 0;
    for x in listOfFile:
        count += 1
        x1 = os.path.basename(x)
        dict.update({count: x1})
    #print("Dict is ",dict)
    return render(request, 'user/usernaivebayes.html', {'dict': dict})

def usernaivetest(request):
    if request.method == "GET":
        dataset = request.GET.get('datasetname')
        print("Naive Dataset Name ",dataset)
        data = NaivebayesDPH(dataset)
        dict = data.mainmethod()
        algorithm = 'Naive Bayes'
        name = request.session['loggeduser']
        email = request.session['email']
        now = datetime.now()
        dt_string = now.strftime("%B %d, %Y  %H:%M:%S %p %A %Z")
        useralgorithammodels.objects.create(name=name,email=email,appliedalgo=algorithm,datasetname=dataset,currectrecord=dict['correct'],totalrecord=dict['total'],accuracy=dict['result'])
        print('Results ',dict)
    return render(request,'user/naiveresults.html',dict)
def usersvm(request):
    dict = {}
    dirName = settings.MEDIA_ROOT
    listOfFile = getListOfFiles(dirName)
    count = 0;
    for x in listOfFile:
        count += 1
        x1 = os.path.basename(x)
        dict.update({count: x1})
    return render(request, 'user/usersvmpage.html', {'dict': dict})

def usersvmtest(request):
    if request.method == "GET":
        dataset = request.GET.get('datasetname')
        print("SVM Dataset Name ",dataset)

    dict = svm.mymain(dataset)
    algorithm = 'SVM'
    name = request.session['loggeduser']
    email = request.session['email']
    now = datetime.now()
    dt_string = now.strftime("%B %d, %Y  %H:%M:%S %p %A %Z")
    useralgorithammodels.objects.create(name=name, email=email, appliedalgo=algorithm, datasetname=dataset,
                                        currectrecord=dict['correct'], totalrecord=dict['total'],
                                        accuracy=dict['result'])

    #print('Results of Dict ',dict)
    return render(request,'user/svmresult.html',dict)

def rfanalyse(request):
    dict = {}
    dirName = settings.MEDIA_ROOT
    listOfFile = getListOfFiles(dirName)
    count = 0;
    for x in listOfFile:
        count += 1
        x1 = os.path.basename(x)
        dict.update({count: x1})
    return render(request, 'user/rfanalysepage.html', {'dict': dict})

def rftest(request):
    if request.method == "GET":
        dataset = request.GET.get('datasetname')
        print("RF Dataset Name ",dataset)


    dict = randomforest.rfmainfun(dataset)
    algorithm = 'Random Forest'
    name = request.session['loggeduser']
    email = request.session['email']
    now = datetime.now()
    dt_string = now.strftime("%B %d, %Y  %H:%M:%S %p %A %Z")
    useralgorithammodels.objects.create(name=name, email=email, appliedalgo=algorithm, datasetname=dataset,
                                        currectrecord=dict['correct'], totalrecord=dict['total'],
                                        accuracy=dict['result'])
    return render(request,'user/rfresult.html',dict)

def decesiontreeanalyze(request):
    dict = {}
    dirName = settings.MEDIA_ROOT
    listOfFile = getListOfFiles(dirName)
    count = 0;
    for x in listOfFile:
        count += 1
        x1 = os.path.basename(x)
        dict.update({count: x1})
    return render(request, 'user/dtpage.html', {'dict': dict})

def decesiontreetest(request):
    if request.method == "GET":
        dataset = request.GET.get('datasetname')
        print("DT Dataset Name ",dataset)


    dict = decisiontree.dtmain(dataset)
    algorithm = 'Decision Tree'
    name = request.session['loggeduser']
    email = request.session['email']
    now = datetime.now()
    dt_string = now.strftime("%B %d, %Y  %H:%M:%S %p %A %Z")
    useralgorithammodels.objects.create(name=name, email=email, appliedalgo=algorithm, datasetname=dataset,
                                        currectrecord=dict['correct'], totalrecord=dict['total'],
                                        accuracy=dict['result'])
    return render(request,'user/dtresultpage.html',dict)




def lstmanalysis(request):
    dict = {}
    dirName = settings.MEDIA_ROOT
    listOfFile = getListOfFiles(dirName)
    count = 0;
    for x in listOfFile:
        count += 1
        x1 = os.path.basename(x)
        dict.update({count: x1})
    return render(request, 'user/lstmpage.html', {'dict': dict})
def lstmtest(request):
    if request.method == "GET":
        dataset = request.GET.get('datasetname')
        print("LSTM Dataset Name ",dataset)


    dict = decisiontree.dtmain(dataset)
    top_words = dict['correct']
    accuracy = lstmScore(top_words)
    print('LSTM Accuracy ',accuracy)
    dict.update({'lstm':accuracy})
    algorithm = 'LSTM'
    name = request.session['loggeduser']
    email = request.session['email']
    now = datetime.now()
    dt_string = now.strftime("%B %d, %Y  %H:%M:%S %p %A %Z")
    useralgorithammodels.objects.create(name=name, email=email, appliedalgo=algorithm, datasetname=dataset,
                                        currectrecord=dict['correct'], totalrecord=dict['total'],
                                        accuracy=accuracy)
    return render(request,'user/lstmresultpage.html',dict)


def UserChart(request):
    dataset = useralgorithammodels.objects.values('appliedalgo').annotate(dcount=Avg('accuracy'))
    return render(request, 'user/usercharts.html', {'chart_type': 'bar', 'dataset': dataset})