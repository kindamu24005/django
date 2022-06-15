from django.shortcuts import render

from blog.forms import CommentForm
from .models import Post

# Create your views here.
def frontpage(request):
    posts = Post.objects.all() #データベースにあるpostのデータを全てとってくる。それをpostsの中に格納
    return render(request, "blog/frontpage.html", {"posts": posts}) #{}内はpostsを"posts"で全てviewsに渡してあげる→htmlファイルと連携してサーバーに返す

def post_detail(request, slug): #クリックするとslugにpost-1が入る
    post = Post.objects.get(slug=slug) #post-1とpost-1を照合してそのデータをpostに入れる

    if request.method =="POST":
        form = CommentForm(request.POST)
    return render(request, "blog/post_detail.html", {"post": post}) #それをリターンで返す














