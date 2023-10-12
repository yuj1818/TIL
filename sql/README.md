# 데이터베이스

체계적인 데이터 모음

## 데이터

저장이나 처리에 효율적인 형태로 변환된 정보

### 기존의 데이터 저장 방식

- 파일 이용
    - 어디에서나 쉽게 사용 가능
    - 데이터를 구조적으로 관리하기 어려움
- 스프레드 시트를 이용
    - 테이블의 열과 행을 사용해 데이터를 구조적으로 관리 가능
    - 스프레드 시트의 한계
        1. 크기
            - 일반적으로 약 100만 행까지만 저장 가능
        2. 보안
            - 단순히 파일이나 링크 소유 여부에 따른 단순한 접근 권한 기능 제공
        3. 정확성
            1. 만약 공식적으로 강원의 지명이 강언으로 바뀌었다고 가정한다면?
            2. 이 변경으로 인해 테이블 모든 위치에서 해당 값을 업데이트 해야 함
            3. 찾기 및 바꾸기 기능을 사용해 바꿀 수 있지만 만약 데이터가 여러 시트에 분산되어 있다면 변경에 누락이 생기거나 추가 문제가 발생할 수 있음

### 데이터베이스의 역할

데이터를 저장하고 조작 

## Relational Database(관계형 데이터베이스)

- 데이터 간에 관계가 있는 데이터 항목들의 모음
- 테이블, 행, 열의 정보를 구조화하는 방식
- 서로 관련된 데이터 포인터를 저장하고 이에 대한 액세스를 제공
- `관계` : 여러 테이블 간의 (논리적) 연결
- 이 관계로 인해 두 테이블을 사용하여 데이터를 다양한 형식으로 조회할 수 있음
    - 특정 날짜에 구매한 모든 고객 조회
    - 지난 달에 배송일이 지연된 고객 조회

### 관계형 데이터베이스 예시

- 고객 테이블에서 고객 데이터 간 비교를 하기 위해서 어떻게 해야 하는가?
    
    
    | 이름 | 청구지 | 주소지 |
    | --- | --- | --- |
    | 김한웅 | 서울 | 강원 |
    | 박지수 | 경기 | 서울 |
    - 고유한 식별 값을 부여하기(기본 키, Primary Key)
        
        
        | id | 이름 | 청구지 | 주소지 |
        | --- | --- | --- | --- |
        | 1 | 김한웅 | 서울 | 강원 |
        | 2 | 박지수 | 경기 | 서울 |
- 주문 테이블, 고객 테이블이 존재할 때 누가 어떤 주문을 했는지 어떻게 식별할것인가?
    
    
    | id | 주문일 | 주문 상태 |
    | --- | --- | --- |
    | 1 | 2002/01/01 | 배송 완료 |
    | 2 | 2002/03/04 | 상품 준비중 |
    
    | id | 이름 | 청구지 | 주소지 |
    | --- | --- | --- | --- |
    | 1 | 김한웅 | 서울 | 강원 |
    | 2 | 박지수 | 경기 | 서울 |
    - 고객의 고유한 식별 값을 저장(외래 키, Foreign Key)
        
        
        | id | 주문일 | 주문 상태 | 고객 id |
        | --- | --- | --- | --- |
        | 1 | 2002/01/01 | 배송 완료 | 2 |
        | 2 | 2002/03/04 | 상품 준비중 | 1 |

### 관계형 데이터베이스 관련 키워드

#### Table(Relation)

- 행과 열을 사용하여 데이터를 기록하는 곳

#### Field(Column, Attribute)

- 각 필드에는 고유한 데이터 형식(타입)이 지정됨

#### Record(Row, Tuple)

- 각 레코드에는 구체적인 데이터 값이 저장됨

#### Database(Schema)

- 테이블의 집합

#### Primary Key(기본 키)

- 각 레코드의 고유한 값
- 관계형 데이터베이스에서 레코드의 식별자로 활용

#### Foreign Key(외래 키)

- 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
- 다른 테이블의 기본 키를 참조
- 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용

## DBMS(Database Management System)

- 데이터베이스를 관리하는 소프트웨어 프로그램
- 데이터 저장 및 관리를 용이하게 하는 시스템
- 데이터베이스와 사용자 간의 인터페이스 역할
- 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움

### RDBMS(Relational Database Management System)

- 관계형 데이터베이스를 관리하는 소프트웨어 프로그램
    - SQLite
        - 경량의 오픈 소스 데이터베이스 관리 시스템
        - 컴퓨터나 모바일 기기에 내장되어 간단하고 효율적인 데이터 저장 및 관리를 제공
    - MySQL
    - PostgreSQL
    - Oracle Database

# SQL(Structure Query Language)

- 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
- 테이블의 형태로 구조화된 관계형 데이터베이스에게 요청을 질의(요청)
- 관계형 데이터베이스와의 대활르 위해 사용하는 프로그래밍 언어

## SQL 표준

- SQL은 미국 국립 표준 협회(ANSI)와 국제 표준화 기구(ISO)에 의해 표준이 채택됨
- 모든 RDBMS에서 SQL 표준을 지원
- 다만 각 RDBMS마다 독자적인 기능에 따라 표준을 벗어나는 문법이 존재하니 주의

## SQL Syntax

```sql
SELECT column_name FROM table_name;
```

- SQL 키워드는 대소문자를 구분하지 않음
    - 하지만 대문자로 작성하는 것을 권장(명시적 구분)
