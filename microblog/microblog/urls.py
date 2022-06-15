
from django.contrib import admin
from django.urls import path

from blog.views import frontpage #blogフォルダの中のviewsファイルの中にfrontpageが書いてありますよ

urlpatterns = [
    path('admin/', admin.site.urls), #データベースを扱ううえでの管理画面にアクセスする
    path("", frontpage) #何のpathも指定しない時はフロントページに飛ぶ
]
