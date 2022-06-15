#データベースに接続するモデル

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255) #文字をtitleに格納
    slug = models.SlugField() #ブログ記事の投稿番号をslugに格納
    intro = models.TextField()
    body = models.TextField() #文字を打つことができるフィールド
    posted_date = models.DateField(auto_now_add=True) #日付を打つことができるフィールド（auto_now_addはリアルタイムを自動で入力）



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    #ForeignKey:1対多の関係の時に使う
    #on_delete:本文を消すと他のemail情報とかname情報とかも全て消すようになる、、、みたいな
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)