- 각 SQL Statements의 끝에는 세미콜론(;)이 필요
    - 세미콜론은 각 SQL Statements를 구분하는 방법(명령어의 마침표)

## SQL Statements

- SQL을 구성하는 가장 기본적인 코드 블록
- 예시
    
    ```sql
    SELECT column_name FROM table_name;
    ```
    
    - 해당 예시 코드는 SELECT Statements라 부름
    - 이 Statement는 SELECT, FROM 2개의 keyword로 구성됨
- 수행 목적에 따라 4가지 유형으로 나뉨
    
    
    | 유형 | 역할 | SQL 키워드 |
    | --- | --- | --- |
    | DDL(Data Definition Language) | 데이터의 기본 구조 및 형식 변경 | CREATE, DROP, ALTER |
    | DQL(Data Query Language) | 데이터 검색 | SELECT |
    | DML(Data Manipulation Language) | 데이터 조작(추가, 수정, 삭제) | INSERT, UPDATE, DELETE |
    | DCL(Data Control Language) | 데이터 및 작업에 대한 사용자 권한 제어 | COMMIT, ROLLBACK |

`Query`

- 데이터베이스로부터 정보를 요청하는 것
- 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함

## Querying data(DQL)

### SELECT

- 테이블에서 데이터를 조회

```sql
SELECT
	select_list
FROM
	table_name;
```

- SELECT 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
- FROM 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정
- 예시
    - 테이블 employees에서 LastName 필드의 모든 데이터를 조회
    
    ```sql
    SELECT
    	LastName
    FROM
    	employees;
    ```
    
    - 테이블 employees에서 LastName, FirstName 필드의 모든 데이터 조회
    
    ```sql
    SELECT 
      LastName, FirstName
    FROM
      employees;
    ```
    
    - 테이블 employees에서 모든 필드 데이터를 조회
    
    ```sql
    # *(asterisk)를 사용하여 모든 필드 선택
    SELECT
      *
    FROM
      employees;
    ```
    
    - 테이블 employees에서 FirstName 필드의 모든 데이터를 조회(단, 조회 시 FirstName이 아닌 ‘이름’으로 출력 될 수 있도록 변경)
    
    ```sql
    SELECT
      FirstName as 이름
    FROM
      employees;
    ```
    
    - 테이블 tracks에서 Name, Milliseconds 필드의 모든 데이터 조회(단, Milliseconds필드는 60000으로 나눠 분 단위 값으로 출력)
    
    ```sql
    SELECT
      Name, Milliseconds/60000 AS '재생 시간(분)'
    FROM
      tracks;
    ```
    

## Sorting data(DQL)

### ORDER BY

- 조회 결과의 레코드를 정렬

```sql
SELECT
	select_list
FROM
	table_name
ORDER BY
	column1 [ASC|DESC],
	column2 [ASC|DESC],
	...;
```

- FROM clause 뒤에 위치
- 하나 이상의 컬럼을 기준으로 결과를 오름차순(ASC, default), 내림차순(DESC)으로 정렬
- 예시
    - 테이블 employees에서 FirstName 필드의 모든 데이터를 오름차순으로 조회
    
    ```sql
    SELECT
      FirstName
    FROM
      employees
    ORDER BY
      FirstName;
    ```
    
    - 테이블 employees에서 FirstName 필드의 모든 데이터를 내림차순으로 조회
    
    ```sql
    SELECT
      FirstName
    FROM
      employees
    ORDER BY
      FirstName DESC;
    ```
    
    - 테이블 customers에서 Country 필드를 기준으로 내림차순으로 정렬 한 다음 City 필드 기준으로 오름차순 정렬하여 조회
    
    ```sql
    SELECT
      Country, City
    FROM
      customers
    ORDER BY
      Country DESC,
      City;
    ```
    
    - 테이블 tracks에서 Milliseconds 필드를 기준으로 내림차순으로 정렬한 다음 Name, Milliseconds 필드의 모든 데이터를 조회(단, Milliseconds 필드는 60000으로 나눠 분 단위 값으로 출력)
    
    ```sql
    SELECT
      Name, Milliseconds/60000 AS '재생 시간(분)'
    FROM
      tracks
    ORDER BY
      Milliseconds DESC;
    ```
    

### 정렬에서의 NULL

- NULL 값이 존재할 경우, 오름차순 정렬 시 결과에 NULL이 먼저 출력

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/6f91b238-6c07-4d4c-b581-ae1bd3efa0e0)

### SELECT statement 실행 순서

- 테이블에서(FROM) → 조회하여(SELECT) → 정렬(ORDER BY)

## Filtering data(DQL)

- 관련 Keywords
    - Clause
        - DISTINCT
        - WHERE
        - LIMIT
    - Operator
        - BETWEEN
        - IN
        - LIKE
        - Comparison
        - Logical

### DISTINCT

- 조회 결과에서 중복된 레코드를 제거

```sql
SELECT DISTINCT
	select_list
FROM
	table_name;
```

- SELECT 키워드 바로 뒤에 작성해야 함
- SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정
- 예시
    - 테이블 customer에서 Country 필드의 모든 데이터를 중복없이 오름차순으로 조회
    
    ```sql
    SELECT DISTINCT
      Country
    FROM
      customers
    ORDER BY
      Country;
    ```
    

### WHERE

- 조회 시 특정 검색 조건을 지정

```sql
SELECT
	select_list
FROM
	table_name
WHERE
	search_condition;
```

