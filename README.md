# 프리온보딩 백엔드 코스 선발 과제

## 📖 **Contents**
- [모델링 및 설정](#-모델링-및-설정) 
- [Setup 과정](#-setup-과정)
- [요구사항 및 구현 과정](#-요구사항-및-구현-과정)
  - [채용공고 전체 목록 조회 API](#-채용공고-전체-목록-조회-api)
  - [채용공고 전체 목록 조회 API에서 검색 기능 구현](#-채용공고-전체-목록-조회-api에서-검색-기능-구현)
  - [채용공고 등록 API](#-채용공고-등록-api)
  - [채용공고 상세 페이지 API 및 해당 회사의 다른 채용공고 확인 기능 구현](#-채용공고-상세-페이지-api-및-해당-회사의-다른-채용공고-확인-기능-구현)
  - [채용공고 수정 API](#-채용공고-수정-api)
  - [채용공고 삭제 API](#-채용공고-삭제-api)
  - [채용공고 지원 API](#-채용공고-지원-api)
- [Postman API 문서](#-postman-api-문서)


<br>

## 📌 모델링 및 설정 
- **wanted라는 이름의 프로젝트를 가상환경에서 시작하고 employment라는 이름의 App 생성 / RDBMS는 django 기본인 sqlite3로 활용**
<img width="1071" alt="image" src="https://user-images.githubusercontent.com/95380638/174308623-580d4861-cbeb-4920-80b2-55e33abd2654.png">

- **models.py에서 Company와 JobPosting이라는 이름으로 각각 회사와 채용공고에 해당하는 모델 생성, django 기본 모델인 User로 사용자 모델 대체. ApplicationStatus라는 모델로 채용공고 지원 내역 모델 생성**
  - Company 모델과 JobPosting 모델은 1:N 관계로 설정
  - User 모델과 JobPosting 모델은 M:N 관계로 설정
  - User 모델 및 JobPosting 모델은 ApplicationStatus 모델과 1:N관계 설정 

<img width="1426" alt="image" src="https://user-images.githubusercontent.com/95380638/174075590-d688f0bc-5054-4e76-b489-c46c8fdf5068.png">

- django 기본 어드민 페이지를 이용해서 DB 데이터 생성 진행

<br>

- **REST API 서버를 만들기 위해 DRF(Django REST Framework) 라이브러리 설치**

<br>

## 📌 Setup 과정 
```terminal
pip install -r requirements.txt
```
- 해당 명령어를 통해 requirements.txt 파일 안에 있는 패키지들을 설치

```terminal
pip list

Package             Version
------------------- -------
asgiref             3.5.2
Django              4.0.5
djangorestframework 3.13.1
pip                 22.1.2
pytz                2022.1
setuptools          62.3.2
sqlparse            0.4.2
```

- 이후에 pip list 명령어로 설치된 패키지 확인

<br>

## 📌 요구사항 및 구현 과정

### 📌 채용공고 전체 목록 조회 API
```python
[
	{
	  "채용공고_id": 채용공고_id,
	  "회사명":"원티드랩",
	  "국가":"한국",
	  "지역":"서울",
	  "채용포지션":"백엔드 주니어 개발자",
	  "채용보상금":1500000,
	  "사용기술":"Python"
	},
	{
	  "채용공고_id": 채용공고_id,
	  "회사명":"네이버",
	  "국가":"한국",
	  "지역":"판교",
	  "채용포지션":"Django 백엔드 개발자",
	  "채용보상금":1000000,
	  "사용기술":"Django"
	},
  ...
]
```
- **요구사항 : 채용공고 목록을 위와 같은 JSON 형태의 데이터로 확인할 수 있도록 설정**

- **구현 과정** 
<img width="876" alt="image" src="https://user-images.githubusercontent.com/95380638/174088914-ff7018e2-7ffe-4ea5-b5ec-7f01881df0f2.png">

- **employment App 내부에 serializers.py 파일을 생성하고 채용공고 전체 목록을 조회하기 위한 JobPostingModelSerializer를 생성** 
  - serializer 필드를 자동으로 설정해주는 ModelSerializer를 상속받아 진행
- models.py에 설정한 필드 이름이 아닌 한글명으로 사용하기 위해 Serializer 내부에 새로운 필드 설정
- 회사와 관련된 Serializer인 CompanySerializer도 생성해서 JobPostingModelSerializer 내부에 들어올 수 있게 to_representation 메서드 override 하기
  - 여기서 CompanySerializer 관련 데이터를 '채용회사'라는 이름으로 설정 

<img width="939" alt="image" src="https://user-images.githubusercontent.com/95380638/173994448-11707921-4008-4718-ab8a-9a4741c7fbd2.png">

- **그 다음, views.py에서 APIView를 상속받아 채용공고 전체 목록을 조회하는 JobPostingsAPIView 생성**
  - GET 방식일 때는 채용공고 전체 목록을 조회할 수 있도록 ORM 코드 작성
  - 단일 객체가 아닌 객체 목록을 serializer 하기 위해 JobPostingModelSerializer에 many=True 설정

- **urls.py에서 채용공고 전체 조회하기 위해 jobpostings/ 라는 URL 설정**

<br>

- **구현 결과**
<img width="1209" alt="image" src="https://user-images.githubusercontent.com/95380638/174089506-e773450e-8b36-4f59-a28f-224b53269d5f.png">

<br>

### 📌 채용공고 전체 목록 조회 API에서 검색 기능 구현
- **요구사항 : some/url?search=원티드 와 같이 Request URL에 ?search= 를 입력한 뒤 검색하고자 하는 키워드를 입력하고 요청하면 해당 내용이 JSON 형태의 데이터로 보여줄 수 있도록 설정**

- **구현 과정**
<img width="1099" alt="image" src="https://user-images.githubusercontent.com/95380638/173995537-f9cf778f-383d-4693-9cc0-cd662d01c10c.png">

- **views.py의 채용공고 전체 목록을 조회하는 JobPostingsAPIView에서 관련 코드 추가**
  - search라는 이름으로 검색 키워드가 입력되니까 search_keyword = request.GET.get('search') 코드로 입력된 키워드를 변수로 지정
  - 만약 해당 변수가 있다면, Q 객체로 검색된 키워드 search_keyword를 OR 조건으로 필터링
  - 회사 이름, 국가, 지역과 포지션, 보상금, 기술 필드에 다 OR 조건으로 걸리도록 설정

<br>

- **구현 결과**

<img width="1179" alt="image" src="https://user-images.githubusercontent.com/95380638/173995923-54604052-5ac7-4da3-a736-309b283de8fe.png">

<br>

### 📌 채용공고 등록 API
```python
{
  "회사_id":회사_id,
  "채용포지션":"백엔드 주니어 개발자",
  "채용보상금":1000000,
  "채용내용":"원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..",
  "사용기술":"Python"
}
```

- **요구사항 : 위와 같은 JSON 형태의 데이터를 입력했을 때 채용공고가 등록되도록 설정**

- **구현 과정**

<img width="563" alt="image" src="https://user-images.githubusercontent.com/95380638/173996890-b5278ef2-ff84-4ec1-838a-9d09a826a3af.png">

- **serializers.py에서 채용공고를 등록하기 위한 JobPostingCreateSerializer 생성**
  - 채용공고 전체 목록과는 다르게, content 필드인 채용내용 필드를 새롭게 추가 

<img width="802" alt="image" src="https://user-images.githubusercontent.com/95380638/173996368-a8fb3726-f3f5-4877-8f2b-e7c26cb91493.png">

- **views.py에 있는 JobPostingsAPIView를 이용해서 POST 방식일 경우 채용공고가 등록될 수 있도록 구현**
  - POST 방식으로 입력된 데이터를 serializer = JobPostingCreateSerializer(data=request.data) 이렇게 JobPostingCreateSerializer쪽으로 보내주기
  - serializer에서 데이터에 대한 유효성 검증 이후 통과되면 저장, 그리고 201번 코드를 응답
  - 만약 실패했다면 400번 코드로 예외처리 진행

<br>

- **구현 결과**

<img width="1185" alt="image" src="https://user-images.githubusercontent.com/95380638/173997252-198574f9-bad7-46b2-ba15-e80c89b12cf1.png">

<br>

### 📌 채용공고 상세 페이지 API 및 해당 회사의 다른 채용공고 확인 기능 구현
```python
{
  "채용공고_id": 채용공고_id,
  "회사명":"원티드랩",
  "국가":"한국",
  "지역":"서울",
  "채용포지션":"백엔드 주니어 개발자",
  "채용보상금":1500000,
  "사용기술":"Python",
  "채용내용": "원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..",
  "회사가올린다른채용공고":[채용공고_id, 채용공고_id, ..] # id List (선택사항 및 가산점요소).
}
```
- **요구사항 : 특정 채용공고에 대한 상세 페이지를 요청했을 때, 위와 같이 JSON 형태의 데이터를 확인할 수 있도록 설정 / 채용내용도 추가로 확인하도록 설정 / 해당 회사가 올린 다른 채용공고 id값도 확인할 수 있도록 설정**

- **구현 과정**
<img width="852" alt="image" src="https://user-images.githubusercontent.com/95380638/174306922-4d3c80ec-629f-4d49-9d42-018ba3aa7853.png">

<img width="714" alt="image" src="https://user-images.githubusercontent.com/95380638/174307080-1309cf31-d1fd-493f-95b0-821350eb4784.png">

- **serializers.py에서 채용공고 상세 페이지를 확인하기 위한 JobPostingDetailSerializer 생성**
  - 전체 목록과 다르게 content 필드인 채용내용 필드를 추가해서 확인할 수 있도록 설정
  - CompanySerializer가 JobPostingModelSerializer 내부에 들어올 수 있게 to_representation 메서드 override 하기
    - 여기서도 CompanySerializer 관련 데이터를 '채용회사'라는 이름으로 설정 

- **해당 회사가 올린 다른 채용공고 id값을 확인할 수 있도록 기존의 하나였던 CompanySerializer를 목록 조회 연결 CompanySerializer와 상세 조회 연결
CompanyDetailSerializer 이렇게 2개로 변경**
  - CompanyDetailSerializer에서는 models.py의 JobPosting 모델에서 정의한 Company 모델과의 related_name인 company_jobposting를 이용해서 역참조 진행
  - 채용공고 상세 조회 JobPostingDetailSerializer에서 Nested Serializer로 CompanyDetailSerializer 설정
  - **해당 회사의 id값과 1:N관계에 있는 JobPosting 객체들에게 역참조로 접근해서 요구사항인 리스트 형태가 아닌 QuerySet 형태로 구현하게됨**


<img width="685" alt="image" src="https://user-images.githubusercontent.com/95380638/173998221-cb7feb46-f093-4d65-ad06-dfea8c864fa2.png">

- **views.py에서는 채용공고 상세 조회를 위한 JobPostingAPIView를 APIView를 상속받아 생성**
  - GET 방식으로 요청이 올 때, 상세 pk를 받고 get_object_or_404 코드로 객체가 있으면 보여주고 없으면 404 예외처리 진행

- **urls.py에서는 jobpostings/<int:pk>/ 로 URL를 설정해서 채용공고 상세 조회 및 추후에 수정과 삭제시에도 pk를 받도록 설정**

<br>

- **구현 결과**
<img width="1207" alt="image" src="https://user-images.githubusercontent.com/95380638/174307298-2a33d90c-652a-4f05-a85f-86f8d446c2f1.png">

<br>

### 📌 채용공고 수정 API
- **요구사항 : 채용공고 상세 페이지에서 회사 ID를 제외한 다른 필드 값을 JSON 형태의 데이터로 수정할 수 있도록 설정**

- **구현 과정**

<img width="719" alt="image" src="https://user-images.githubusercontent.com/95380638/173998960-0e045687-9c2e-4a3d-b1f4-cdffd094904f.png">

- **serializers.py에서 채용공고 수정을 위한 JobPostingUpdateSerializer 생성**
  - 회사_id는 수정할 수 없도록 필드에 추가하지 않았음

<img width="668" alt="image" src="https://user-images.githubusercontent.com/95380638/173999251-f4b2a9c5-2740-4e44-beda-de9e3450bfd4.png">

- **views.py에서는 기존의 상세 조회 JobPostingAPIView에서 PUT 방식으로 요청이 올 때 채용공고를 수정할 수 있도록 설정**
  - PUT 방식의 요청일 때, 채용공고 pk를 받아서 get_object_or_404로 모델 객체가 있으면 보여주고 없으면 404 예외처리
  - 받은 데이터를 JobPostingUpdateSerializer에 보내주고 유효성 검사 진행
  - 성공하면 데이터를 저장하고, 실패하면 400번 예외처리 하게끔 설정

<br>

- **구현 결과**

<img width="1199" alt="image" src="https://user-images.githubusercontent.com/95380638/173999691-8ae7ac12-24c2-4b24-891e-5d2bd94b5b06.png">


<br>

### 📌 채용공고 삭제 API
- **요구사항 : 특정 채용공고를 삭제할 수 있도록 설정**

- **구현 과정**

<img width="672" alt="image" src="https://user-images.githubusercontent.com/95380638/174000241-59951fe1-8f5d-41ee-a3ed-1c730363e4a4.png">

- **views.py에서는 채용공고 상세 조회를 하는 JobPostingAPIView에서 DELETE 방식으로 요청이 왔을 때 채용공고를 삭제할 수 있도록 설정**
  - DELETE 방식일 때 채용공고 pk를 받고 get_object_or_404로 모델 데이터가 있으면 가져오고 없으면 404 예외처리
  - 해당 객체를 jobposting.delete() 이렇게 삭제시키기
  - 삭제 이후 204코드 응답

<br>

- **구현 결과**

<img width="1214" alt="image" src="https://user-images.githubusercontent.com/95380638/174000719-40c49624-dbdf-4b1d-b21a-72afb4094dde.png">

<br>

### 📌 채용공고 지원 API
- **요구사항 : 사용자가 원하는 특정 채용공고에 지원하는 JSON 형태의 id 값을 넣으면 채용공고 id와 사용자 id값을 함께 볼 수 있도록 설정**

- **구현 과정**

<img width="1018" alt="image" src="https://user-images.githubusercontent.com/95380638/174072486-2186a43d-616f-42c6-b1f2-388b5242843d.png">
 
- **models.py에서 ApplicationStatus라는 채용공고 지원 내역을 볼 수 있는 모델 생성**
  - 먼저 기존의 JobPosting 모델에 user 필드를 생성하고 ManyToManyField 필드로 M:N 관계 설정 
    - 1명의 사용자는 여러개의 채용공고에 지원할 수 있고, 1개의 채용공고는 여러명이 지원할 수 있기 때문
  - 그리고 ApplicationStatus라는 모델을 생성해서 User 모델과 JobPosting 모델 각각 1:N관계 설정
    - 이렇게 설정해서 해당 모델에는 User 모델 id 값과 JobPosting id 값을 볼 수 있도록 하기

<img width="580" alt="image" src="https://user-images.githubusercontent.com/95380638/174073337-8e14cf29-cee5-4504-b9da-2ce0e1e176b9.png">

- **serializers.py에서는 사용자가 채용공고 현황을 조회할 수 있는 UserApplySerializer를 생성하고 채용공고에 지원할 수 있는 UserApplyCreateSerializer 생성**
  - 둘 다 ApplicationStatus 모델을 설정하고 채용공고 id 값과 사용자 id 값을 볼 수 있도록 설정

<img width="921" alt="image" src="https://user-images.githubusercontent.com/95380638/174073784-f55e3797-620d-4baf-a3f6-0bab48056e16.png">

- **views.py에서는 사용자가 채용공고 현황을 보고 지원할 수 있는 UserApplyAPIView 생성**
  - GET 방식에서는 사용자가 로그인 되었을 때, 로그인된 사용자의 id로 필터링해서 모델 데이터 보여주기
  - POST 방식에서는 입력된 JSON 데이터를 UserApplyCreateSerializer에 보내고 유효성 검사 진행

- **urls.py에서는 jobpostings/user/ 라는 URL로 설정**

<br>

- **구현 결과**

<img width="1234" alt="image" src="https://user-images.githubusercontent.com/95380638/174074526-51c08194-0911-40c4-aa24-b29c19fca148.png">

- **로그인 시, 채용공고 지원 현황 보여주기**

<img width="1217" alt="image" src="https://user-images.githubusercontent.com/95380638/174074787-c4a6771b-6932-4263-b0db-4ebb0601562b.png">

- **JSON 데이터로 입력하면 채용공고 지원하기**

<br>

## 📌 Postman API 문서
- [Postman API 문서](https://documenter.getpostman.com/view/20920872/UzBjtU4c)

- **Postman API 문서 예시**
<img width="1434" alt="image" src="https://user-images.githubusercontent.com/95380638/174248014-cf726f11-8207-4352-874b-02cb76d52b22.png">

- **Postman을 사용해서 실제 클라이언트 입장에서 API가 작동하는지 검토**
- jobpostings - Apply/List는 로그인 정보가 필요



