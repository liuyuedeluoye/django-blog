from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('post/<int:pk>/',views.post_detail,name = 'post_detail'),
    path('register/', views.register, name='register'),
    path('post/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorites, name='favorites'),

    # Django 内置登录视图
    # template_name：指定使用哪个模板
    path('login/', auth_views.LoginView.as_view(
        template_name='blog/login.html',
        redirect_authenticated_user=True  # 已登录用户访问 login 直接跳转
    ), name='login'),

    # Django 内置登出视图
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]