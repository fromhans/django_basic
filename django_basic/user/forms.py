from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    repassword = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'

    )

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')
        if password and repassword:
            if password != repassword:
                self.add_error('password', '비밀번호가 다릅니다')
                self.add_error('repassword', '비밀번호가 다릅니다')


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일를 입력해주세요.'
        },
        label="이메일",
        max_length=64
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="비밀번호",
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        }
    )

    # 기본적으로는 is_valid 를 통해 값이 들어있는지 아닌지가 검사되고 있으나,
    # 추가적으로 forms 안의 clean 함수를 상속하고 재정의하여 유효성 검사를 수행해준다.
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error('email', '아이디가 없습니다')
                return

            if not check_password(password, user.password):
                self.add_error('password', "비밀번호가 틀렸습니다")
            else:
                self.email = user.email
