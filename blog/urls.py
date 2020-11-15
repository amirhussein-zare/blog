from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.all_articles,name = 'all_articles'),
    path('<int:id>/<slug:slug>/',views.article_detail,name= 'artcile_detail'),
    path('category/<str:title>/',views.article_category,name = 'article_category'),
]