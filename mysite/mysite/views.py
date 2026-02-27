from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article


def homepage(request):
    article = Article.objects.all().order_by('date')[2::-1]
    return render(request, 'homepage.html', {'latest_articles': article})


def about(request):
    staff = ['Tommas Edison', 'Michel Romen', 'Timothy Smith']
    director = {"name": "Jacky Chan", "img": '/director.jpg'}
    email = "info@mysite.ru"
    telephone = "+7 (999) 123-45-67"
    address = ('20 W 34th St.', 'New York', 'NY 10001', 'USA')
    data = {"staff": staff, "director": director, "email": email, "telephone": telephone, "address": address}
    return render(request, 'about.html', data)