- FROM clause 뒤에 위치
- search_condition은 비교연산자 및 논리연산자(AND, OR, NOT 등)를 사용하는 구문이 사용됨
- 예시
    - 테이블 customers에서 City 필드 값이 ‘Prague’인 데이터의 LastName, FirstName, City 조회
    
    ```sql
    SELECT
      LastName, FirstName, City
    FROM
      customers
    WHERE
      City = 'Prague';
    ```
    
    - 테이블 customers에서 City 필드 값이 ‘Prague’가 아닌 데이터의 LastName, FirstName, City 조회
    
    ```sql
    SELECT
      LastName, FirstName, City
    FROM
      customers
    WHERE
      City != 'Prague';
    ```
    
    - 테이블 customers에서 Company 필드 값이 NULL이고 Contry 필드 값이 ‘USA’인 데이터의 LastName, FirstName, Company, Country 조회
    
    ```sql
    SELECT
      LastName, FirstName, Company, Country
    FROM
      customers
    WHERE
      Company IS NULL AND Country = 'USA';
    ```
    
    - 테이블 customers에서 Company 필드 값이 NULL이거나 Country 필드 값이 ‘USA’인 데이터의 LastName, FirstName, Company, Country 조회
    
    ```sql
    SELECT
      LastName, FirstName, Company, Country
    FROM
      customers
    WHERE
      Company IS NULL OR Country = 'USA';
    ```
    
    - 테이블 tracks에서 Bytes 필드 값이 10000 이상 500000 이하인 데이터의 Name, Bytes 조회
    
    ```sql
    SELECT
      Name, Bytes
    FROM
      tracks
    WHERE
      Bytes BETWEEN 10000 and 500000;
    
    --WHERE
    --  10000 <= Bytes and Bytes <= 500000;
    ```
    
    - 테이블 tracks에서 Bytes 필드 값이 10000 이상 500000 이하인 데이터의 Name, Bytes을 Bytes를 기준으로 오름차순 조회
    
    ```sql
     SELECT
      Name, Bytes
    FROM
      tracks
    WHERE
      Bytes BETWEEN 10000 and 500000
    ORDER BY
      Bytes;
    ```
    
    - 테이블 customers에서 Country 필드 값이 ‘Canada’ 또는 ‘Germany’ 또는 ‘France’인 데이터의 LastName, FirstName, Country 조회
    
    ```sql
    SELECT
      LastName, FirstName, Country
    FROM
      customers
    WHERE
      Country IN ('Canada', 'Germany', 'France');
    ```
    
    - 테이블 customers에서 Country 필드 값이 ‘Canada’ 또는 ‘Germany’ 또는 ‘France’가 아닌 데이터의 LastName, FirstName, Country 조회
    
    ```sql
    SELECT
      LastName, FirstName, Country
    FROM
      customers
    WHERE
      Country NOT IN ('Canada', 'Germany', 'France');
    ```
    
    - 테이블 customers에서 LastName  필드 값이 son으로 끝나는 데이터의 LastName, FirstName 조회
    
    ```sql
    SELECT
      LastName, FirstName
    FROM
      customers
    WHERE
      LastName LIKE '%son';
    ```
    
    - 테이블 customers에서 FirstName 필드 값이 4자리면서 ‘a’로 끝나는 데이터의 LastName, FirstName 조회
    
    ```sql
    SELECT
      LastName, FirstName
    FROM
      customers
    WHERE
      FirstName LIKE '___a';
    ```
    

### Operators

#### Comparison Operators(비교 연산자)

- =
- ≥
- ≤
- ≠
- IS
- LIKE
    - 값이 특정 패턴에 일치하는지 확인
    - Wildcards와 함께 사용
        - % : 0개 이상의 문자열과 일치하는지 확인
        - _ : 단일 문자와 일치하는지 확인
- IN
    - 값이 특정 목록 안에 있는지 확인
- BETWEEN…AND

#### Logical Operators(논리 연산자)

- AND(&&)
- OR(||)
- NOT(!)

### LIMIT

- 조회하는 레코드 수를 제한

```sql
SELECT 
	select_list
FROM
	table_name
LIMIT [offset,] row_count;
```

- 하나 또는 두 개의 인자를 사용(0 또는 양의 정수)
- row_count는 조회하는 최대 레코드 수를 지정
- 예시
    - 테이블 tracks에서 TrackId, Name, Bytes 필드 데이터를 Bytes 기준 내림차순으로 7개만 조회
    
    ```sql
    SELECT
      TrackId, Name, Bytes
    FROM
      tracks
    ORDER BY
      Bytes DESC
    LIMIT 7;
    ```
    
    - 테이블 tracks에서 TrackId, Name, Bytes 필드 데이터를 Bytes 기준 내림차순으로 4번째부터 7번째 데이터만 조회
    
    ```sql
    SELECT
      TrackId, Name, Bytes
    FROM
      tracks
    ORDER BY
      Bytes DESC
    LIMIT 3, 4;
    ```
    

## Grouping data(DQL)

### GROUP BY

- 레코드를 그룹화하여 요약본 생성
- `집계 함수`와 함께 사용
    - 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
    - SUM, AVG, MAX, MIN, COUNT

```sql
SELECT
	c1, c2, ..., cn, aggregate_function(ci)
FROM
	table_name
GROUP BY
	c1, c2, ..., cn;

```

