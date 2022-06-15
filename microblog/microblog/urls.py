
from django.contrib import admin
from django.urls import path

from blog.views import frontpage, post_detail #blogフォルダの中のviewsファイルの中にfrontpageが書いてありますよ

urlpatterns = [
    path('admin/', admin.site.urls), #データベースを扱ううえでの管理画面にアクセスする
    path("", frontpage), #何のpathも指定しない時はフロントページに飛ぶ
    path("<slug:slug>/", post_detail, name="post_detail") #slugはurlに指定することのできる文字列（modelsで定義している）
]
