from django.contrib import admin
from .models import Article,  ArticleCategory
# Register your models here.

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display  = ('title','status')
    list_filter   = (['status'])
    search_fields = ('title',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','writer','publish','status')
    list_filter = ('status','writer','publish')
    search_fields = ('title','body')
    raw_id_fields = ('writer',)
    prepopulated_fields = {"slug":('title',)}
    list_editable = ('status',)