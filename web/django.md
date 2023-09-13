# Django

## Framework

- 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
- 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공

### Framework를 사용하는 이유

- 기본적인 구조, 도구, 규칙  등을 제공하기 때문에 개발자는 피룻적인 해야 하는 핵심 개발에만 집중 할 수 있음
- 여러 라이브러리를 제공해 개발 속도를 빠르게 할 수 있음(생산성)
- 유지보수와 확장에 용이해 소프트웨어의 품질을 높임

## Django

- Python 기반의 대표적인 웹 프레임워크
- 검증된 웹 프레임워크
- 대규모 서비스에서도 안정적인 서비스 제공

## 클라이언트와 서버

### 웹의 동작 방식

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/6425c9ba-69f5-4b6a-9471-19f7987a38be)

- 클라이언트(Client)
    - 서비스를 요청하는 주체
    - 웹 사용자의 인터넷이 연결된 장치, 웹 브라우저
- 서버(Server)
    - 클라이언트의 요청에 응답하는 주체
    - 웹 페이지, 앱을 저장하는 컴퓨터
- ⭐우리가 웹 페이지를 보게 되는 과정⭐
    - 웹 브라우저(클라이언트)에서 google.com을 입력
    - 브라우저는 인터넷에 연결된 전세계 어딘 가에 있는 구글 컴퓨터(서버)에게 ‘Google 홈페이지.html’ 파일을 달라고 요청
    - 요청을 받은 구글 컴퓨터는 데이터베이스에서 ‘Google 홈페이지.html’ 파일을 찾아 응답
    - 전달받은 Google 홈페이지.html 파일을 웹 브라우저가 사람이 볼 수 있도록 해석해주면서 사용자는 구글의 메인 페이지를 보게 됨

 

## 프로젝트 및 가상환경

### 가상 환경

- Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 **독립적인** 실행 환경
- 가상 환경이 필요한 경우
    - 한 개발자가 2개의 프로젝트를 진행하는데 각 프로젝트에 사용해야하는 requests 패키지 버전이 다르기 때문에 파이썬 환경에서는 두가지 버전이 양립할 수 없어 독립적인 개발 환경이 필요
    - 한 개발자가 2개의 프로젝트를 진행하는데 각 프로젝트에서 사용해야하는 패키지가 함께 사용하면 충돌이 발생하는 경우 독립적인 개발 환경이 필요

#### 가상 환경 venv 생성

```bash
$ python -m venv venv
```

#### 가상 환경 활성화

- global에서 가상 환경으로 이동하는 것이 아닌 **활성화**

```bash
$ source venv/Scripts/activate
```

#### 환경에 설치된 패키지 목록 확인

```bash
$ pip list
```

- 2명의 개발자가 하나의 프로젝트를 함께 개발하는 경우, 서로 어떤 패키지를 설치했고, 어떤 버전을 설치했는지 파악하고 있어야 하므로 패키지 목록이 공유되어야 함

### 의존성 패키지

- 한 소프트웨어 패키지가 다른 패키지의 기능이나 코드를 사용하기 때문에 그 패키지가 존재해야만 제대로 작동하는 관계
- 사용하려는 패키지가 설치되지 않았거나, 호환되는 버전이 아니면 오류가 발생하거나 예상치 못한 동작을 보일 수 있음
- 개발 환경에서는 각각의 프로젝트가 사용하는 패키지와 그 버전을 정확히 관리한느 것이 중요
- 가상환경 & 의존성 패키지 관리

#### 의존성 패키지 목록 생성

```bash
$ pip freeze > requirements.txt
```

### Django 프로젝트 생성 전 루틴

```bash
# 1. 가상환경(venv) 생성
$ python -m venv venv

# 2. 가상환경 활성화
$ source venv/Scripts/activate

# 3. Django 설치
$ pip install Django

# 4. 의존성 파일 생성
$ pip freeze > requirements.txt
```

### Django 프로젝트 생성

```bash
# firstpjt라는 이름의 프로젝트를 생성
$ django-admin startproject firstpjt .
```

### Django 서버 실행

```bash
# manage.py와 동일한 경로에서 명령어 진행
$ python manage.py runserver
```

### 서버 확인

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 접속 후 확인

## Django 프로젝트와 앱

### Django Project

- 애플리케이션의 집합
- DB 설정, URL 연결, 전체 앱 설정 등을 처리

### Django application

- 독립적으로 작동하는 기능 단위 모듈
- 각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성

