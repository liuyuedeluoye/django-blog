# 文件路径：blog/admin.py
from django.contrib import admin
from .models import Category,Post
from django_summernote.admin import SummernoteModelAdmin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name","slug"]

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ['title','category','created_at','updated_at']

    list_filter = ['category','created_at']

    search_fields = ['title','abstract']

    summernote_fields = ['content']

    date_hierarchy = 'created_at'
# list_per_page: Literal[20]表示， list_per_page 的类型是整数，默认值是 20（每页显示 20 条）。 
    list_per_page = 20
