# Generated by Django 3.1.3 on 2020-11-09 10:48

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='カテゴリー名')),
                ('slug', models.SlugField(unique=True, verbose_name='英語名')),
            ],
            options={
                'verbose_name': 'カテゴリー名',
                'verbose_name_plural': 'カテゴリーリスト',
            },
        ),
        migrations.CreateModel(
            name='Prefecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='都道府県名')),
                ('slug', models.SlugField(unique=True, verbose_name='英語名')),
            ],
            options={
                'verbose_name': '都道府県名',
                'verbose_name_plural': '都道府県リスト',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='images/', verbose_name='サムネ')),
                ('title', models.CharField(max_length=75, verbose_name='タイトル')),
                ('description', models.CharField(max_length=255, verbose_name='headタグでの説明')),
                ('content', markdownx.models.MarkdownxField(verbose_name='本文')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(null=True, verbose_name='公開日')),
                ('is_public', models.BooleanField(default=False, verbose_name='公開する')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tourismapi.category')),
                ('prefecture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tourismapi.prefecture')),
            ],
            options={
                'verbose_name': '記事',
                'verbose_name_plural': 'ブログ投稿',
                'ordering': ['-created_at'],
            },
        ),
    ]
