from django.shortcuts import render,HttpResponse
from django.contrib import messages
from user.models import userregistermodel,useralgorithammodels
from django.db.models import Count,Avg
# Create your views here.

def adminlogincheck(request):
    if request.method == "POST":
        usid = request.POST.get('cflgname')
        pswd = request.POST.get('cflgpsswd')
        print("User ID is = ", usid)
        if usid == 'admin' and pswd == 'admin':
            return render(request, 'admins/adminhome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'admins/admins.html')

def activateusers(request):
    dict = userregistermodel.objects.all()
    return render(request,'admins/activateusers.html',{'objects':dict})
def activatewaitedusers(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        status = 'activated'
        print("PID = ", uid,status)
        userregistermodel.objects.filter(id=uid).update(status=status)
    dict = userregistermodel.objects.all()
    return render(request, 'admins/activateusers.html', {'objects': dict})

def adminanalysis(request):
    dict = useralgorithammodels.objects.all()
    return render(request,'admins/adminalgoanalyse.html',{'objects':dict})

def chart(request):
    dataset = useralgorithammodels.objects.values('appliedalgo').annotate(dcount=Avg('accuracy'))
    return render(request, 'admins/charts.html', {'chart_type': 'bar', 'dataset': dataset})