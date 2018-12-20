# Generated by Django 2.0 on 2018-12-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comment_personalblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbehavior',
            name='UserAgent',
            field=models.CharField(max_length=500, null=True, verbose_name='用户设备信息'),
        ),
        migrations.AlterField(
            model_name='userbehavior',
            name='IP',
            field=models.CharField(max_length=300, verbose_name='用户ip'),
        ),
    ]
