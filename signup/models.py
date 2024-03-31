from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # AbstractUser를 상속하고 USERNAME_FIELD를 설정합니다.
    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS에서 'email'을 제거합니다.
    REQUIRED_FIELDS = ['user_name', 'major', 'nickname', 'phone_number']

    # 'email' 필드에 대해 중복 값을 허용하지 않도록 설정합니다.
    email = models.EmailField(unique=True)

    # 추가로 필요한 필드를 여기에 정의합니다.
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
