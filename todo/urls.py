from django.urls import path
from .views import todo_list, todo_detail, todo_post, todo_edit, todo_done, todo_done_list

app_name = 'todo'  # 네임스페이스 설정

urlpatterns = [
    path('', todo_list, name='todo_list'),  # 할 일 목록
    path('<int:pk>/', todo_detail, name='todo_detail'),  # 할 일 세부 정보
    path('post/', todo_post, name='todo_post'),  # 새 할 일 작성
    path('<int:pk>/edit/', todo_edit, name='todo_edit'),  # 할 일 수정
    path('done/', todo_done_list, name='todo_done_list'),  # 완료된 할 일 목록
    path('done/<int:pk>/', todo_done, name='todo_done'),  # 할 일을 완료 상태로 설정
]
