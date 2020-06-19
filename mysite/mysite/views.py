from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')

def prices(request):
    content = {"zag": "Нашей основной целью является предоставление вам максимально возможного качества обслуживания каждый раз, чтобы ваш автомобиль работал как новый.",
               "page": "Стоимость услуг"}

    return render(request, 'template.html', context=content)

def news(request):
    s = requests.get("http://auto.bigmir.net/autonews")
    soup = BeautifulSoup(s.content,"html.parser")
    news_header = []
    news_body = []
    list = soup.find_all("li", class_="b-prev-articles__list-item g-clearfix")
    for item in list:
        tag = item.find_all("a", class_="b-prev-articles__list-item__title")
        news_header.append(tag[0].text)
        tag = item.find_all("div", class_="b-prev-articles__list-item__description")
        news_body.append(tag[0].text)

    # сделать циклом 10 новостей
    # вывести в дикт

    news_cont = dict(zip(news_header, news_body))
    content = {"news": news_cont}
    return render(request, 'template.html', content)