![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/adf1975c-3cb2-436d-acb4-b514068fbc9e)

### 앱 사용 과정

- 앱 생성

```bash
# 앱의 이름은 복수형으로 지정하는 것을 권장
$ python manage.py startapp articles
```

- 앱 등록

```python
# 반드시 앱을 생성한 후에 등록해야 함
# 등록 후 생성은 불가능

# settings.py
INSTALLED_APPS = [
	'articles',
	'django.contrib.admin',
	'django.contrib.auth',
	'dfango.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]
```

## Django 디자인 패턴

### 디자인 패턴

- 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책
- 공통적인 문제를 해결하는데 쓰이는 형식화 된 관행

### MVC 디자인 패턴

- Model, View, Controller
- 애플리케이션을 구조화하는 대표적인 패턴
- 데이터, 사용자 인터페이스, 비즈니스 로직을 분리
- 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위해

### MTV 디자인 패턴

- Model, Template, View
- Django에서 애플리케이션을 구조화하는 패턴
- 기존 MVC 패턴과 동일하나 명칭을 다르게 정의한 것
    - View → Template
    - Controller → View

### 프로젝트 구조

- setting.py
    - 프로젝트의 모든 설정을 관리
- urls.py
    - URL과 이에 해당하는 적절한 views를 연결
- \__init\__.py
    - 해당 폴더를 패키지로 인식하도록 설정
- asgi.py
    - 비동기식 웹 서버와의 연결 관련 설정
- wsgi.py
    - 웹 서버와의 연결 관련 설정
- manage.py
    - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

### 앱 구조

- admin.py
    - 관리자용 페이지 설정
- models.py
    - DB와 관련된 Model을 정의
    - MTV 패턴의 M
- views.py
    - HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환
    - url, mode, template과 연계
    - MTV 패턴의 V
- apps.py
    - 앱의 정보가 작성된 곳
- tests.py
    - 프로젝트 테스트 코드를 작성하는 곳

## 요청과 응답

### Django와 요청&응답

