from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Post
from django.db.models import Q
from .form import RegisterForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # 获取？后的category_slug
    category_slug = request.GET.get('category','')
    # 或缺？后的关键字
    keyword = request.GET.get('q','')
    # print(f'分类：{category_slug},关键字:{keyword}')
    posts = Post.objects.all().order_by('-created_at')
    if category_slug:
        posts = posts.filter(category__slug = category_slug)
    # 在标题和摘要里面匹配关键词
    if keyword:
        posts = posts.filter(
            Q(title__icontains = keyword) | Q(abstract__icontains = keyword)
        )
# 返回一个分类用于展示
    categories =Category.objects.all()
    return render(
        request,
        'blog/index.html',
        {
            "posts":posts,
            "categories":categories,
            'category_slug': category_slug,   # 传给模板，用于高亮当前选中
            'keyword': keyword,               # 回显搜索关键词
            'title': '小帅 博客 - 首页',
        }
    )

def post_detail(request,pk):
    post = get_object_or_404(Post, pk = pk)
    context = {
        "post" :post,
        "title" : f'{post.title} -- 博客'
    }
    return render(
        request,
        'blog/post_detail.html',
        context,
    )
def register(request):
    # 首先判断用户是否登陆，如果登陆直接返回首页user.is_authenticated
    if request.user.is_authenticated:
        return redirect('index')
    # 其次先判断表单提交是否是post，再判断表单是否存在,is_valid
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,f'欢迎登陆！{user.username}')
            return redirect('index')
    else:
        # GET 请求：显示空白注册表单
        form = RegisterForm()
    return render(request, 'blog/register.html', {
        'form': form,
        'title': '注册 - 小帅 博客'
    })

# login_required 装饰器：未登录用户访问此视图时，自动跳转到登录页
@login_required
def toggle_favorite(request,pk):
    post = get_object_or_404(Post, pk = pk)
    # 如果帖子已经被收藏了，那么就可以取消收藏
    if post.favourites.filter(id = request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)
# 文件路径：blog/views.py 新增
@login_required
def favorites(request):
    """当前用户的收藏列表"""
    # 通过 related_name 反向查询用户的收藏文章
    posts = request.user.favourite_posts.all().order_by('-created_at')
    return render(request, 'blog/favorites.html', {
        'posts': posts,
        'title': '我的收藏 - RUNOOB 博客'
    })