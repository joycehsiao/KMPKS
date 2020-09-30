from django.shortcuts import render,HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect
from personal.models import UserProfile
from article.models import article,tag
from bs4 import BeautifulSoup
import random
from django.db.models.aggregates import Count

def index(request):

    return render(request, 'home/index.html',locals())

 

def home(request):
    if request.user.is_authenticated:
        user=UserProfile.objects.get(user=request.user)
        popuPost_list=article.objects.all().order_by('-like')[:4]
        recentPost_list=article.objects.all().order_by('-pubtime')[:4]
        #找最新文章和最受歡迎文章
        img_list=getImg(recentPost_list)
        plainTex_list=getContentText(recentPost_list)
        
        #找最受歡迎的TAG，參考https://blog.csdn.net/qq_25046261/article/details/79178462
        tag_list = tag.objects.annotate(num_posts=Count('article')).order_by("-num_posts")[:4]
        tag_article_list=[]
        for t in tag_list:
            temp_list=article.objects.filter(tags=t).order_by('-like')[:3]
            for i in temp_list:
                tag_article_list.append(i)
                
        t_a_plainText=getContentText(tag_article_list)
        t_a_img_list=getImg(tag_article_list)

        #給前端forloop
        top1tag=[0,1,2]
        top2tag=[3,4,5]
        top3tag=[6,7,8]
        return render(request, 'home/home.html',locals())
    else:
        return HttpResponseRedirect('/accounts/login')

        

def getImg(img):
    img_list=[]
    for u in img:
        if 'img' in u.content:
            soup = BeautifulSoup(u.content, 'html.parser')
            img_tags = soup.find('img')
            for i in soup.select('img'):
                i.extract()
            img_list.append(img_tags.get('src'))
        else:
            index=random.randint(1,3)
            img_list.append('/static/img/default'+str(index)+'.jpg/')

    return img_list

def getContentText(c):
    text_list=[]
    for u in c:
        soup = BeautifulSoup(u.content, 'html.parser')
        for i in soup.select('img'):
            i.extract()
        text_list.append(soup.get_text(' ', strip=True))

    return text_list