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

## Django Model

- DB의 테이블을 정의하고 조작할 수 있는 기능들을 제공
- 테이블 구조를 설계하는 청사진(blueprint)

### model 클래스 작성

```python

# articles/models.py

class Article(models.Model):
		title = models.CharField(max_length=10)
		content = models.TextField()
```

- 위의 모델 클래스는 최종적으로 DB에 다음과 같은 테이블 구조를 만듦

![모델 클래스 == 테이블 설계도](https://github.com/yuj1818/TIL/assets/95585314/37ab9bdd-e385-4f1a-98ed-cd526abf67ac)

모델 클래스 == 테이블 설계도

- django.db.models 모듈의 Model이라는 부모 클래스를 상속 받음
- Model은 model에 관련된 모든 코드가 이미 작성되어있는 클래스
    - [https://github.com/django/django/blob/main/django/db/models/base.py#L459](https://github.com/django/django/blob/main/django/db/models/base.py#L459)
- 개발자는 가장 중요한 테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록 하기 위한 것(프레임워크의 이점)
- 클래스 변수명
    - 테이블의 각 “필드(열) 이름”
    - title, content
- model Field 클래스
    - 테이블 필드의 “데이터 타입”
    - CharField, TextField
    - [https://docs.djangoproject.com/en/4.2/ref/models/fileds/](https://docs.djangoproject.com/en/4.2/ref/models/fileds/)
- model Field 클래스의 키워드 인자
    - 테이블 필드의 `제약조건` 관련 설정
    - [https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-options](https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-options)
    - `제약조건` : 데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙(ex: 숫자만, 문자 100자 까지만 등)

## Migrations

model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법

### ⭐Migrations 과정⭐

![Untitled 10](https://github.com/yuj1818/TIL/assets/95585314/00f13a75-ad10-4ba5-868d-acaad77f282e)

- model class를 기반으로 최종 설계도(migration) 작성

```bash
$ python manage.py makemigrations
```

- 최종 설계도를 DB에 전달하여 반영

```bash
$ python manage.py migrate
```

### migrate 후 DB 내에 생성 된 테이블 확인

- Article 모델 클래스로 만들어진 articles_article 테이블

![Untitled 11](https://github.com/yuj1818/TIL/assets/95585314/49bdbc8c-3404-4619-8b73-2a5929101d99)

### 추가 Migrations

#### 추가 모델 필드 작성

```python
# articles/models.py

class Articles(models.Model):
		title = models.CharField(max_length=10)
		content = models.TextField()
		created_at = models.DateTimeField(auto_now_add=True)
		updated_at = models.DateTimeField(auto_now=True)
```

- 이미 기존 테이블이 존재하기 때문에 필드를 추가할 때 필드의 기본 값 설정이 필요
- 1번은 현재 대화를 유지하면서 직접 기본 값을 입력하는 방법
- 2번은 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법

```bash
$ python manage.py makemigrations
```

![Untitled 12](https://github.com/yuj1818/TIL/assets/95585314/3141d884-9ede-4ea5-8cd6-132b774cdb1e)

- 추가하는 필드의 기본 값을 입력해야하는 상황
- 날짜 데이터이기 때문에 직접 입력하기 보다 Django가 제안하는 기본 값을 사용하는 것을 권장
- 아무것도 입력하지 않고 enter를 누르면 Django가 제안하는 기본 값으로 설정 됨

![Untitled 13](https://github.com/yuj1818/TIL/assets/95585314/73398fe7-d8c6-4f69-a71c-0780e29ec25b)

- migrations 과정 종료 후 2번째 migration 파일이 생성됨을 확인

![Untitled 14](https://github.com/yuj1818/TIL/assets/95585314/6409bf35-f76b-43db-9cac-fe5cda79cb1d)

- 이처럼 Django는 설계도를 쌓아가면서 추후 문제가 생겼을 시 복구하거나 되돌릴 수 있도록 함(≒ git commit)
- migrate 후 테이블 필드 변화 확인

```bash
$ python manage.py migrate
```

![Untitled 15](https://github.com/yuj1818/TIL/assets/95585314/8225fb7a-ad68-49e6-91ef-0a37e0c2c680)

- **model class에 변경사항이 생겼다면, 반드시 새로운 설계도를 생성하고, 이를 DB에 반영해야 함**
    - model class 변경 → makemigrations → migrate

### Model Field

- DB 테이블의 필드(열)을 정의하며, 해당 필드에서 저장되는 데이터 타입과 제약조건을 정의

#### CharField()

- 길이의 제한이 있는 문자열을 넣을 때 사용
- 필드의 최대 길이를 결정하는 max_length는 필수 인자

#### TextField()

- 글자의 수가 많을 때 사용

#### DateTimeField()

- 날짜와 시간을 넣을 때 사용
- 📒DateTimeField의 선택 인자
    - auto_now
        - 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장
    - auto_now_add
        - 데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장

## Admin site

### Automatic admin interface

- Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
- 데이터 확인 및 테스트 등을 진행하는데 매우 유용

### admin 계정 생성

- email은 선택사항이기 때문에 입력하지 않고 진행 가능
- 비밀번호 입력 시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기

```bash
$ python manage.py createsuperuser
```

### admin에 모델 클래스 등록

- admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능

```python
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

## ORM(Object-Relational-Mapping)

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

### ORM의 역할

- django(Python Object)와 DB(SQL)는 서로 다른 언어를 사용하기 때문에 소통이 불가
- ORM이 django와 DB의 중간에서 소통을 가능하게 함

### QuerySet API

- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구
- API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리
- Python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것

<img src="https://github.com/yuj1818/TIL/assets/95585314/3c1eb412-a2de-421e-9866-46c06ac3ff16" width="50%">

#### QuerySet API 구문

- (Model class).(Manager).(Queryset API)’
- Manager가 method를 가지고 있음
- 예) Article.objects.all()

#### Query

- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- 쿼리문을 작성한다 ⇒ 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다
- 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달

#### QuerySet

- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
    - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
- Django ORM을 통해 만들어진 자료형
- 단, 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

### QuerySet API 실습

#### QuerySet API 실습 사전 준비

```bash
pip install ipython
pip install django-extensions
```

```python
# settings.py

INSTALLED_APPS = [
		# local applications
		'articles',
		# 외부 라이브러리
		'django_extensions',
		# 장고 내부
		...,
]
```

```bash
pip freeze > requirements.txt
```

#### Django shell

- Django 환경 안에서 실행되는 python shell
- 입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침

```bash
# Django shell 실행
python manage.py shell_plus
```

#### Create

```bash
# 방법 1
article = Article() # Article(class)로부터 article(instance) 생성
article.title = 'first' # 인스턴스 변수(title)에 값을 할당
article.content = 'django!' # 인스턴스 변수(content)에 값을 할당
article.save() # save를 하지 않으면 아직 DB에 값이 저장되지 않음
```

```bash
# 방법 2
article = Article(title='second', content='django!')
article.save()
```

```bash
# 방법 3
Article.objects.create(title='third', content='django!')
```

`save()` : 객체를 데이터베이스에 저장하는 메서드

#### Read

```bash
Article.objects.all()
```

`all()` : 전체 데이터 조회

```bash
Article.objects.get(pk=1) # 1번째 데이터 조회
Article.objects.get(pk=100) # 100번째 데이터 조회
Article.objects.get(content='django!')
# content 필드 값이 django!인 데이터가 여러 개이므로 에러가 일어남.
# get()은 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
# 위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함
```

`get()` : 단일 데이터 조회

```bash
Article.objects.filter(content='django!') # content 필드 값이 django!인 데이터 다 조회
Article.objects.filter(title='abc') # title 필드 값이 abc이 데이터 다 조회
Article.objects.filter(title='first') # title 필드 값이 first인 데이터 다 조회
```

`filter()` : 특정 조건 데이터 조회

#### Update

- 데이터 수정
- 인스턴스 변수를 변경 후 save 메서드 호출

```bash
article = Artile.objects.get(pk=1) # 수정할 인스턴스 조회
article.title = 'byebye' # 인스턴스 변수 변경
article.save() # 저장
```

#### Delete

- 데이터 삭제
- 삭제하려는 데이터 조회 후 delete 메서드 호출

```bash
article = Article.objects.get(pk=1) # 삭제할 인스턴스 조회
article.delete() # delete 메서드 호출
```

### ORM with view

#### Read

- 전체 게시글 조회

```python
# articles/views.py

from .models import Article

def index(request):
articles = Article.objects.all()
context = {
	'articles': articles,
}
return render(request, 'articles/index.html', context)
```

```html
<!-- articles/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Articles</h1>
  <hr>
  {% for article in articles %}
    <p>글번호: {{article.pk}}</p>
    <p>글 제목: {{article.title}}</p>
    <p>글 내용: {{article.content}}</p>
    <hr>
  {% endfor %}
</body>
</html>
```

- 단일 게시글 조회

```python
# articles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
]
```

```python
# articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

```html
<!-- templates/articles/detail.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h2>DETAIL</h2>
  <h3>{{article.pk}} 번째 글</h3>
  <hr>
  <p>제목: {{article.title}}</p>
  <p>내용: {{article.content}}</p>
  <p>작성 시각: {{article.created_at}}</p>
  <p>수정 시각: {{article.updated_at}}</p>
  <hr>
  <a href="{% url "index" %}">[back]</a>
</body>
</html>
```

#### Create

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    ...
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
```

```python
# articles/views.py

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article(title=title, content=content)
    article.save()

    return render(request, 'articles/create.html')
```

```html
<!-- templates/articles/new.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>NEW</h1>
  <form action="">
    <div>
      <label for="title">Title: </label>
      <input type="text" id="title" name="title">
    </div>
    <div>
      <label for="content">Content: </label>
      <textarea name="content" id="content"></textarea>
    </div>
    <input type="submit" value="제출">
  </form>
  <hr>
  <a href="articles:index">[back]</a>
</body>
</html>
```

#### HTTP request methods

- HTTP
    - 네트워크 상에서 데이터를 주고 받기 위한 약속
- HTTP request methods
    - 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것
    - GET
        - 특정 리소스를 조회하는 요청
        - GET으로 데이터를 전달하면 Query string 형식으로 보내짐
    - POST
        - 특정 리소스에 변경(생성, 수정, 삭제)을 요구하는 요청
        - POST로 데이터를 전달하면 HTTP Body에 담겨 보내짐
- HTTP response status code
    - 특정 HTTP 요청이 성공적으로 완료되었는지를 3자리 숫자로 표현하기로 약속한 것
    - [https://developer.mozilla.org/en-US/docs/Web/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
    - 403 Forbidden
        - 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
- CSRF(Cross-Site-Request-Forgery)
    - 사이트 간 요청 위조
    - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
    - 요청 시 CSRF Token을 함께 보내야 하는 이유
        - Django 서버는 해당 요청이 DB에 데이터를 하나 생성하는 (DB에 영향을 주느) 요청에 대해 “Django 가 직접 제공한 페이ㅣ에서 데이터를 작성하고 있는지에 대한 확인 요소 필요
        - 겉모습이 똑같은 위조 사이트나 정상적이지 않은 요청에 대한 방어 수단
        - 기존 - 요청 데이터 → 게시글 작성
        - 변경 - 요청 데이터 + 인증 토큰 → 게시글 작성
    - POST일 때만 Token을 확인하는 이유
        - POST는 단순 조회를 위한 GET과 달리 특정 리소스에 변경
        - DB에 조작을 가하는 요청은 반드시 인증 수단이 필요
        - 데이터베이스에 대한 변경사항을 만드는 요청이기 때문에 토큰을 사용하여 최소한의 신원을 확인하는 것
- redirect
    - 클라이언트가 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수
    - 게시글 작성 후 완료를 알리는 페이지를 응답하는 것
    - 데이터 저장 후 페이지를 주는 것이 아닌 다른 페이지로 사용자를 보내야 함
    
    ```python
    # articles/views.py
    
    from django.shortcuts import render, redirect
    
    def create(request):
        title = request.GET.get('title')
        content = request.GET.get('content')
    
        article = Article(title=title, content=content)
        article.save()
    
        return redirect('articles:detail', article.pk)
    ```
    
    - 해당 redirect에서 클라이언트는 detail url로 요청을 다시 보내게 됨
    - 결과적으로 detail view 함수가 호출되어 detail view 함수의 반환 결과인 detail 페이지를 응답 받음
    - 결국 사용자는 게시글 작성 후 작성된 게시글의 detail 페이지로 이동하는 것으로 느끼게 되는 것

#### Delete

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    ...
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```

```python
# article.views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

```html
<!-- templates/articles/detail.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h2>DETAIL</h2>
  <h3>{{article.pk}} 번째 글</h3>
  <hr>
  <p>제목: {{article.title}}</p>
  <p>내용: {{article.content}}</p>
  <p>작성 시각: {{article.created_at}}</p>
  <p>수정 시각: {{article.updated_at}}</p>
  <hr>
  <form action="{% url "articles:delete" article.pk %}" method="POST">
    <input type="submit" value="DELETE">
  </form>
  <a href="{% url "articles:index" %}">[back]</a>
</body>
</html>
```

#### Update

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    ...
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update', views.update, name='update'),
]
```

```python
# articles/views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)
```

```html
<!-- templates/articles/edit.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>EDIT</h1>
  <form action="{% url "articles:update" article.pk %}" method="POST">
    {% csrf_token %}
    <div>
      <label for="title">Title: </label>
      <input type="text" id="title" name="title" value="{{article.title}}">
    </div>
    <div>
      <label for="content">Content: </label>
      <textarea name="content" id="content">{{article.content}}</textarea>
    </div>
    <input type="submit" value="제출">
  </form>
  <hr>
  <a href="{% url "articles:detail" article.pk %}">[back]</a>
</body>
</html>
```

## Django Form

- 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구
- 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공
- HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움

### HTML ‘form’ 의 한계

- form 태그는 지금까지 사용자로부터 데이터를 받기 위해 활용한 방법
- 비정상적 혹은 악의적인 요청을 필터링 할 수 없음
    - 수집한 데이터가 정확하고 유효한지에 대한 확인이 필요(유효성 검사)
        - 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함
        - 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

### Form class 정의

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

```python
# articles/views.py

def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

```html
<!-- templates/articles/new.html -->
<body>
  <h1>NEW</h1>
  <form action="{% url "articles:create" %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}    <!-- form rendering options -->
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
</body>
```

#### Form rendering options

- label, input 쌍을 특정 HTML 태그로 감싸는 옵션
    - [https://docs.djangoproject.com/en/4.2/topics/forms/#form-rendering-options](https://docs.djangoproject.com/en/4.2/topics/forms/#form-rendering-options)

### Widgets

- HTML ‘input’ element의 표현을 담당
- Widget은 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것
    - https://docs.djangoproject.com/ko/4.2/ref/forms/widgets/#built-in-widgets

```python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
	title = form.CharField(max_length=10)
	content = forms.CharField(widget=forms.Textarea)
```

## Django ModelForm

- Model과 연결된 Form을 자동으로 생성해주는 기능을 제공
    - Form + Model

| Form | ModelForm |
| --- | --- |
| 사용자 입력 데이터를 DB에 저장하지 않을 때 | 사용자 입력 데이터를 DB에 저장해야 할 때 |
| 로그인 | 게시글, 회원가입 |

### ModelForm class 정의

- 기존 ArticleForm 클래스 수정

```python
# articles/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'
```

#### Meta class

- ModelForm의 정보를 작성하는 곳
- ‘fields’ 및 ‘exclude’ 속성
    - exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음

```python
# articles/forms.py

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('title',)
```

```python
# articles/forms.py

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		exclude = ('title',)
```

- ModelForm 적용한 create 로직

#### is_valid()

- 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환

```python
# articles/views.py

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```

- ModelForm을 적용한 edit 로직

```python
# articles.views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

```html
<!-- articles/edit.html -->

<body>
  <h1>Edit</h1>
  <form action="{% url "articles:update" article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
</body>
```

- ModelForm을 적용한 update 로직

```python
# articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

#### save()

- 데이터베이스 객체를 만들고 저장
- 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정

## Handling HTTP requests

### view 함수 구조 변화

- new, create 함수
    - 공통점 - 데이터 생성을 구현하기 위함
    - 차이점 - new는 GET method 요청만을 create는 POST method 요청만을 처리
- new, create 함수 결합

```python
# articles/views.py

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context
```

- edit, update 함수 결합

```python
# articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

## Static Files

서버 측에서 변경되지 않고 고정적으로 제공되는 파일(이미지, JS, CSS 파일 등)

### 웹 서버와 정적 파일

- 웹 서버의 기본 동작은 특정 위치(URL)에 있는 자원을 요청(HTTP request) 받아서 응답(HTTP response)을 처리하고 제공(serving)하는 것
    - “자원에 접근 가능한 주소가 있다”
- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공
- 정적 파일을 제공하기 위한 경로(URL)가 있어야 함

### Static files 제공하기

1. 기본 경로에서 제공하기
    - app폴더/static
        
        ![Untitled 17](https://github.com/yuj1818/TIL/assets/95585314/290f2a7b-c513-4fa9-a58c-36238d013fc7)
        
    - static tag를 사용해 이미지 파일에 대한 url 제공
    
    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <img src="{% static "articles/sample-1.png" %}" alt="img">
    </body>
    </html>
    ```
    
    - STATIC_URL
        - 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
        - 실제 파일이나 디렉토리가 아니며, URL로만 존재
        
        ```python
        # settings.py
        
        STATIC_URL = 'static/'
        ```
        
2. 추가 경로에서 제공하기
    - STATICFILES_DIRS에 문자열 값으로 추가 경로 설정
    
    ```python
    # settings.py
    
    STATICFILES_DIRS = [
    	BASE_DIR / 'static',
    ]
    ```
    
    `STATICFILES_DIRS` : 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트
    
    - 추가 경로에 이미지 파일 배치
        
        ![Untitled 18](https://github.com/yuj1818/TIL/assets/95585314/17706371-15b8-4597-b18d-1aff9f39834c)
        
    - static tag를 사용해 이미지 파일에 대한 url 제공
    
    ```html
    <!-- articles/index.html -->
    
    <img src="{% static 'sample-2.png' %}" alt="img">
    ```
    
- **정적 파일을 제공하려면 요청에 응답하기 위한 URL이 필요**

## Media files

사용자가 웹에서 업로드하는 정적 파일(user-uploaded)

### 미디어 파일 제공

1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
    - 업로드 된 파일의 URL ⇒ settings.MEDIA_URL
    - 위 URL을 참조하는 파일의 실제 위치 ⇒ settings.MEDIA_ROOT
    
    `MEDIA_ROOT` : 미디어 파일들이 위치하는 디렉토리의 절대 경로
    
    `MEDIA_URL` : MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성
    
    ```python
    # settings.py
    
    MEDIA_URL = 'media/'
    
    MEDIA_ROOT = BASE_DIR / 'media'
    ```
    
2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정

```python
# crud/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	...
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 이미지 업로드

- blank=True 속성을 작성해 빈 문자열이 저장될 수 있도록 제약 조건 설정

```python
# articles/models.py

class Article(models.Model):
	title = models.CharField(max_length=10)
	content = models.TextField()
	image = models.ImageField(blank=True)
	created_at = models.DatetimeField(auto_now_add=True)
	updated_at = models.DatetimeField(auto_now=True)
```

- migrations 진행
- form 요소의 enctype 속성 추가

```html
<!-- articles/create.html -->
  <form action="{% url "articles:create" %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```

- view 함수에서 업로드 파일에 대한 추가 코드 작성

```python
# articles/views.py

def create(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST, request.FILES)
```

`ImageField()`

- 이미지 업로드에 사용하는 모델 필드
- 이미지 객체가 직접 저장되는 것이 아닌 '**이미지 파일의 경로**'가 문자열로 DB에 저장
    - 성능 및 DB 최적화
        - 직접 파일을 저장하면 DB 크기가 급격하게 증가
            - 성능이 저하
            - 파일 자체는 파일시스템에 별도로 저장
            - DB에는 그 파일에 대한 문자열 경로만
    - 유지 보수 관점
        - DB에 직접 파일에 저장해버리면 파일을 변경하거나 업데이트 할 때, DB를 직접 조작해야 함
        - 하지만, DB에 경로만 저장되어 있다면 파일시스템에서만 파일을 수정하면 되므로 유지 보수에 용이

### 업로드 이미지 제공

- ‘url’ 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
- article.image.url
    - 업로드 파일의 경로
- article.image
    - 업로드 파일의 파일 이름

```html
<!-- articles/detail.html -->

<img src="{{ article.image.url }}" alt="img">
```

- 이미지를 업로드 하지 않은 게시물은 detail 템플릿을 렌더링 할 수 없음
- 이미지 데이터가 있는 경우만 이미지를 출력할 수 있도록 처리

```html
<!-- articles/detail.html -->

{% if article.image %}
  <img src="{{ article.image.url }}" alt="img">
{% endif %}
```

- 수정 페이지 form 요소에도 enctype 속성 추가
    - update html form에 enctype 추가
- update view 함수에서 업로드 파일에 대한 추가 코드 작성
    - update view 함수 form 정의 부분에 request.FILES 추가

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

### 데이터베이스 초기화

- migration 파일 삭제(ex: 0001_initial.py)
- db.sqlite3 파일 삭제
- **/__init/__.py 파일이나 migrations 폴더를 지우지 않도록 주의 필요**

### Migrations 기타 명령어

```bash
$ python manage.py showmigrations
```

- migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 명령어
- [X] 표시가 있으면 migrate가 완료되었음을 의미

![Untitled 17](https://github.com/yuj1818/TIL/assets/95585314/b2dc1898-23eb-4098-95e8-c474ff578f3e)

```bash
$ python manage.py sqlmigrate articles 0001
```

- 해당 migrations 파일이 SQL 언어(DB에서 사용하는 언어)로 어떻게 번역되어 DB에 전달되는지 확인하는 명령어

![Untitled 18](https://github.com/yuj1818/TIL/assets/95585314/cd7e8ea1-0685-4e1c-9b19-85bbc0b40e9d)

### 첫 migrate 시 출력 내용이 많은 이유는?

- Django 프로젝트가 동작하기 위해 미리 작성 되어있는 기본 내장 app들에 대한 migration 파일들이 함께 migrate 되기 때문

### SQLite

- 데이터베이스 관리 시스템 중 하나이며 Django의 기본 데이터베이스로 사용됨
- 파일로 존재하며 가볍고 호환성이 좋음

### CRUD

- 소프트웨어가 가지는 기본적인 데이터 처리 기능
- Create(저장)
- Read(조회)
- Update(갱신)
- Delete(삭제)

### Field lookups

- 특정 레코드에 대한 조건을 설정하는 방법
- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨
- [https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups)

### ORM, QuerySet API를 사용하는 이유

- 데이터베이스 쿼리를 추상화하여 Django 개발자가 데이터베이스와 직접 상호작용하지 않아도 되도록 함
- 데이터베이스와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움

### QuerySet API 관련 문서

- [https://docs.djangoproject.com/en/4.2/ref/models/querysets](https://docs.djangoproject.com/en/4.2/ref/models/querysets)
- [https://docs.djangoproject.com/en/4.2/topics/db/queries/](https://docs.djangoproject.com/en/4.2/topics/db/queries/)

### HTTP request methods 사용 예시

- HTTP request methods를 활용한 효율적인 URL 구성
    - 동일한 URL이지만 method에 따라 서버에 요구하는 행동을 다르게 요구
        - (GET) articles/1/ ⇒ 1번 게시글 조회 요청
        - (POST) articles/1/ ⇒ 1번 게시글 조작 요청

### ModelForm 키워드 인자 data와 instance 살펴보기

- https://github.com/django/django/blob/main/django/forms/models.py#L341

```python
class BaseModelForm(BaseForm):
	def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
							 initial=None, error_class=ErrorList, label_suffix=None, 
               empty_permitted=False, instance=None, use_required_attribute=None,
               renderer=None):
```

### Widget 응용

```python
# articles/forms.py

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required':'내용을 입력해주세요.'},
    )
```

### ‘upload_to’ argument

- ImageField()의 upload_to 인자를 사용해 미디어 파일 추가 경로 설정

```python
# 1
image = models.ImageField(blank=True, upload_to='images/')

# 2
image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')

# 3
def articles_image_path(instance, filename):
	return f'images/{instance.user.username}/{filename}'

image = models.ImageField(blank=True, upload_to=articles_image_path)
```

### request.FILES가 두번재 위치 인자인 이유

- ModelForm 상위 클래스 BaseModelForm의 생성자 함수 키워드 인자

```python
class BaseModelForm(BaseForm):
	def __init__(self, data=None, **files=None**, auto_id='id_%s', prefix=None,
							 initial=None, error_class=ErrorList, label_suffix=None, 
               empty_permitted=False, instance=None, use_required_attribute=None,
               renderer=None):
```
