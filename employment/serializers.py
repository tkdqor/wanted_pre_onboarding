from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Company, JobPosting, ApplicationStatus



# 채용공고 전체 목록 조회 Serializer
class JobPostingModelSerializer(serializers.ModelSerializer):
    # model에 정의한 필드 이름을 한글화 
    채용공고_id = serializers.IntegerField(source='id') 
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='compensation') 
    사용기술 = serializers.CharField(source='stack') 

    class Meta: 
        model = JobPosting
        fields = ('채용공고_id', 'company', '채용포지션', '채용보상금', '사용기술')
        depth = 1  # Company 모델과 JobPosting 모델이 1:N관계이므로 관련된 Company 모델 데이터 보여주기 


# 채용공고 상세 조회 Serializer
class JobPostingDetailSerializer(serializers.ModelSerializer):
    # model에 정의한 필드 이름을 한글화 
    채용공고_id = serializers.IntegerField(source='id') 
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='compensation') 
    사용기술 = serializers.CharField(source='stack') 
    채용내용 = serializers.CharField(source='content') # 전체 목록과 다르게 채용내용 필드 추가

    class Meta:
        model = JobPosting
        fields = ('채용공고_id', 'company', '채용포지션', '채용보상금', '사용기술', '채용내용')
        depth = 1  # Company 모델과 JobPosting 모델이 1:N관계이므로 관련된 Company 모델 데이터 보여주기 


# 채용공고 등록 Serializer
class JobPostingCreateSerializer(serializers.ModelSerializer):
    # model에 정의한 필드 이름을 한글화 
    회사_id = serializers.IntegerField(source='company_id') 
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='compensation') 
    채용내용 = serializers.CharField(source='content')
    사용기술 = serializers.CharField(source='stack')  

    class Meta:
        model = JobPosting
        fields = ('회사_id', '채용포지션', '채용보상금', '채용내용', '사용기술')


# 채용공고 수정 Serializer
class JobPostingUpdateSerializer(serializers.ModelSerializer):
    # model에 정의한 필드 이름을 한글화 
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='compensation') 
    채용내용 = serializers.CharField(source='content')
    사용기술 = serializers.CharField(source='stack') 

    class Meta:
        model = JobPosting
        fields = ('채용포지션', '채용보상금', '채용내용', '사용기술')  # 회사_id는 수정하지 않도록 필드에 추가 X


# 사용자 채용공고 현황 Serializer
class UserApplySerializer(serializers.ModelSerializer):
    # model에 정의한 필드 이름을 한글화 
    채용공고_id = serializers.IntegerField(source='jobposting_status_id')
    사용자_id = serializers.IntegerField(source='applicant_id') 

    class Meta:
        model = ApplicationStatus
        fields = ('채용공고_id', '사용자_id')


# 사용자 채용공고 지원 Serializer
class UserApplyCreateSerializer(serializers.ModelSerializer):
    # model에 정의한 필드 이름을 한글화 
    채용공고_id = serializers.IntegerField(source='jobposting_status_id')
    사용자_id = serializers.IntegerField(source='applicant_id') 

    class Meta:
        model = ApplicationStatus
        fields = ('채용공고_id', '사용자_id')



