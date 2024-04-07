from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    # 현재 로그인한 사용자 정보 가져오기
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('main')