- FROM 및 WHERE 절 뒤에 배치
- GROUP BY 절 뒤에 그룹화 할 필드 목록을 작성
- 예시
    - Country 필드를 그룹화, 각 그룹에 대한 집계 값 계산
    
    ```sql
    SELECT
      Country, COUNT(*)
    FROM
      customers
    GROUP BY
      Country;
    ```
    
    - 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Bytes 평균 값을 내림차순 조회
    
    ```sql
    SELECT
      Composer, AVG(Bytes)
    FROM
      tracks
    GROUP BY Composer
    ORDER BY AVG(Bytes) DESC;
    
    --SELECT
    --  Composer, AVG(Bytes) as avgOfBytes
    --FROM
    --  tracks
    --GROUP BY Composer
    --ORDER BY avgOfBytes DESC;
    ```
    
    - 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Millisecondes의 평균 값이 10 미만인 데이터 조회(단, Milliseconds 필드는 60000으로 나눠 분 단위 값의 평균으로 계산)
    
    ```sql
    SELECT
      Composer, AVG(Milliseconds / 60000) as avgOfMinute
    FROM
      tracks
    GROUP BY
      Composer
    HAVING
      avgOfMinute < 10;
    
    # Having clause
    # 집계 항목에 대한 세부 조건을 지정
    # 주로 GROUP BY와 함께 사용되며 GROUP BY가 없다면 WHERE 처럼 동작
    ```
    

### SELECT statement 실행 순서

- 테이블에서(FROM) → 특정 조건에 맞추어(WHERE) → 그룹화 하고(GROUP BY) → 만약 그룹 중에서 조건이 있다면 맞추고(HAVING) → 조회하여(SELECT) → 정렬하고(ORDER BY) → 특정 위치의 값을 가져옴(LIMIT)

## Create a table(DDL)

- 테이블 생성

```sql
CREATE TABLE table_name (
	column_1 data_type constraints,
	column_2 data_type constratins,
	...,
);
```

