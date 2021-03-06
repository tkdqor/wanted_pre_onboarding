from django.shortcuts import get_object_or_404     # 모델 객체가 없으면 404에러 발생시키기 위함
from rest_framework.response import Response
from .models import Company, JobPosting, ApplicationStatus
from .serializers import JobPostingModelSerializer, JobPostingDetailSerializer, \
JobPostingCreateSerializer, JobPostingUpdateSerializer, UserApplySerializer, UserApplyCreateSerializer 
# serializers.py에서 정의한 Serializer 클래스 import
from rest_framework import status
from rest_framework.views import APIView           # APIView를 이용해서 View 구성하기
from django.db.models import Q                     # 검색 기능을 위해 Q 객체 import



# 채용공고 전체 목록 조회 View - 채용공고 등록 View
class JobPostingsAPIView(APIView):
    # GET 방식일 때는 채용공고 전체 목록 조회
    def get(self, request):
        jobpostings = JobPosting.objects.all()
        serializer = JobPostingModelSerializer(jobpostings, many=True) # 단일 객체가 아닌 객체 목록을 serializer 하기 위해 many=True 설정

        # 채용공고 검색 기능
        search_keyword = request.GET.get('search')
        if search_keyword:
            # Q 객체로 검색된 키워드 search_keyword를 OR 조건으로 필터링 해주기
            jobpostings = JobPosting.objects.filter(Q(company__name__icontains=search_keyword) | Q(company__country__icontains=search_keyword) |
            Q(company__region__icontains=search_keyword) | Q(position__icontains=search_keyword) | Q(compensation__icontains=search_keyword) | 
            Q(stack__icontains=search_keyword))
            serializer = JobPostingModelSerializer(jobpostings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    # POST 방식일 때는 채용공고 등록
    def post(self, request):
        serializer = JobPostingCreateSerializer(data=request.data)  # 입력된 data 보내기
        if serializer.is_valid():                            # 유효성 검증 후 통과하면 저장
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 검증되지 않는 경우 400 예외처리



# 채용공고 상세 조회 View - 채용공고 수정 View - 채용공고 삭제 View
class JobPostingAPIView(APIView):
    # GET 방식일 떄는 채용공고 상세 조회
    def get(self, request, pk):
        jobposting = get_object_or_404(JobPosting, id=pk)    # 모델 객체가 없으면 404 예외처리
        serializer = JobPostingDetailSerializer(jobposting)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # PUT 방식일 때는 채용공고 수정
    def put(self, request, pk):
        jobposting = get_object_or_404(JobPosting, id=pk)
        serializer = JobPostingUpdateSerializer(jobposting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE 방식일 때는 채용공고 삭제
    def delete(self, request, pk):
        jobposting = get_object_or_404(JobPosting, id=pk)
        jobposting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


# 사용자 채용공고 현황 및 지원 View
class UserApplyAPIView(APIView):
    # GET 방식일 떄는 채용공고 지원 현황 보여주기
    def get(self, request):
        # 사용자가 로그인 되었을 경우에만 해당 API 데이터 보여주기
        if request.user.is_authenticated:
            applicant = request.user
            applicationStatus = ApplicationStatus.objects.filter(applicant_id=applicant.id) # 로그인된 사용자의 id로 필터링하기
            serializer = UserApplySerializer(applicationStatus, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)    
    
    # POST 방식일 떄는 채용공고 지원 기능 구현
    def post(self, request):
        serializer = UserApplyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
