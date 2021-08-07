from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog ,Comment
from django.utils import timezone
# Create your views here.

# main 페이지 만들기임
def mainpage(request):
    return render(request,'main.html')

def mypage(request):
    return render(request,'myPage.html')

def cameraTest(request):
    return render(request,'cameraTest.html')

def main(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request,'community.html',context)

# detail 페이지 만들기    title 이런게 나옴
def detail(request,id):
    detail_data = get_object_or_404(Blog,pk=id)
    comments = Comment.objects.filter(blog_id = id)
    context= {
        'title' : detail_data.title,
        'writer' : detail_data.writer,
        'pub_date' : detail_data.pub_date,
        'body' : detail_data.body,
        'id' : id,
        'comments' : comments,
        'image' : detail_data.image
    }

    return render(request,'community_detail.html',context)

# 기본 create 페이지 
def create_page(request):
    return render(request,'community_create.html')

# create 를 작성하는 함수
def create(request):
    new_data = Blog()
    new_data.title = request.POST['title']
    new_data.writer = request.POST['writer']
    new_data.body = request.POST['body']
    new_data.image = request.FILES['image']
    new_data.pub_date= timezone.now()
    new_data.save()
    return redirect('main')

# update 함수

def update_page(request,id):
    update_page = get_object_or_404(Blog,pk=id)
    context= {
        'id' : id,
        'title' : update_page.title ,
        'writer' : update_page.writer ,
        'body' : update_page.body ,
        'pub_date' : update_page.pub_date,
        'image' : update_page.image 
    }
    return render(request,'community_update.html',context)

def update(request,id):
    update_data = get_object_or_404(Blog,pk=id)
    update_data.title = request.POST['title']
    update_data.writer = request.POST['writer']
    update_data.body = request.POST['body']
    update_data.image = request.FILES['image']
    update_data.pub_date = timezone.now()
    update_data.save()
    return redirect('main')


# 삭제 하는 함수 

def delete(request,id):
    delete_data= get_object_or_404(Blog,pk=id)
    delete_data.delete()
    return redirect('main')


# comment 생성

def create_comment(request,id):
    new_comment = Comment()
    blog_id = Blog.objects.get(pk=id)
    new_comment.blog_id = blog_id
    new_comment.user = request.POST['user']
    new_comment.content = request.POST['content']
    new_comment.date = timezone.now()
    new_comment.save()
    return redirect('detail', id)


# 댓글 삭제

def delete_comment(request,id,comment_id):
    comment= get_object_or_404(Comment,pk= comment_id)
    comment.delete()

    return redirect('detail', id)
    