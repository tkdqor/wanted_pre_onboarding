from django.db import models
from django.contrib.auth.models import User

# 사용자에 해당하는 모델은 django에 내장되어있는 User 모델로 대체


# 회사에 해당하는 Company 모델
class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='회사명')
    country = models.CharField(max_length=50, verbose_name='국가')
    region = models.CharField(max_length=50, verbose_name='지역')

    def __str__(self):
        return f'{self.name}'



# 채용공고에 해당하는 JobPosting 모델
class JobPosting(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_jobposting', verbose_name='회사_id', default=1)
    # Company 모델과 JobPosting 모델은 1:N관계로 설정 / Company 모델 데이터 삭제 시, 같이 삭제되도록 CASCADE 설정
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='company_user', verbose_name='지원자', null=True, blank=True)
    # User 모델과 JobPosting 모델은 1:1관계로 설정 / User 모델 데이터 삭제 시, JobPosting 모델의 데이터는 삭제되지 않도록 PROTECT 설정
    position = models.CharField(max_length=100, verbose_name='채용포지션')
    compensation = models.PositiveIntegerField(default=1000000, verbose_name='채용보상금')
    content = models.TextField(verbose_name='채용내용')     # CharField 보다는 긴 내용을 작성하기 위해 TextField 설정
    stack = models.TextField(verbose_name='사용기술')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
