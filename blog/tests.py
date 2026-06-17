# 在 Django Shell 中逐行输入
from blog.models import Category,Post
# 首先测试分类功能
category_django = Category.objects.create(category_name = 'django',slug = 'django')
category_css = Category.objects.create(category_name = 'css',slug = 'css')
category_python =  Category.objects.create(category_name = 'python' , slug = 'python')

# 接着测试内容，测试用例为每个分类下有两篇文章
Post.objects.create(
    category = category_django,
    title = "这是一个django标题内容",
    abstract = "这是一个django摘要内容",
    content = "这是一个django正文内容",
    slug = "这是一个django_url内容"
)
Post.objects.create(
    category = category_css,
    title = "这是一个css标题内容",
    abstract = "这是一个css摘要内容",
    content = "这是一个css正文内容",
    slug = "这是一个css_url内容"
)
Post.objects.create(
    category = category_python,
    title = "这是一个python标题内容",
    abstract = "这是一个python摘要内容",
    content = "这是一个python正文内容",
    slug = "这是一个python_url内容"
)

# 3. 验证查询
print(Post.objects.all())           # 输出所有文章
print(Post.objects.count())         # 文章总数
print(Post.objects.filter(category= category_django))  # Django 分类下的文章
print(Post.objects.filter(category= category_css))
print(Post.objects.filter(category= category_python))