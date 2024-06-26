from django.urls import path
from .views import guestbook, write, delete, deleteform

app_name = 'guestbook'

urlpatterns = [
    path('', guestbook, name='guestbook'),  # 방명록 목록
    path('write/', write, name='write'),  # 방명록 작성
    path('delete/', delete, name='delete'),  # 방명록 삭제
    path('deleteform/<int:id>/', deleteform, name='deleteform'),  # 삭제 폼
]
