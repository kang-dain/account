from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('signup.urls')),  # signup 앱 URL 포함
    path('main/', include('main.urls')),  # main 앱 URL 포함
    path('login/', include('login.urls')),  # login 앱 URL 포함
    path('home/', include('home.urls')),  # home 앱 URL 포함
    path('guestbook/', include('guestbook.urls')),  # guestbook 앱 URL 포함
    path('todo/', include('todo.urls')),
    path('post/', include('post.urls', namespace='post')),
    path('', include('home.urls')),  # 기본 URL을 home 앱으로 설정
]
