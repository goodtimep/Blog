# Generated by Django 2.0 on 2018-11-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181106_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ArticleName',
            field=models.CharField(max_length=20, verbose_name='文章名'),
        ),
        migrations.AlterField(
            model_name='article',
            name='BackgroundPath',
            field=models.CharField(max_length=50, verbose_name='文章背景地址'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CategoryName',
            field=models.CharField(max_length=10, verbose_name='分类名'),
        ),
    ]