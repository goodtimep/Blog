# Generated by Django 2.0 on 2018-11-05 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryName', models.CharField(max_length=50, verbose_name='分类名')),
                ('BackgroundPath', models.CharField(max_length=100, verbose_name='背景地址')),
                ('CategoryLog', models.CharField(max_length=100, null=True, verbose_name='Log地址')),
                ('Intor', models.CharField(max_length=200, null=True, verbose_name='分类详情')),
                ('Id', models.AutoField(primary_key=True, serialize=False, verbose_name='类ID')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
            },
        ),
    ]
