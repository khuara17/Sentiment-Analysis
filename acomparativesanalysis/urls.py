"""acomparativesanalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from .views import index,searchahashtags,searchresults,trendingtopics,getTrending,user,admins,logout
from user.views import userregister,userlogincheck,usernaivebayes,usernaivetest,usersvm,usersvmtest,rfanalyse,rftest,decesiontreeanalyze,decesiontreetest,lstmanalysis,lstmtest,UserChart
from admins.views import adminlogincheck,activateusers,activatewaitedusers,adminanalysis,chart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$',index,name='index'),
    url(r'^searchahashtags/',searchahashtags,name="searchahashtags"),
    url(r'^searchresults/',searchresults,name='searchresults'),
    url(r'^trendingtopics/',trendingtopics,name='trendingtopics'),
    url(r'^getTrending/',getTrending,name='getTrending'),
    url(r'^user/',user,name='user'),
    url(r'^admins/',admins,name='admins'),
    url(r'^logout/',logout,name='logout'),

    url(r'^userregister/',userregister,name='userregister'),
    url(r'^userlogincheck/',userlogincheck,name='userlogincheck'),
    url(r'^usernaivebayes/',usernaivebayes,name='usernaivebayes'),
    url(r'^usernaivetest/',usernaivetest,name='usernaivetest'),
    url(r'^usersvm/',usersvm,name='usersvm'),
    url(r'^usersvmtest/',usersvmtest,name='usersvmtest'),
    url(r'^rfanalyse/',rfanalyse,name='rfanalyse'),
    url(r'^rftest/',rftest,name='rftest'),
    url(r'^decesiontreeanalyze/',decesiontreeanalyze,name='decesiontreeanalyze'),
    url(r'^decesiontreetest/',decesiontreetest,name='decesiontreetest'),
    url(r'lstmanalysis/',lstmanalysis,name='lstmanalysis'),
    url(r'lstmtest/',lstmtest,name='lstmtest'),
    url(r'UserChart/',UserChart,name='UserChart'),

    url(r'^adminlogincheck/',adminlogincheck,name='adminlogincheck'),
    url(r'^activateusers/',activateusers,name='activateusers'),
    url(r'^activatewaitedusers/',activatewaitedusers,name='activatewaitedusers'),
    url(r'^adminanalysis/',adminanalysis,name='adminanalysis'),
    url(r'^chart/',chart,name='chart'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)