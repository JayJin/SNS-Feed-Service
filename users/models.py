from django.db import models

# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = "user_list"

    email = models.CharField(max_length=32, null=False)         # 올바른 구조인지 검증 필요
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
                                                                # 다른 개인정보와 유사할 수 없음, 최소 10자이상, 숫자로만 사용 불가, 숫자 문자 특수문자 2가지 이상 포함,
                                                                # 이전 비밀번호와 동일하게 설정할 수 없음, 3회이상 연속되는 문자 사용 불가 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)