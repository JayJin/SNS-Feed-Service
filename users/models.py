from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):

        if not email:
            raise ValueError('이메일 작성해주세요.')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None):

        user = self.create_user(
            email,
            password=password,
            nickname=nickname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class UserModel(models.Model):
    class Meta:
        db_table = "user_list"

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        error_messages={'unique': "이미 존재하는 이메일 주소입니다."}   
    )         # 올바른 구조인지 검증 필요
    password = models.CharField(max_length=256, null=False)
                                                                # 다른 개인정보와 유사할 수 없음, 최소 10자이상, 숫자로만 사용 불가, 숫자 문자 특수문자 2가지 이상 포함,
                                                                # 이전 비밀번호와 동일하게 설정할 수 없음, 3회이상 연속되는 문자 사용 불가 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

