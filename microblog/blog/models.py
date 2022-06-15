#データベースに接続するモデル

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255) #文字をtitleに格納
    slug = models.SlugField() #ブログ記事の投稿番号をslugに格納
    intro = models.TextField()
    body = models.TextField() #文字を打つことができるフィールド
    posted_date = models.DateField(auto_now_add=True) #日付を打つことができるフィールド（auto_now_addはリアルタイムを自動で入力）