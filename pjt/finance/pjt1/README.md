# 실습 목표   
- 파이썬으로, 인터넷에 있는 날씨 정보 가져와, 내가 원하는 정보만 출력   
   
## 날씨 정보
- 직접 수집은 어려움
- api를 통해 인터넷에 있는 데이터를 가져와서 사용

## 전문용어 이해하기
### 서버
- 부탁을 받으면 처리해주거나, 부탁대로 원하는 값을 돌려주는 역할
### 클라이언트
- 부탁하는 역할

    <img src = "https://github.com/yuj1818/TIL/assets/95585314/1285c8dc-1bca-4981-8e58-e017eb743746" width="50%" height="50%">
    <img src = "https://github.com/yuj1818/TIL/assets/95585314/5c4fd2af-f08e-4a19-a542-fd2856fa578b" width="50%" height="50%">
    <img src = "https://github.com/yuj1818/TIL/assets/95585314/d989733d-ac8c-4343-b121-16e31d1beec5" width="50%" height="50%">
   
### 클라이언트는 어떻게 요청을 보낼 수 있는가?
- 브라우저의 주소를 입력
    - https://fakestoreapi.com/carts
- requests 라이브러리를 사용하여 요청
    - url: 요청을 보내는 서버 주소
    - requests: 해당 서버(url)에 데이터를 달라고 요청을 보내는 함수
    - json(): 내부 데이터를 json 형태로 변환해주는 함수
        ```python
        import requests

        url = 'https://fakestoreapi.com/carts'
        data = requests.get(url).json()
        print(data)
        ```

### 서버는 어떻게 요청을 해석할까
- API
    - 클라이언트가 원하는 기능을 수행하기 위해서 서버 측에 만들어 놓은 프로그램
    - 서버 측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 API를 미리 만들어 둠
    ![image.png](attachment:image.png)
    
## 오픈 API
- 외부에서 사용할 수 있도록 무료로 개방된 API
- 사용법은 공식 문서에 명시되어 있음
- 프로젝트에서 사용되는 API
    - [OpenWeatherMap API](https://openweathermap.org/api): 가상 데이터 및 날씨 정보를 제공하는 오픈 API
    - [금융상품통합비교공시 API](https://finlife.fss.or.kr/finlife/main/contents.do?menuNo=700029): 금융감독원에서 제공하는 금융 상품 정보를 제공하는 오픈 API
    
### 오픈 API 특징 및 주의사항
- 너무 많은 계정에서 동시에 요청을 보내면 서버가 견디지 못함
- 악용을 방지하기 위해 오픈 API는 API KEY를 활용하여 사용자를 확인
- 일부 오픈 API는 <span style="color:red">사용량이 제한</span>되어 있음(과금 주의!)

# 날씨 데이터 수집
## JSON(Javascript Object Notation)
- 자바 스크립트 객체 표기법
- 데이터를 저장하거나 전송할 때 많이 사용되는 <span style="color:red">경량의 텍스트 기반의 데이터 형식</span>
- 통신 방법이나 프로그래밍 문법이 아니라 단순히 데이터를 표현하는 표현 방법 중 하나
- 특징
    - 데이터는 중괄호({})로 둘러싸인 키-값 쌍의 집합
    - 키 = 문자열 / 값 = 다양한 데이터
    - 값은 쉼표(,)로 구분됨
### 예제
- 파싱(Parsing): 데이터를 의미 있는 구조로 분석하고 해석하는 과정
- json.loads(): JSON 형식의 문자열을 파싱하여 python Dictionary 로 변환
    ```python
    import json    # 내장 모듈

    # json 데이터
    json_data = '''
    {
        "name": "김싸피",
        "age": 28,
        "hobbies": [
            "공부하기",
            "복습하기"
        ]
    }
    '''

    data = json.loads(json_data)
    print(data)
    print(data['name'])
    ```
## Openweathermap API
- 기상 데이터 및 날씨 정보를 제공하는 API
- 전세계 날씨 데이터를 가져와 날씨, 일일 및 시간 별 예보 등 다양한 정보를 얻을 수 있음
- API 사용량 제한
    - 60 calls/minute
    - 1,000,000 calls/month
```python
# !pip install requests

import requests
import pprint

lat = 37.56

lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'

response = requests.get(url).json()
pprint.pprint(response)

city_name = 'Pusan, KR'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

response = requests.get(url).json()
pprint.pprint(response)

response = requests.get(url).json()
# 온도만
temp = response['main']['temp']
# 섭씨온도로 변환
temp -= 273.15

print('부산의 기온은 %.2f ℃입니다.' %(temp))
```