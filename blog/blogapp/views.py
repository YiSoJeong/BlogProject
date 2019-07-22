from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects #퀴리셋
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details': details})

def new(request): # new.html 띄워줌
    return render(request, 'new.html')

def create(request): #입력받은 내용 > 디비에 넣어줌
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # 객체를 디비에 저장 객체.delete는 반대
    return redirect('/blog/'+str(blog.id))