- 각 필드에 적용할 데이터 타입 작성
- 테이블 및 필드에 대한 제약조건(contratins) 작성
- 예시
    - examples 테이블 생성 및 확인
    
    ```sql
    CREATE TABLE examples (
      ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
      LastName VARCHAR(50) NOT NULL,
      FirstName VARCHAR(50) NOT NULL
    );
    ```
    
    ![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/cc02bc91-a961-4a87-83e0-04aa379138e5)
    
    - 테이블 스키마(구조) 확인
    
    ```sql
    PRAGMA table_info('examples');
    ```
    
    ![Untitled 2](https://github.com/yuj1818/TIL/assets/95585314/8f5cd902-9881-40a4-b19d-db4a2860d887)
    

### 데이터 타입

![Untitled 3](https://github.com/yuj1818/TIL/assets/95585314/ab5469d1-9856-4e9c-8566-15ee90dcbe0b)

- NULL
    - 아무런 값도 포함하지 않음을 나타냄
- INTEGER
    - 정수
- REAL
    - 부동 소수점
- TEXT
    - 문자열
- BLOB
    - 이미지, 동영상, 문서 등의 바이너리 데이터

### 제약 조건(Constraints)

![Untitled 4](https://github.com/yuj1818/TIL/assets/95585314/cd936039-f7e5-4471-adc7-49f9fce91f1a)

- 테이블의 필드에 적용되는 규칙 또는 제한 사항
- 데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장
- PRIMARY KEY
    - 해당 필드를 기본 키로 지정
    - **INTEGER 타입에만 적용되며 INT, BIGINT 등과 같은 정수 유형은 적용되지 않음**
- NOT NULL
    - 해당 필드에 NULL 값을 허용하지 않도록 지정
- FOREIGN KEY
    - 다른 테이블과의 외래 키 관계를 정의

### AUTOINCREMENT 키워드

![Untitled 5](https://github.com/yuj1818/TIL/assets/95585314/5798294d-8364-4cab-9fac-f48549b496a8)

- 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성
- 필드의 자동 증가를 나타내는 특수한 키워드
- 주로 PRIMARY KEY 필드에 적용
- INTEGER PRIMARY KEY AUTOINCREMENT가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값을 할당
- 삭제된 값을 무시되며 재사용할 수 없게 됨

## Modifying table fields(DDL)

### ALTER

- 테이블 및 필드 조작

| 명령어 | 역할 |
| --- | --- |
| ALTER TABLE ADD COLUMN | 필드 추가 |
| ALTER TABLE RENAME COLUMN | 필드 이름 변경 |
| ALTER TABLE DROP COLUMN | 필드 삭제 |
| ALTER TABLE RENAME TO | 테이블 이름 변경 |

#### ADD COLUMN

```sql
ALTER TABLE
	table_name
ADD COLUMN
	column_definition;
```

- ADD COLUMN 키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성
- 예시
    - examples 테이블에 다음 조건에 맞는 Country 필드 추가
    
    ```sql
    ALTER TABLE 
      examples
    ADD COLUMN 
      Country VARCHAR(100) NOT NULL;
    ```
    
    - exampels 테이블에 다음 조건에 맞는 Age, Address 필드 추가
    
    ```sql
    ALTER TABLE examples
    ADD COLUMN Age INTEGER NOT NULL;
    
    ALTER TABLE examples
    ADD COLUMN Address VARCHAR(100) NOT NULL;
    ```
    

#### RENAME COLUMN

```sql
ALTER TABLE
 table_name
RENAME COLUMN
	current_name TO new_name
```

- RENAME COLUMN 키워드 뒤에 이름을 바꾸려는 필드의 이름을 지정하고 TO 키워드 뒤에 새 이름을 지정
- 예시
    - examples 테이블 Address 필드의 이름을 PostCode로 변경
    
    ```sql
    ALTER TABLE
    	examples
    RENAME COLUMN
    	Address TO PostCode;
    ```
    

#### DROP COLUMN

```sql
ALTER TABLE
	table_name
DROP COLUMN
	current_name
```

- DROP COLUMN 키워드 뒤에 삭제하려는 필드의 이름을 지정
- 삭제하는 필드가 다른 부분에서 참조되지 않고 PRIMARY KEY가 아니며 UNIQUE 제약 조건이 없는 경우에만 작동
- 예시
    - examples 테이블의 PostCode 필드를 삭제
    
    ```sql
    ALTER TABLE
    	examples
    DROP COLUMN
    	PostCode;
    ```
    

#### RENAME TO

```sql
ALTER TABLE
	table_name
RENAME TO
	new_table_name;
```

- RENAME TO 키워드 뒤에 새로운 테이블 이름 지정
- 예시
    - examples 테이블 이름을 new_examples로 변경
    
    ```sql
    ALTER TABLE
    	examples
    RENAME TO
    	new_examples;
    ```
    

## Delete a table(DDL)

### DROP TABLE

- 테이블 삭제

```sql
DROP TABLE table_name;
```

- DROP TABLE statement 이후 삭제할 테이블 이름 작성
- 예시
    - examples 테이블 삭제
    
    ```sql
    DROP TABLE examples;
    ```
    

## Insert data(DML)

### INSERT

- 테이블 레코드 삽입

```sql
INSERT INTO table_name (c1, c2, ...)
VALUES (v1, v2, ...);
```

- INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록 작성
- VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록 작성
- 예시
    - 실습 테이블 생성
    
    ```sql
    CREATE TABLE articles(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title VARCHAR(100) NOT NULL,
      content VARCHAR(200) NOT NULL,
      createdAt DATE NOT NULL
    );
    ```
    
    - articles 테이블에 다음과 같은 데이터 입력
    
    | title | content | createdAt |
    | --- | --- | --- |
    | hello | world | 2000-01-01 |
    
    ```sql
    INSERT INTO articles (title, content, createdAt)
    VALUES ('hello', 'world', '2000-01-01');
    ```
    
    - articles 테이블에 다음과 같은 데이터 추가 입력
    
    | title | content | createdAt |
    | --- | --- | --- |
    | title1 | content1 | 1900-01-01 |
    | title2 | content2 | 1800-01-01 |
    | title3 | content3 | 1700-01-01 |
    
    ```sql
    INSERT INTO articles (title, content, createdAt)
    VALUES
      ('title1', 'content1', '1900-01-01'),
      ('title2', 'content2', '1800-01-01'),
      ('title3', 'content3', '1700-01-01');
    ```
    
    - DATE 함수를 사용해 articles 테이블에 다음과 같은 데이터 추가 입력
    
    | title | content | createdAt |
    | --- | --- | --- |
    | mytitle | mycontent | 2023-10-10(오늘날짜) |
    
    ```sql
    INSERT INTO articles (title, content, createdAt)
    VALUES ('mytitle', 'mycontent', DATE());
    ```
    

## Update data(DML)

### UPDATE

- 테이블 레코드 수정

```sql
UPDATE table_name
SET column_name = expression,
[WHERE
	condition];
```

- SET 절 다음에 수정 할 필드와 새 값을 지정
- WHERE 절에서 수정 할 레코드를 지정하는 조건 작성
- WHERE 절을 작성하지 않으면 모든 레코드를 수정
- 예시
    - articles 테이블 1번 레코드의 title 필드 값을 ‘update Title’로 변경
    
    ```sql
    UPDATE articles
    SET title = 'update Title'
    WHERE id = 1;
    ```
    
    - articles 테이블 2번 레코드의 title, content 필드 값을 각각 ‘update Title’, ‘update Content’로 변경
    
    ```sql
    UPDATE articles
    SET title = 'update Title', content = 'update Content'
    WHERE id = 2;
    ```
    

## Delete data(DML)

### DELETE

- 테이블 레코드 삭제

```sql
DELETE FROM table_name
[WHERE
	condition];
```

- DELETE FROM 절 다음에 테이블 이름 작성
- WHERE 절에서 삭제할 레코드를 지정하는 조건 작성
- WHERE 절을 작성하지 않으면 모든 레코드를 삭제
- 예시
    - articles 테이블의 1번 레코드 삭제
    
    ```sql
    DELETE FROM articles
    WHERE id = 1;
    ```
    
    - articles 테이블에서 작성일이 오래된 순으로 레코드 2개 삭제
    
    ```sql
    DELETE FROM articles
    WHERE id in (
      SELECT id FROM articles
      ORDER BY createdAt
      LIMIT 2
    );
    ```
    

## Join

### 관계

- 여러 테이블 간의 (논리적) 연결

### 관계의 필요성

- 커뮤니티 게시판에 필요한 데이터 생각해보기
    - id, title, content, writer, role
- 특정 writer를 기준으로 게시글을 조회한다면 동명이인이 존재할 때, 혹은 특정 데이터가 수정되었을 때 문제 발생
- 그러므로, 테이블을 나누어서 분류
    - 예) articles, users, roles
- articles와 users 테이블에 각각 userrId, roleId 외래 키 필드 작성
    - 관리자인 사람만 보고 싶다면 roleId 기반으로 조회
    - 사용자가 이름을 바꾸면 users에서 한번만 변경하면 자동으로 모두 변경

### JOIN이 필요한 순간

- 테이블을 분리하면 데이터 관리는 용이해질 수 있으나 출력시에는 문제가 있음
- 테이블 한 개 만을 출력할 수 밖에 없어 다른 테이블과 결합하여 출력하는 것이 필요해짐

## Joining tables

### JOIN

- 둘 이상의 테이블에서 데이터를 검색하는 방법

<aside>
💡 실습 데이터 준비

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId)
    REFERENCES users(id)
);

INSERT INTO
  users (name)
VALUES
  ('하석주'), ('송윤미'), ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);
