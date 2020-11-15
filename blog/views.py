from django.shortcuts import render,get_object_or_404
from .models import Article , ArticleCategory
# Create your views here.
def all_articles(request):
    articles = Article.published.all()
    context = {"all_articles" :articles}
    return render(request,'blog/all_articles.html',context)
def article_detail(request,id,slug):
    #article = Article.objects.get(id=id,slug=slug)
    article = get_object_or_404(Article,id=id,slug=slug)
    return render(request,'blog/article_detail.html',{'article':article})
def article_category(request,title):
    category = ArticleCategory.objects.get(title=title)
    articles_by_category = Article.objects.filter(category=category)
    return render(request,'blog/article_category.html',{"articles_by_category":articles_by_category})