![Untitled 2](https://github.com/yuj1818/TIL/assets/95585314/8736c679-02dc-4032-ad6d-94f82a4e1aba)

### URLs

```python

# urls.py

from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
		path('admin/', admin.site.urls),
		path('articles/', views.index),
]
```

- [http://127.0.0.1:8000/articles/](http://127.0.0.1:8000/articles/) 로 요청이 왔을 때, views 모듈의 index 뷰 함수를 호출

### View

```python
# views.py

from Django.shortcuts import render

def index(request):
		return render(request, 'articles/index.html')
```

- 특정 경로에 있는 template과 request 객체를 결합해 응답 객체를 반환하는 index view 함수 정의

### Template

- articles 앱 폴더 안에 templates 폴더 생성
    - 폴더명은 반드시 templates 여야 하며 개발자가 직접 생성해야 함
- templates 폴더 안에 articles 폴더 생성
- articles 폴더 안에 템플릿 파일 생성

### Django에서 template을 인식하는 경로 규칙

- 예시
    - **app폴더 / templates /** articles / index.html
    - **app폴더 / templates /** example.html
- Django는 templates 폴더 까지 기본 경로로 인식하기 때문에 이 지점 이후의 template 경로를 작성해야 함

![Untitled 3](https://github.com/yuj1818/TIL/assets/95585314/f51f6a7f-2b4c-4c5f-b1b4-786e8d9cf8e3)

### 데이터 흐름에 따른 코드 작성

- URLs → View → Template
    
    ![Untitled 4](https://github.com/yuj1818/TIL/assets/95585314/a788c6b4-79d3-4dd4-904d-8b4284031878)
    
## Django Template

데이터 표현을 제어하면서, 표현과 관련된 부분을 담당

### Django Template Language(DTL)

- Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

### DTL Syntax

1. Variable
    - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
    - 딕셔너리 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨
    - dot(.)을 사용하여 변수 속성에 접근할 수 있음
    
    ```html
    {{variable}}
    ```
    
2. Filters
    - 표시할 변수를 수정할 때 사용
    - chained가 가능하며 일부 필터는 인자를 받기도 함
    - 약 60개의 built-in template filters를 제공
    
    ```html
    {{variable|filter}}
    ```
    
3. Tags
    - 반복 또는 논리를 수행하여 제어 흐름을 만듦
    - 일부 태그는 시작과 종료 태그가 필요
    - 약 24개의 built-in template tags를 제공
    
    ```html
    {% tag %}
    ```
    
4. Comments
    - DTL에서의 주석
    
    ```html
    {# #}
    {% comment %}
    		{% if name == 'Sophia' %}
    		{% endif %}
    {% endcomment %}
    ```
    

### DTL 예시

```python
# urls.py
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index),
    path('dinner/', views.dinner)
]
```

```python
# views.py
def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked
    }

    return render(request, 'articles/dinner.html', context)
```

```html
<!-- articles/dinner.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>{{ picked }} 메뉴는 {{ picked|length }}글자 입니다.</p>
    <h1>메뉴판</h1>
    <ul>
        {% for food in foods %}
            <li>{{ food }}</li>
        {% endfor %}
    </ul>
    {% if foods|length == 0 %}
        <p>메뉴가 소진 되었습니다.</p>
    {% else %}
        <p>아직 메뉴가 남았습니다.</p>
    {% endif %}
</body>
</html>
```

## 템플릿 상속

### 기본 템플릿 구조의 한계

- 만약 모든 템플릿에 bootstrap을 적용하려면
- 모든 템플릿에 bootstrap CDN을 작성해야 할까?

### 템플릿 상속(Template Inheritance)

- **페이지의 공통요소를 포함**하고, **하위 템플릿이 재정의 할 수 있는 공간**을 정의하는 기본 ‘skeleton’ 템플릿을 작성하여 상속 구조를 구축

### 상속 구조 구축

- skeleton 역할의 상위 템플릿 작성

```html
<!-- articles/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
		...
		{% comment %} bootstrap CDN 생략 {% endcomment %}
</head>
<body>
		{% block content %}
		{% endblock content %}
		{% comment %} bootstrap CDN 생략 {% endcomment %}
</body>
</html>
```

- 기존 하위 템플릿의 변화

```html
<!-- articles/index.html -->

{% extends 'articles/base.html' %}
{% block content %}
		<h1>Hello, {{ name }}</h1>
{% endblock content %}
```

```html
<!-- articles/dinner.html -->
{% extends "articles/base.html" %}
{% block content %}
    <p>{{ picked }} 메뉴는 {{ picked|length }}글자 입니다.</p>
    <h2>메뉴판</h2>
    <ul>
        {% for food in foods %}
            <li>{{ food }}</li>
        {% endfor %}
    </ul>
    {% if foods|length == 0 %}
        <p>메뉴가 소진 되었습니다.</p>
    {% else %}
        <p>아직 메뉴가 남았습니다.</p>
    {% endif %}
{% endblock content %}
```

### ‘extends’ tag

- 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
- **반드시 템플릿 최상단에 작성되어야 함(2개 이상 사용 불가)**

### ‘block’ tag

- 하위 템플릿에서 재정의 할 수 있는 블록을 정의
- 하위 템플릿이 작성할 수 있는 공간을 지정

## HTML form(요청과 응답)

### 데이터를 보내고 가져오기(Sending and Retrieving form data)

- HTML form element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기
- HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법

### ‘form’ element

- 사용자로부터 할당된 데이터를 서버로 전송
- 웹에서 사용자 정보를 입력하는 여러 방식(text, password, checkbox 등)을 제공

### fake Naver 실습

```python
# urls.py

from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search)
]
```

```python
# views.py

from django.shortcuts import render

def search(request):
    return render(request, 'articles/search.html')
```

```html
<!-- articles/search.html -->
{% extends "articles/base.html" %}
{% block content %}
    <form action="https://search.naver.com/search.naver/" method="GET">
        <label for="message">검색어</label>
        <input type="text" name="query" id="message">
        <input type="submit" value="submit">
    </form>
{% endblock content %}
```

### ‘action’ & ‘method’

- form의 핵심 속성 2가지
- 데이터를 어디(action)로 어떤 방식(method)으로 요청할지

#### action

- 입력 데이터가 전송될 URL을 지정(목적지)
- 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

#### method

- 데이터를 어떤 방식으로 보낼 것인지 정의
- 데이터의 HTTP request methods (GET, POST)를 지정

### ‘input’ element

- 사용자의 데이터를 입력 받을 수 있는 요소
- type 속성 값에 따라 다양한 유형의 입력 데이터를 받음

### ‘name’ attribute

- input의 핵심 속성
- 입력한 데이터에 붙이는 이름(key)
- 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음

### Query String Parameters

- 사용자의 입력 데이터를 URL 주소에 파라미털ㄹ 통해 서버로 보내는 방법
- 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성되며, 기본 URL과 물음표(?)로 구분됨
- 예시
    - http://host:port/path?key=value&key=value

## form 활용

### 사용자 입력 데이터를 받아 그대로 출력하는 서버 만들기

```python
# urls.py
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('throw/', views.throw),
    path('catch/', views.catch)
]
```

```python
# views.py
from django.shortcuts import render

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    msg = request.GET.get('message')
    context = {
        'msg': msg
    }
    return render(request, 'articles/catch.html', context)
```

```html
<!-- throw.html -->
{% extends "articles/base.html" %}
{% block content %}
    <h1>Throw</h1>
    <form action="/catch/" method="GET">
        <input type="text" id="message" name="message">
        <input type="submit">
    </form>
{% endblock content %}
```

```html
<!-- catch.html -->
{% extends "articles/base.html" %}
{% block content %}
    <h1>Catch</h1>
    <h3>{{ msg }}를 받았습니다!</h3>
{% endblock content %}
```

### HTTP request 객체

- form으로 전송한 데이터뿐만 아니라 모든 요청 관련 데이터가 담겨 있음
- view 함수의 첫번째 인자
- form 데이터를 가져오는 방법
    
    ```python
    request.GET.get(데이터 name)
    ```
    

## Django URLs

### 요청과 응답에서 Django URLs의 역할

![Untitled 6](https://github.com/yuj1818/TIL/assets/95585314/68206ff4-dc1e-4af8-ba32-08618a38c77d)

### URL dispatcher

- 운항 관리자, 분배기
- URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)

## 변수와 URL

### 현재 URL 관리의 문제점

- 템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면 계속해서 비슷한 URL과 템플릿을 작성해 나가야 할까?

### Variable Routing

- URL 일부에 변수를 포함시키는 것
- 변수는 view 함수의 인자로 전달할 수 있음

#### Variable routing 작성법

- <`path_converter` : variable_name>

```python
path('articles/<int:num>/', views.detail),
path('hello/<str:name>/', views.greeting)
```

`path converters` : URL 변수의 타입을 지정(str, int 등 5가지 타입 지원)

#### Varibale routing 실습

```python
# urls.py
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('hello/<str:name>/', views.greeting)
]
```

```python
# views.py
from django.shortcuts import render

def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'articles/greeting.html', context)
```

```html
<!-- articles/greetings.html -->
{% extends "base.html" %}
{% block content %}
    <h1>Greeting</h1>
    <h3>{{ name }}님 안녕하세요!</h3>
{% endblock content %}
```

## APP과 URL

### App URL mapping

- 각 앱에 URL을 정의하는 것
- 프로젝트와 각 앱이 URL을 나누어 관리를 편하게 하기 위함

### 2번째 앱 생성 후 발생할 수 있는 문제

- view 함수 이름이 같거나 같은 패턴의 url주소를 사용하게 되는 경우
- 아래 코드와 같이 해결할 수 잇으나 더 좋은 방법이 필요
- **URL을 각자 app에서 관리하자**

#### 기존 URL 구조

![Untitled 6](https://github.com/yuj1818/TIL/assets/95585314/68206ff4-dc1e-4af8-ba32-08618a38c77d)

#### 변경된 URL 구조

![Untitled 7](https://github.com/yuj1818/TIL/assets/95585314/65fe9f40-f3da-435f-b3b0-cb82e39a3682)

### url 구조 변화

```python
# firstpjt/urls.py
from django.contrib import admin
from django.urls import path, include
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls'))
]
```

```python
# articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('articles/', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.greeting)
]
```

```python
# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index)
]
```

### include()

- 프로젝트 내부 앱들을 URL을 참조할 수 있도록 매핑하는 함수
- URL의 일치하는 부분까지 잘라내고, 남은 문자열 부분은 후속 처리를 위해 include된 URL로 전달

## URL 이름 지정

### url 구조 변경에 따른 문제점

- 기존 ‘articles/’주소가 ‘articles/index/’로 변경됨에 따라 해당 주소를 사용하는 모든 위치를 찾아가 변경해야 함
- **URL에 이름을 지어주면 이름만 기억하면 되지 않을까?**

### Naming URL patterns

- URL에 이름을 지정하는 것
- path 함수의 name 인자를 정의해서 사용

```python
# articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('articles/', views.index, name='articles'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.greeting, name='greeting')
]
```

```html
<!-- articles/index.html -->
{% extends "base.html" %}
{% block content %}
  <h1>안녕! {{name}}</h1>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'search' %}">search</a>
  <a href="{% url 'throw' %}">throw</a>
{% endblock content %}
```

![Untitled 8](https://github.com/yuj1818/TIL/assets/95585314/6b8f3ecf-344c-43bc-9786-4b9a277024f5)

### ‘url’ tag

```html
{% url 'url-name' arg1 arg2 %}
```

- 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환

## URL 이름 공간

### URL 이름 지정 후 남은 문제

- articles 앱의 url 이름과 pages 앱의 url 이름이 같은 상황
- 단순히 이름만으로는 완벽하게 분리할 수 없음
- **이름에 성(키, key)를 붙이자**

### ‘app_name’ 속성 지정

```python
# articles/urls.py
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    ...,
]
```

```python
# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    ...,
]
```

### URL tag의 최종 변화

{% url ‘index’ %} ⇒ {% url ‘articles:index’ %}


## 참고

### Django 프로젝트 생성 루틴 정리 + git

- 가상환경 생성
- 가상환경 활성화
- django 설치
- 의존성 파일 생성(패키지 설치시마다 진행)
- .gitignore 파일 생성(첫 add 전)
- git 저장소 생성
- Django 프로젝트 생성

### 가상환경을 사용하는 이유

- 의존성 관리
    - 라이브러리 및 패키지를 각 프로젝트마다 독립적으로 사용 가능
- 팀 프로젝트 협업
    - 모든 팀원이 동일한 환경과 의존성 위에서 작업하여 버전간 충돌을 방지

### LTS(Long-Term Support)

- 프레임워크나 라이브러리 등의 소프트웨어에서 장기간 지원되는 안정적인 버전을 의미할 때 사용
- 기업이나 대규모 프로젝트에서는 소프트웨어 업그레이드에 많은 비용과 시간이 필요하기 때문에 안정적이고 장기간 지원되는 버전이 필요
- https://www.djangoproject.com/download/

### requirements 설치 방법

```bash
# requirements.txt에 있는 패키지 설치 방법
$ pip install -r requirements.txt
```

### MTV 디자인 패턴 정리

- Model
    - 데이터와 관련된 로직을 관리
    - 응용 프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
- Template
    - 레이아웃과 화면을 처리
    - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
- View
    - Model & Template과 관련한 로직을 처리해서 응답을 반환
    - 클라이언트의 요청에 대해 처리를 분기하는 역할
- View 예시
    - 데이터가 필요하다면 model에 접근해서 데이터를 가져옴
    - 가져온 데이터를 template로 보내 화면을 구성
    - 구성된 화면을 응답으로 만들어 클라이언트에게 반환

![Untitled 5](https://github.com/yuj1818/TIL/assets/95585314/188e34b5-8471-4d15-ac0b-60f98062391c)

### render 함수

- 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수
- request
    - 응답을 생성하는 데 사용되는 요청 객체
- template_name
    - 템플릿 이름의 경로
- context
    - 템플릿에서 사용할 데이터(딕셔너리 타입으로 작성)

```python
render(request, template_name, context)
```

### 추가 템플릿 경로 지정

- 템플릿 기본 경로 외 커스텀 경로 추가하기

```python
# setting.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- 최상위 폴더에 templates 폴더 만들어서 그 안에 base.html 생성
- extends 경로 수정

```html
{% extends 'base.html' %}
```

#### BASE_DIR

- settings에서 경로 지정을 편하게 하기 위해 최상단 지점을 지정 해놓은 변수

### DTL 주의사항

- Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 명칭을 그렇게 설계했을 뿐이지 Python 코드로 실행되는 것이 아니며 Python과는 관련 없음
- 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리
- 공식문서를 참고해 다양한 태그와 필터 사용해보기
    - [https://docs.djangoproject.com/en/4.2/ref/templates/builtins/](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/)

### Trailing Slashes

- Django는 URL 끝에 ‘/’가 없다면 자동으로 붙임
- “기술적인 측면에서, [foo.com/bar와](http://foo.com/bar와) [foo.com/bar/는](http://foo.com/bar/는) 서로 다른 URL”
    - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 이 두 주소를 서로 다른 페이지로 봄
- 그래서 Django는 검색 엔진이 혼동하지 않게 하기 위해 붙이는 것을 선택한 것
- 그러나 모든 프레임워크가 이렇게 동작하는 것은 아니니 주의