```

</aside>

### JOIN의 종류

- INNER JOIN
    - 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
    
    ```sql
    SELECT select_list FROM table_a
    INNER JOIN table_b ON table_b.fk = table_a.pk;
    ```
    
    - FROM 절 이후 메인 테이블 지정 (table_a)
    - INNER JOIN 절 이후 메인 테이블과 조인할 테이블을 지정 (table_b)
    - ON 키워드 이후 조인 조건을 작성
    - 조인 조건은 table_a과 table_b 간의 레코드를 일치시키는 규칙을 지정
    - 예시
        - 1번 회원(하석주)가 작성한 모든 게시글의 제목과 작성자명을 조회
        
        ```sql
        SELECT articles.title, users.name FROM articles
        INNER JOIN users
          ON users.id = articles.userId
        WHERE users.id = 1;
        ```
        
- LEFT JOIN
    - 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
    
    ```sql
    SELECT
    	select_list
    FROM
    	table_a
    LEFT JOIN table_b
    	ON table_b.fk = table_a.pk;
    ```
    
    - FROM 절 이후 왼쪽 테이블 지정 (table_a)
    - LEFT JOIN 절 이후 오른쪽 테이블 지정 (table_b)
    - ON 키워드 이후 조인 조건을 작성
        - 왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴
    - 왼쪽은 테이블의 모든 레코드를 표기
    - 오른쪽 테이블과 매칭되는 레코드가 없으면 NULL을 표시
    - 예시
        - 게시글을 작성한 이력이 없는 회원 정보 조회
        
        ```sql
        SELECT * FROM users
        LEFT JOIN articles
        	ON articles.userId = users.id
        WHERE articles.userId IS NULL;
        ```
        
## Many to one relationships - N : 1 or 1 : N

- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
- 예시
    - comment(N) - article(1)
        - 0개 이상의 댓글은 1개의 게시글에 작성 될 수 있다.
        
        ![Untitled 7](https://github.com/yuj1818/TIL/assets/95585314/575b891a-8d94-485a-8f52-8a947be10887)
        

### ForeignKey(to, on_delete)

- N:1 관계 설정 모델 필드
- to
    - 참조하는 모델 class 이름
- on_delete
    - 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정(데이터 무결성)
    - CASCADE
        - 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
        - 기타 설정 값 참고
            - [https://docs.djangoproject.com/en/4.2/ref/models/fields/#arguments](https://docs.djangoproject.com/en/4.2/ref/models/fields/#arguments)

### 댓글 모델 구현

#### 댓글 모델 정의

- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형으로 작성하는 것을 권장
- ForeignKey 클래스를 작성하는 위치와 관계없이 외래 키는 테이블 필드 마지막에 생성됨

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### Migration

- 댓글 테이블의 article_id 필드 확인
- 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장 되었던 이유
    - ‘참조 대상 클래스 이름’ + ‘_’ + ‘클래스 이름’

### 댓글 생성 연습

```bash
# 게시글 작성
Articles.objects.create(title='title', content='content')

# Comment 클래스의 인스턴스 comment 생성
comment = Comment()

# 인스턴스 변수 저장
comment.content = 'first content'

# DB에 댓글 저장
comment.save()

# 에러 발생
# articles_comment 테이블의 ForeignField, article_id 값이 저장 시 누락되었기 때문

# 게시글 조회
article = Article.objects.get(pk=1)

# 외래 키 데이터 입력
comment.article = article

# 댓글 저장 및 확인
comment.save()

# 두번째 댓글 작성
comment = Comment(content='second comment', article=article)
comment.save()

```

### 관계 모델 참조

#### 역참조

- N:1 관계에서 1에서 N을 참조하거나 조회하는 것(1 → N)
- N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만 1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 이름이 필요
- article.comment_set.all()
    - article - 모델 인스턴스
    - comment_set - related manager(역참조 이름)
    - all() - QuerySet API

#### related manager

- N:1 혹은 M:N 관계에서 역참조 시에 사용하는 매니저
- ‘objects’ 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨
- 이름 규칙
    - N:1 관계에서 생성되는 Related manager의 이름은 참조하는 “모델명_set” 이름 규칙으로 만들어짐
    - 해당 댓글의 게시글(Comment → Article)
        - comment.article
    - 게시글의 댓글 목록(Article → Comment)
        - article.comment_set.all()

```bash
# 1번 게시글 조회
article = Article.objects.get(pk=1)

# 1번 게시글에 작성된 모든 댓글 조회하기
article.comment_set.all()

# 1번 게시글에 작성된 모든 댓글 내용 출력
comments = article.comment_set.all()

for comment in comments:
	print(comment.content)
