# Generated by Django 3.1.1 on 2020-10-22 17:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201022_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.ArticleCategory'),
        ),
    ]
