from django.shortcuts import render
from newsapi import NewsApiClient
from newsApp.models import Post,Saved
from django.http import HttpResponse
# from django.template import context
# Create your views here.
mylist = []
def index(request): 
    Post.objects.all().delete()
    newsApi = NewsApiClient(api_key = '508840f478804c84a86421ab5394a080')  #https://newsapi.org/v2/top-headlines?country=in&apiKey=508840f478804c84a86421ab5394a080
    headLines = newsApi.get_top_headlines( sources="bbc-news, the-verge")  #bbc-news, the-verge  sources = 'the-times-of-india, google-news',
    articles = headLines['articles']
    
    desc = []
    news = []
    img = []
    idd = []
    
    for i in range(len(articles)):
        article = articles[i]
        idd.append(i)
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        Post.objects.create(idd = i, desc = desc[i], news = news[i], img = img[i])
    mylist = zip(idd, news, desc, img)


    return render(request, "main/index.html", context = {"mylist": mylist})

    # return render(request, 'blog/index.html',
    #          context={'all_articles': all_articles, 'message': 'Write something!'})

def readmore(request):
    tmp = request.GET["ib"]
    me = Post.objects.get(idd = tmp)
    return render(request, "main/readmore.html", context = {"news": me.news, "desc": me.desc, "img": me.img})

def save(request):
    tmp = request.GET["ib"]
    me = Post.objects.get(idd = tmp)
    print(tmp)
    Saved.objects.create(idd = me.idd, desc = me.desc, news = me.news, img = me.img)


    #additional
    desc = []
    news = []
    img = []
    idd = []
    saved = Saved.objects.all()
    for ob in saved:
        desc.append(ob.desc)
        news.append(ob.news)
        img.append(ob.img)
    savedlist = zip(news,desc,img)
    return render(request, "main/save.html", context = {"savedlist": savedlist})

def delete(request):
    Saved.objects.all().delete()
    return render(request, "main/delete.html")


def sports(request):
    Post.objects.all().delete()
    newsApi = NewsApiClient(api_key = '508840f478804c84a86421ab5394a080')  #https://newsapi.org/v2/top-headlines?country=in&apiKey=508840f478804c84a86421ab5394a080
    headLines = newsApi.get_top_headlines( category = 'sports')  #bbc-news, the-verge  sources = 'the-times-of-india, google-news',
    articles = headLines['articles']
    
    desc = []
    news = []
    img = []
    idd = []
    
    for i in range(len(articles)):
        article = articles[i]
        idd.append(i)
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        Post.objects.create(idd = i, desc = desc[i], news = news[i], img = img[i])
    mylist = zip(idd, news, desc, img)
    return render(request, "main/index.html", context = {"mylist": mylist})

def sports(request):
    Post.objects.all().delete()
    newsApi = NewsApiClient(api_key = '508840f478804c84a86421ab5394a080')  #https://newsapi.org/v2/top-headlines?country=in&apiKey=508840f478804c84a86421ab5394a080
    headLines = newsApi.get_top_headlines(category="sports", country="in")  #bbc-news, the-verge  sources = 'the-times-of-india, google-news',
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    idd = []
    
    for i in range(len(articles)):
        article = articles[i]
        idd.append(i)
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        Post.objects.create(idd = i, desc = desc[i], news = news[i], img = img[i])
    mylist = zip(idd, news, desc, img)
    return render(request, "main/index.html", context = {"mylist": mylist})

def science(request):
    Post.objects.all().delete()
    newsApi = NewsApiClient(api_key = '508840f478804c84a86421ab5394a080')  #https://newsapi.org/v2/top-headlines?country=in&apiKey=508840f478804c84a86421ab5394a080
    headLines = newsApi.get_top_headlines(category = "science")  #bbc-news, the-verge  sources = 'the-times-of-india, google-news',
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    idd = []
    
    for i in range(len(articles)):
        article = articles[i]
        idd.append(i)
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        Post.objects.create(idd = i, desc = desc[i], news = news[i], img = img[i])
    mylist = zip(idd, news, desc, img)
    return render(request, "main/index.html", context = {"mylist": mylist})

def india(request):
    Post.objects.all().delete()
    newsApi = NewsApiClient(api_key = '508840f478804c84a86421ab5394a080')  #https://newsapi.org/v2/top-headlines?country=in&apiKey=508840f478804c84a86421ab5394a080
    headLines = newsApi.get_top_headlines(sources="the-times-of-india")  #bbc-news, the-verge  sources = 'the-times-of-india, google-news',
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    idd = []
    
    for i in range(len(articles)):
        article = articles[i]
        idd.append(i)
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        Post.objects.create(idd = i, desc = desc[i], news = news[i], img = img[i])
    mylist = zip(idd, news, desc, img)
    return render(request, "main/index.html", context = {"mylist": mylist})

def entertainment(request):
    Post.objects.all().delete()
    newsApi = NewsApiClient(api_key = '508840f478804c84a86421ab5394a080')  #https://newsapi.org/v2/top-headlines?country=in&apiKey=508840f478804c84a86421ab5394a080
    headLines = newsApi.get_top_headlines(category="entertainment", country="in")  #bbc-news, the-verge  sources = 'the-times-of-india, google-news',
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    idd = []
    
    for i in range(len(articles)):
        article = articles[i]
        idd.append(i)
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        Post.objects.create(idd = i, desc = desc[i], news = news[i], img = img[i])
    mylist = zip(idd, news, desc, img)
    return render(request, "main/index.html", context = {"mylist": mylist})

def us(request):
    Post.objects.all().delete()
    newsApi = NewsApiClient(api_key = '508840f478804c84a86421ab5394a080')  #https://newsapi.org/v2/top-headlines?country=in&apiKey=508840f478804c84a86421ab5394a080
    headLines = newsApi.get_top_headlines(country="us")  #bbc-news, the-verge  sources = 'the-times-of-india, google-news',
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    idd = []
    
    for i in range(len(articles)):
        article = articles[i]
        idd.append(i)
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        Post.objects.create(idd = i, desc = desc[i], news = news[i], img = img[i])
    mylist = zip(idd, news, desc, img)
    return render(request, "main/index.html", context = {"mylist": mylist})


def health(request):
    Post.objects.all().delete()
    newsApi = NewsApiClient(api_key = '508840f478804c84a86421ab5394a080')  #https://newsapi.org/v2/top-headlines?country=in&apiKey=508840f478804c84a86421ab5394a080
    headLines = newsApi.get_top_headlines(category="health")  #bbc-news, the-verge  sources = 'the-times-of-india, google-news',
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    idd = []
    
    for i in range(len(articles)):
        article = articles[i]
        idd.append(i)
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        Post.objects.create(idd = i, desc = desc[i], news = news[i], img = img[i])
    mylist = zip(idd, news, desc, img)
    return render(request, "main/index.html", context = {"mylist": mylist})

def world(request):
    Post.objects.all().delete()
    newsApi = NewsApiClient(api_key = '508840f478804c84a86421ab5394a080')  #https://newsapi.org/v2/top-headlines?country=in&apiKey=508840f478804c84a86421ab5394a080
    headLines = newsApi.get_top_headlines(sources="bbc-news, the-verge")  #bbc-news, the-verge  sources = 'the-times-of-india, google-news',
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    idd = []
    
    for i in range(len(articles)):
        article = articles[i]
        idd.append(i)
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        Post.objects.create(idd = i, desc = desc[i], news = news[i], img = img[i])
    mylist = zip(idd, news, desc, img)
    return render(request, "main/index.html", context = {"mylist": mylist})

