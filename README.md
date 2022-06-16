# 프리온보딩 백엔드 코스 선발 과제

<br>

## 요구사항 및 구현 과정

### 📌 초기 모델링 및 설정 
- **wanted라는 이름의 프로젝트를 가상환경에서 시작하고 employment라는 이름의 App 생성 / RDBMS는 django 기본인 sqlite3로 활용**
<img width="1056" alt="image" src="https://user-images.githubusercontent.com/95380638/173993193-3640c348-ce18-46ec-a208-6622c9d62240.png">

- **models.py에서 Company와 JobPosting이라는 이름으로 각각 회사와 채용공고에 해당하는 모델 생성, django 기본 모델인 User로 사용자 모델 대체**
  - Company 모델과 JobPosting 모델은 1:N관계로 설정
  - User 모델과 JobPosting 모델은 1:1관계로 설정

<img width="1423" alt="image" src="https://user-images.githubusercontent.com/95380638/173993344-cd0b3a07-c83c-4a76-9b16-eb0d475337d6.png">

- django 기본 어드민 페이지를 이용해서 DB 데이터 생성 진행

<br>

- **REST API 서버를 만들기 위해 DRF(Django REST Framework) 라이브러리 설치**

<br>

### 📌 Setup 과정 
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

### 📌 (1) 채용공고 전체 목록 조회 API
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
<img width="712" alt="image" src="https://user-images.githubusercontent.com/95380638/173993698-595b580a-25e2-4462-8f04-2cfe4833a5fd.png">

- **employment App 내부에 serializers.py 파일을 생성하고 채용공고 전체 목록을 조회하기 위한 JobPostingModelSerializer를 생성** 
  - serializer 필드를 자동으로 설정해주는 ModelSerializer를 상속받아 진행
- models.py에 설정한 필드 이름이 아닌 한글명으로 사용하기 위해 Serializer 내부에 새로운 필드 설정
- depth = 1 코드를 추가해서 Company 모델과 JobPosting 모델이 1:N관계이므로 관련된 Company 모델 데이터 보여주기

<img width="939" alt="image" src="https://user-images.githubusercontent.com/95380638/173994448-11707921-4008-4718-ab8a-9a4741c7fbd2.png">

- **그 다음, views.py에서 APIView를 상속받아 채용공고 전체 목록을 조회하는 JobPostingsAPIView 생성**
  - GET 방식일 때는 채용공고 전체 목록을 조회할 수 있도록 ORM 코드 작성
  - 단일 객체가 아닌 객체 목록을 serializer 하기 위해 JobPostingModelSerializer에 many=True 설정

- **urls.py에서 채용공고 전체 조회하기 위해 jobpostings/ 라는 URL 설정**

- **구현 결과**

<img width="1176" alt="image" src="https://user-images.githubusercontent.com/95380638/173994953-75b3cb7a-bbc8-4ce2-b880-485f34df7f8a.png">

<br>

### 📌 (2) 채용공고 전체 목록 조회 API에서 검색 기능 구현
- **요구사항 : some/url?search=원티드 와 같이 Request URL에 ?search= 를 입력한 뒤 검색하고자 하는 키워드를 입력하고 요청하면 해당 내용이 JSON 형태의 데이터로 보여줄 수 있도록 설정**

- **구현 과정**
<img width="1099" alt="image" src="https://user-images.githubusercontent.com/95380638/173995537-f9cf778f-383d-4693-9cc0-cd662d01c10c.png">

- **views.py의 채용공고 전체 목록을 조회하는 JobPostingsAPIView에서 관련 코드 추가**
  - search라는 이름으로 검색 키워드가 입력되니까 search_keyword = request.GET.get('search') 코드로 입력된 키워드를 변수로 지정
  - 만약 해당 변수가 있다면, Q 객체로 검색된 키워드 search_keyword를 OR 조건으로 필터링
  - 회사 이름, 국가, 지역과 포지션, 보상금, 기술 필드에 다 OR 조건으로 걸리도록 설정

- **구현 결과**

<img width="1179" alt="image" src="https://user-images.githubusercontent.com/95380638/173995923-54604052-5ac7-4da3-a736-309b283de8fe.png">

<br>

### 📌 (3) 채용공고 등록 API
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

- **구현 결과**

<img width="1185" alt="image" src="https://user-images.githubusercontent.com/95380638/173997252-198574f9-bad7-46b2-ba15-e80c89b12cf1.png">

<br>

### 📌 (4) 채용공고 상세 페이지 API
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
- **요구사항 : 특정 채용공고에 대한 상세 페이지를 요청했을 때, 위와 같이 JSON 형태의 데이터를 확인할 수 있도록 설정 / 채용내용도 추가로 확인하도록 설정**

- **구현 과정**

<img width="709" alt="image" src="https://user-images.githubusercontent.com/95380638/173997975-ec077d56-fe16-4948-8a8b-f61fb8b5c642.png">

- **serializers.py에서 채용공고 상세 페이지를 확인하기 위한 JobPostingDetailSerializer 생성**
  - 전체 목록과 다르게 content 필드인 채용내용 필드를 추가해서 확인할 수 있도록 설정
  - class Meta에 depth = 1를 설정해서 1:N관계로 있는 Company 모델 데이터 보여주기 

<img width="685" alt="image" src="https://user-images.githubusercontent.com/95380638/173998221-cb7feb46-f093-4d65-ad06-dfea8c864fa2.png">

- **views.py에서는 채용공고 상세 조회를 위한 JobPostingAPIView를 APIView를 상속받아 생성**
  - GET 방식으로 요청이 올 때, 상세 pk를 받고 get_object_or_404 코드로 객체가 있으면 보여주고 없으면 404 예외처리 진행

- **urls.py에서는 jobpostings/<int:pk>/ 로 URL를 설정해서 채용공고 상세 조회 및 추후에 수정과 삭제시에도 pk를 받도록 설정**

- **구현 결과**

<img width="1194" alt="image" src="https://user-images.githubusercontent.com/95380638/173998398-69641243-0c76-4892-a7c9-30ae8317cea3.png">

<br>

### 📌 (5) 채용공고 수정 API
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

- **구현 결과**

<img width="1199" alt="image" src="https://user-images.githubusercontent.com/95380638/173999691-8ae7ac12-24c2-4b24-891e-5d2bd94b5b06.png">


<br>

### 📌 (6) 채용공고 삭제 API
- **요구사항 : 특정 채용공고를 삭제할 수 있도록 설정**

- **구현 과정**

<img width="672" alt="image" src="https://user-images.githubusercontent.com/95380638/174000241-59951fe1-8f5d-41ee-a3ed-1c730363e4a4.png">

- **views.py에서는 채용공고 상세 조회를 하는 JobPostingAPIView에서 DELETE 방식으로 요청이 왔을 때 채용공고를 삭제할 수 있도록 설정**
  - DELETE 방식일 때 채용공고 pk를 받고 get_object_or_404로 모델 데이터가 있으면 가져오고 없으면 404 예외처리
  - 해당 객체를 jobposting.delete() 이렇게 삭제시키기
  - 삭제 이후 204코드 응답

- **구현 결과**

<img width="1214" alt="image" src="https://user-images.githubusercontent.com/95380638/174000719-40c49624-dbdf-4b1d-b21a-72afb4094dde.png">

