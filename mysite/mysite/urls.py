"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('price/', views.prices, name='price'),
    path('parts/', views.patrs, name='parts'),
    path('contacts/', views.contacts, name='contacts'),
]
from bs4 import BeautifulSoup
import requests
s = requests.session()

url = "https://b2b.ad.ua/views/account/login"
headers = {"Referer": "https://b2b.ad.ua/Account/Login",
            "Origin": "https://b2b.ad.ua",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15"}
s.get(url,headers=headers)

firstresp = requests.get(url,headers=headers)
soup = BeautifulSoup(firstresp.content, "lxml")

token = soup.find("form").find("input").get("value")
data = {"__RequestVerificationToken" : token, "ComId" : "15", "UserName" : "33969", "Password" : "033969", "RememberMe" : "False"}
headers = {"Referer": "https://b2b.ad.ua/Account/Login",
            "Origin": "https://b2b.ad.ua",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15"}

resp = requests.post("https://b2b.ad.ua/views/account/login?__RequestVerificationToken="+token+"&ComId=15&UserName=33969&Password=033969&RememberMe=false")
