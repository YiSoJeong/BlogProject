from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from faker import Faker
from .form import BlogPost

def home(request):
    blogs = Blog.objects #퀴리셋
    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해준다.
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts':posts})

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

def faker(request):

    for i in range(5):
        myfake = Faker()

        blog = Blog()
        blog.title = myfake.name()
        blog.body = myfake.text()
        blog.pub_date = timezone.datetime.now()
        blog.save()
    return redirect('home')

def blogpost(request):
    # 1. 입력된 내용 처리 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

    # 2. 빈 페이지 띄우기 -> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})