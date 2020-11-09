from django.db import models
from django.conf import settings
from markdownx.models import MarkdownxField

class Prefecture(models.Model):
    name = models.CharField('都道府県名', max_length=30)
    slug = models.SlugField('英語名', unique=True)

    class Meta:
        verbose_name = '都道府県名'
        verbose_name_plural = '都道府県リスト'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=30)
    slug = models.SlugField('英語名', unique=True)

    class Meta:
        verbose_name = 'カテゴリー名'
        verbose_name_plural = 'カテゴリーリスト'

    def __str__(self):
        return self.name

class Post(models.Model):
    prefecture = models.ForeignKey(Prefecture, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    thumbnail = models.ImageField('サムネ', upload_to='images/')
    title = models.CharField('タイトル', max_length=75)
    description = models.CharField('headタグでの説明', max_length=255, blank=False)
    content = MarkdownxField('本文')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField('公開日', blank=False, null=True)
    is_public = models.BooleanField('公開する', default=False)

    def get_markdown_text_as_html(self):
        """MarkDown記法で書かれたtextをHTML形式に変換して返す"""
        return markdown(self.content, extensions=settings.MARKDOWNX_MARKDOWN_EXTENSIONS)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '記事'
        verbose_name_plural = '投稿リスト'

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
