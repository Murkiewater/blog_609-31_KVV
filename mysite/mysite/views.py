from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article

def homepage(request):
    articles = Article.objects.all().order_by('date')
    data = {"header": "Homepage", 
            "what": "This website is used for article showing. write, read and engage!",
            "artshow": "Here are the latest articles:",
            "articles": articles
            }
    return render(request, 'homepage.html', context=data)

def about(request):
    header = "About us"
    staff = ['John Nicho', 'John Roger', 'Timothy Smith']
    director = {"name": "David Lee", "img": '/director.jpg'}
    address = ('20 W 34th St.', 'New York', 'NY 10001', 'USA')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', data)

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, '../articles/article_list.html', {'articles': articles})