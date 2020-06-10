from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')

def prices(request):
    content = {"zag": "Нашей основной целью является предоставление вам максимально возможного качества обслуживания каждый раз, чтобы ваш автомобиль работал как новый.",
               "page": "Стоимость услуг"}

    return render(request, 'template.html', context=content)

def news(request):
    return render(request, 'template.html')