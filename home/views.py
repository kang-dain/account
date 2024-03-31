from django.shortcuts import render, redirect
from .forms import UserProfileForm

def home(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # 홈 페이지로 리디렉션
    else:
        form = UserProfileForm()
    return render(request, 'home.html', {'form': form})
