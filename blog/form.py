from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    # 手动设置email里的东西
    email = forms.EmailField(
        label= "邮箱",
        required=True,
    )

    class Meta:
        model = User
        fields = ['email','username','password1','password2']
        labels = {
            'username' : '用户名',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['password1']       # ← 'password1' 是字典的 key
        self.fields['password1'].label = '输入密码'
        self.fields['password2'].label = '确认密码'
        self.fields['password1'].help_text = ''      # 清掉密码英文提示
        self.fields['username'].help_text = ''       # 清掉用户名英文提示
        self.fields['password2'].help_text = ''      # 清掉确认密码英文提示