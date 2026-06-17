from django.db import models
from django.urls import reverse
# Create your models here.
# 文件路径：blog/models.py 的 Post 类中添加
from django.contrib.auth.models import User

# 分类 model，需要两个属性，一个属性是分类名称，一个属性是url，其中并且要求返回分类名字吧应该
class Category(models.Model):
    category_name = models.CharField("分类",max_length= 50,unique = True)
    slug = models.SlugField("URL标识" , max_length= 50,unique = True)

    def __str__(self):
        return self.category_name
    
# Post 文章列表，需要的属性是文章的标题、摘要、内容、文章的创建时间，并且需要一个外键绑定到目录上
# 并且外键关系是一个目录对应多个文章，谁是多，外键放在谁那里
class Post(models.Model):
    # 标题也应该是唯一
    title = models.CharField('文章标题',max_length = 50,unique = True)
    # blank=True表示即使文章的摘要不可也是可以过的
    abstract = models.TextField('摘要',blank=True)
    content = models.TextField("正文") 
    slug = models.SlugField("url标识",max_length = 50, unique = True)

    category = models.ForeignKey(
        # category才是反向查询真正的通道
        Category,
        models.CASCADE,
        # # 反向查询：category.posts.all()
        # 没写related_name 时，从分类查文章：category.article_set.all()    # 模型名小写 + _set，Django 自动生成
        # 写了之后，就可以用你起的名字：
        # category.posts.all()          # 干净直观
        # related_name 只是起到了一个名字，方便去反向查询
        related_name="posts",
        verbose_name = "分类",
    )
        # auto_now_add：创建时自动填入当前时间
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    # auto_now：每次保存时自动更新为当前时间
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        # 默认按创建时间倒序排列
        ordering = ['-created_at']

    def __str__(self):
        # 在 Admin 后台和 Shell 中显示对象时，显示标题
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk})
    
    # 文章应该有收藏，一个用户可以有多个收藏的文章，一个文章又可以被多个用户收藏，
    # 因此数据库关系多对多，应该使用ManyToManyField
    favourites = models.ManyToManyField(
        User,
        related_name  = "favourite_posts",
        # 允许为空
        blank=True,
        verbose_name='收藏者'
    )