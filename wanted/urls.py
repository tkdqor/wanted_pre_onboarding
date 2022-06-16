"""wanted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employment.views import JobPostingsAPIView, JobPostingAPIView, UserApplyAPIView



urlpatterns = [
    # 어드민 페이지 URL
    path('admin/', admin.site.urls),

    # 채용공고 전체 조회 URL
    path('jobpostings/', JobPostingsAPIView.as_view()),

    # 채용공고 상세 조회 URL
    path('jobpostings/<int:pk>/', JobPostingAPIView.as_view()),

    # 사용자 채용공고 현황 URL
    path('jobpostings/user/', UserApplyAPIView.as_view()),
]

