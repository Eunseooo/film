"""BlogProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from blogApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls), # 원래 있던 거
    path('', mainpage, name="mainpage"), # main page
    path('community/', main, name="main"), # community
    path('myPage/', mypage, name="mypage"),
    path('cameraTest/', cameraTest, name="cameraTest"),
    path('detail/<int:id>/', detail, name="detail"),  # detail 페이지
    path('create_page/', create_page, name="create_page"), # 글 작성
    path('create/', create, name= 'create'), # 글 작성 
    path('update/<int:id>/', update, name= "update"), # 글 수정
    path('update_page/<int:id>/', update_page, name= "update_page"), # 글 수정
    path('delete/<int:id>/', delete, name= "delete"), # 글 삭제 
    path('detail/<int:id>/comments/create/', create_comment, name= "create_comment"), # 댓글 작성
    path('detail/<int:id>/comments/delete/<int:comment_id>', delete_comment, name= "delete_comment"), # 댓글 삭제 
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 