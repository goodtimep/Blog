# Generated by Django 2.0 on 2018-10-26 19:15

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181026_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aritcledatils',
            name='Text',
        ),
        migrations.AddField(
            model_name='aritcledatils',
            name='Content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='文章内容'),
        ),
    ]
