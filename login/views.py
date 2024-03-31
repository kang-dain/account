from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import User

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()
            if user:
                # 로그인 성공
                # 세션 등록 등 로그인 처리 작업 수행
                return redirect('home')
            else:
                # 로그인 실패 처리
                error_message = "회원가입된 정보 없음"
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
