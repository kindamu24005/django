from django.shortcuts import redirect, render

from blog.forms import CommentForm
from .models import Comment, Post

# Create your views here.
def frontpage(request):
    posts = Post.objects.all() #データベースにあるpostのデータを全てとってくる。それをpostsの中に格納
    return render(request, "blog/frontpage.html", {"posts": posts}) #{}内はpostsを"posts"で全てviewsに渡してあげる→htmlファイルと連携してサーバーに返す

def post_detail(request, slug): #クリックするとslugにpost-1が入る
    post = Post.objects.get(slug=slug) #post-1とpost-1を照合してそのデータをpostに入れる


    #コメントフォームの部分
    if request.method =="POST": #フォームを送信したのかどうかのif文
        form = CommentForm(request.POST)
        
        if form.is_valid(): #送信したフォームが有効かどうかのif文
            comment = form.save(commit=False)
            comment.post = post #詳細ページのデータをcomment.postにいれる
            comment.save()

            return redirect("post_detail", slug=post.slug) #コメントを送信したときどこのページに行きたいのか（ここでは現在の詳細ページ（post_detail）に飛ぶ）

    else:#"POST"でなければ
        form = CommentForm() #コメントフォームをそのまま返す


    return render(request, "blog/post_detail.html", {"post": post, "form": form}) #それをリターンで返す














