from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from  django.contrib.auth.models import User
from . models import Comment, Post, Category

# Create your views here.
def blog(request):
    cat = Category.objects.all()
    posts = Post.objects.filter(is_published=True).order_by('posted')
    r_posts = Post.objects.filter(is_published=True).order_by('posted')[0:3]
    #paginator
    posts= Paginator(posts,5)
    page = request.GET.get('page')
    posts = posts.get_page(page)
    
    return render(request,'blog/blog.html',{'posts': posts, 'cat': cat , 'r_posts':r_posts})

def post(request,title):
    
    cat = Category.objects.all()
    recent_posts = Post.objects.filter(is_published=True).order_by('posted')[0:3]
    post = Post.objects.get(title=title)
    related_posts = Post.objects.filter(category=post.category)
    comments = Comment.objects.filter(post=post)
    return render(request,'blog/post.html',{'post': post, 'cat': cat , 'comments': comments,'recent_posts': recent_posts, 'related_posts' : related_posts})    


def post_comment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        webpage = request.POST.get('url')
        post_id = request.POST.get('id')


        usernamef = User.objects.get(first_name=name)
        print(usernamef)

 
        post = Post.objects.get(id=post_id)
        c= Comment(name=usernamef.first_name,email=email,comments=comment,weburl=webpage,post= post)
        c.save()
            
        
        return redirect ('post',title=post.title)
    return redirect('home')    

def search_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        posts = Post.objects.filter(description__icontains=search)
        posts= Post.objects.filter(title__icontains=search)
        cat = Category.objects.all()
        
        r_posts = Post.objects.filter(is_published=True).order_by('posted')[0:3]



    return render(request,'blog/blog.html',{'posts': posts, 'cat': cat , 'r_posts':r_posts})


def get_category(request,cat): 

     
    
    
    categories = Category.objects.all()
    cate = Category.objects.get(name=cat)
    
    posts = Post.objects.filter(category=cate)
   
        
    r_posts = Post.objects.filter(is_published=True).order_by('posted')[0:3]



    return render(request,'blog/blog.html',{'posts': posts, 'cat': categories , 'r_posts':r_posts})
   


       