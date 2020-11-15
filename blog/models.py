from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from extensions.uutils import jalali_convertor

# Create your models here.
class PublishArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish')

class ArticleCategory(models.Model):
    title      = models.CharField(max_length=200,verbose_name='عنوان دسته بندی',unique=True)
    status     = models.BooleanField(default=True,verbose_name='آیا نمایش داده شود؟')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name        = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    
class Article(models.Model):
    STATUS = (
        ('publish','Publish'),
        ('draft','Draft'),
        #(IN DB , IN AP)
    )
    title = models.CharField(max_length=120,verbose_name='عنوان مقاله')
    slug  = models.SlugField(max_length=120,unique=True,allow_unicode=True,verbose_name='آدرس مقاله')
    writer = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نویسنده مقاله')
    body = RichTextUploadingField(verbose_name='بدنه مقاله')
    category =models.ManyToManyField(ArticleCategory,verbose_name='دسته بندی مقاله')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) #django saves this time and you cant see it in admin panel it cant be changed
    updated = models.DateTimeField(auto_now=True)     #django saves it time and you cant see it in admin panel when it changes and created it can be changed
    status = models.CharField(max_length=30,choices=STATUS,default='d') 
    published = PublishArticleManager()
    objects = models.Manager()
    
    def get_absolute_url(self):
        return reverse('blog:artcile_detail', args=[self.id, self.slug])
    def jpublish(self):
        return jalali_convertor(self.publish)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name        = "مقاله"
        verbose_name_plural = "مقالات"