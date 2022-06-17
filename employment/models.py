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
    user = models.ManyToManyField(User, verbose_name='지원자', blank=True)
    # User 모델과 JobPosting 모델은 M:N관계로 설정 / blank=True로 값이 없어도 가능하도록 설정
    position = models.CharField(max_length=100, verbose_name='채용포지션')
    compensation = models.PositiveIntegerField(default=1000000, verbose_name='채용보상금')
    content = models.TextField(verbose_name='채용내용')     # CharField 보다는 긴 내용을 작성하기 위해 TextField 설정
    stack = models.TextField(verbose_name='사용기술')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    def __str__(self):
        return f'{self.id}'


# 사용자가 지원한 채용공고 지원내역 모델
class ApplicationStatus(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='지원자', related_name='applicant', db_constraint=False)
    jobposting_status = models.ForeignKey(JobPosting, on_delete=models.CASCADE, verbose_name='채용공고', db_constraint=False)
    # User 및 JobPosting 모델과 각각 1:N관계로 설정