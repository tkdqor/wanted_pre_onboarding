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

- employment App 내부에 serializers.py 파일을 생성하고 채용공고 전체 목록을 조회하기 위한 Serializer를 생성 
  - serializer 필드를 자동으로 설정해주는 ModelSerializer를 상속받아 진행
- models.py에 설정한 필드 이름이 아닌 한글명으로 사용하기 위해 Serializer 내부에 새로운 필드 설정
- depth = 1 코드를 추가해서 Company 모델과 JobPosting 모델이 1:N관계이므로 관련된 Company 모델 데이터 보여주기 