```

### 댓글 구현

#### 댓글 CREATE

- 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 정의
    
    ```python
    # articles/forms.py
    
    from django import forms
    from .models import Article, Comment
    
    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = '__all__'
    ```
    
- detail view 함수에서 CommentForm을 사용하여 detail 페이지에 렌더링
    
    ```python
    # articles/views.py
    
    form .forms import ArticleForm, CommentForm
    
    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm()
        context = {
            'article': article,
            'comment_form': comment_form,
        }
        return render(request, 'articles/detail.html', context)
    ```
    
    ```html
    <form action="#" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
    ```
    
- Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요한 필드이기 때문에 위와 같이 작성하면 article 입력 form까지 출력 됨
- 하지만, 외래 키 필드는 사용자 입력 값으로 받는 것이 아닌 view 함수 내에서 다른 방법으로 전달 받아 저장되어야 함
- CommentForm의 출력 필드 조정
    
    ```python
    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ('content',)
    ```
    
    - 출력에서 제외된 외래 키 데이터는 어디서 받아와야 하는가?
        - detail 페이지의 url path(’<int:pk>/’, views.detail, name=’detail’) 에서 해당 게시글의 pk 값이 사용되고 있음
        - 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk값
- url 작성 및 action 값 작성
    
    ```python
    # articles/urls.py
    urlpatterns = [
        ... ,
        path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    ]
    ```
    
    ```html
    <!-- articles/detail.html -->
    <form action="{% url "articles:comments_create" article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
    ```
    
- comments_create view 함수 정의
    
    ```python
    # articles/views.py
    
    def comments_create(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('articles:detail', article.pk)
        context = {
            'article': article,
            'comment_form': comment_form,
        }
        return render(request, 'articles/detail.html', context)
    ```
    
- save의 commit 인자를 활용해 외래 키 데이터 추가 입력
    - `save(commit=False)`
        - DB에 저장하지 않고 인스턴스만 반환
        - Create, but don’t save the new instance
    
    ```python
    # articles/views.py
    
    def comments_create(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
    				comment.article = article
    				comment_form.save()
            return redirect('articles:detail', article.pk)
        context = {
            'article': article,
            'comment_form': comment_form,
        }
        return render(request, 'articles/detail.html', context)
    ```
    

#### 댓글 READ

- detail view 함수에서 전체 댓글 데이터를 조회
    
    ```python
    # articles/views.py
    
    from .models import Article, Comment
    
    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm()
        comments = article.comment_set.all()
        context = {
            'article': article,
            'comment_form': comment_form,
            'comments': comments,
        }
        return render(request, 'articles/detail.html', context)
    ```
    
- 전체 댓글 출력 및 확인
    
    ```html
    <!-- articles/detail.html -->
    
    <h4>댓글 목록</h4>
    <ul>
      {% for comment in comments %}
        <li>{{ comment.content }}</li>
      {% endfor %}
    </ul>
    ```
    

#### 댓글 DELETE

- 댓글 삭제 url 작성
    
    ```python
    # article/urls.py
    
    urlpatterns = [
        ... ,
        path('<int:article_pk>/comments/<int:comment_pk>/delete/',
             views.comments_delete,
             name='comments_delete'
        ),
    ]
    ```
    
- 댓글 삭제 view 함수 정의
    
    ```python
    # articles/views.py
    
    def comments_delete(request, article_pk, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)
    ```
    
- 댓글 삭제 버튼 작성
    
    ```html
    <!-- articles/detail.html -->
    
    <h4>댓글 목록</h4>
    <ul>
      {% for comment in comments %}
        <li>
          {{ comment.content }}
          <form action="{% url "articles:comments_delete" article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="DELETE">
          </form>
        </li>
      {% endfor %}
    </ul>
    ```

### Article(N) - User(1)

- 0개 이상의 게시글은 1명의 회원에 의해 작성 될 수 있다.

#### Article-User 모델 관계 설정

```python
# articles/models.py

from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- User 모델을 참조하는 2가지 방법
    - django 프로젝트의 ‘내부적인 구동 순서’와 ‘반환 값’에 따른 이유
    - **User 모델은 직접 참조하지 않는다**
    
    |  | get_user_model() | settings.AUTH_USER_MODEL |
    | --- | --- | --- |
    | 반환 값 | User Object(객체) | accounts.User(문자열) |
    | 사용 위치 | models.py가 아닌 다른 모든 위치 | models.py |

#### Migration

![Untitled 7](https://github.com/yuj1818/TIL/assets/95585314/b94edbe9-8d31-4f5c-9f77-ea411ec291b0)

- 기본적으로 모든 컬럼은 NOT NULL 제약조건이 있기 때문에 데이터 없이는 새로운 필드가 추가되지 못함
    - 기본값 설정 필요
- 1을 입력하고 Enter 진행

![Untitled 8](https://github.com/yuj1818/TIL/assets/95585314/775c069b-acf4-4151-96a6-ba9f4597a7c2)

- 추가되는 외래 키 user_id에 어떤 데이터를 넣을 것인지 직접 입력해야 함
- 마찬가지로 1 입력하고 Enter 진행
- 그러면 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리됨

```bash
python manage.py migrate
```

- migrations 파일 생성 후 migrate 진행
- article 테이블의 user_id 필드 생성 확인

#### 게시글 CREATE

- 기존 ArticleForm 출력 변화 확인
- User 모델에 대한 외래 키 데이터 입력을 위해 불필요한 input이 출력
- ArticleForm 출력 필드 수정

```python
# articles/forms.py

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)
```

- 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용

```python
# articles/views.py

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
			...
```

#### 게시글 READ

- 각 게시글의 작성자 이름 출력

```html
<!-- articles/index.html -->

{% for article in articles %}
  <p>작성자 : {{ article.user }}</p>
  <p>글 번호 : {{ article.pk }}</p>
  <a href="{% url "articles:detail" article.pk %}">
    <p>글 제목 : {{ article.title }}</p>
  </a>
  <p>글 내용 : {{ article.content }}</p>
  <hr>
{% endfor %}
```

```html
<!-- articles/detail.html -->

<h2>DETAIL</h2>
<h3>{{ article.pk }} 번째 글</h3>
<hr>
<p>작성자 : {{ article.user }}</p>
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>작성 시각: {{ article.created_at }}</p>
<p>수정 시각: {{ article.updated_at }}</p>
```

#### 게시글 UPDATE

- 게시글 수정 요청 사용자와 게시글 작성 사용자를 비교하여 본인의 게시글만 수정할 수 있도록 하기

```python
# articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid:
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

- 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 하기

```html
<!-- articles/detail.html -->

{% if request.user == article.user %}
  <a href="{% url "articles:update" article.pk %}">UPDATE</a>
  <form action="{% url "articles:delete" article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
  </form>
{% endif %}
```

#### 게시글 DELETE

- 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 하기

```python
# articles/views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')
```

### Comment(N) - User(1)

- 0개 이상의 댓글은 1명의 회원에 의해 작성 될 수 있다.

#### Comment-User 모델 관계 설정

- User 외래 키 정의

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### Migration

- 이전에 Article와 User 모델 관계 설정 때와 동일한 상황
- 기존 Comment 테이블에 새로운 컬럼이 빈 값으로 추가될 수 없기 때문에 기본 값 설정 과정 필요

#### 댓글 CREATE

- 댓글 작성 시 작성자 정보가 함께 저장될 수 있도록 작성

```python
# articles/views.py

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment_form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

#### 댓글 READ

- 댓글 출력 시 댓글 작성자와 함께 출력

```html
<!-- articles/detail.html -->

{% for comment in comments %}
  <li>
    {{ comment.user}} - {{ comment.content }}
    <form action="{% url "articles:comments_delete" article.pk comment.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="삭제">
    </form>
  </li>
{% endfor %}
```

#### 댓글 DELETE

- 댓글 삭제 요청 사용자와 댓글 작성 사용자를 비교하여 본인의 댓글만 삭제할 수 있도록 하기

```python
# articles/views.py

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
```

- 해당 댓글의 작성자가 아니라면, 댓글 삭제 버튼을 출력하지 않도록 함

```html
<!-- articles/detail.html -->

{% if request.user == comment.user %}
  <form action="{% url "articles:comments_delete" article.pk comment.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
  </form>
{% endif %}
```

## 참고

### 타입 선호도(Type Affinity)

- 컬럼에 데이터 타입이 명시적으로 지정되지 않았거나 지원하지 않을 때 SQLite가 자동으로 데이터 타입을 추론하는 것
    - [https://www.sqlite.org/datatype3.html](https://www.sqlite.org/datatype3.html)
- 타입 선호도 목적
    - 유연한 데이터 타입 지원
        - 데이터 타입을 명시적으로 지정하지 않고도 데이터를 저장하고 조회할 수 있음
        - 컬럼에 저장되는 값의 특성을 기반으로 데이터 타입을 유추
    - 간편한 데이터 처리
        - INTEGER Type Affinity를 가진 열에 문자열 데이터를 저장해도 SQLite는 자동으로 숫자로 변환하여 처리
    - SQL 호환성
        - 다른 데이터베이스 시스템과 호환성을 유지

### 반드시 NOT NULL 제약을 사용해야 하는가?

- 반드시는 아님
- 하지만 데이터베이스를 사용하는 프로그램에 따라 NULL을 저장할 필요가 없는 경우가 많으므로 대부분 NOT NULL을 정의
- “값이 없다” 라는 표현을 테이블에 기록하는 것을 ‘0’이나 ‘빈 문자열’ 등을 사용하는 것으로 대체하는 것을 권장

### SQLite의 날짜와 시간

- SQLite에는 날짜 및/또는 시간을 저장하기 위한 별도 데이터 타입이 없음
- 대신 날짜 및 시간에 대한 함수를 사용해 표기 형식에 따라 TEXT, REAL, INTEGER 값으로 저장
- [https://www.sqlite.org/datatype3.html](https://www.sqlite.org/datatype3.html)

### admin site 등록

- Comment 모델을 admin site에 등록해 CRUD 동작 확인하기

```python
# articles/admin.py

from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
```

### 댓글이 없는 경우 대체 콘텐츠 출력

- DTL ‘for empty’ 태그 사용

```html
<!-- articles/detail.html -->

<h4>댓글 목록</h4>
<ul>
  {% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action="{% url "articles:comments_delete" article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    </li>
  {% empty %}
    <p>댓글이 없어요</p>
  {% endfor %}
</ul>
```

### 댓글 개수 출력하기

- DTL filter - ‘length’ 사용

```html
{{ comments|length }}

{{ article.comment_set.all|length }}
```

- QuerysetAPI - ‘count()’ 사용

```html
{{ article.comment_set.count }}
```

### 인증된 사용자만 댓글 작성 및 삭제

```python
# articles/views.py

@login_required
def comments_create(request, pk):
	pass

@login_required
def comments_delete(request, article_pk, comment_pk):
	pass
```