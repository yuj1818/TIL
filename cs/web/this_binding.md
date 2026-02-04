# Javascript에서의 this 바인딩

## this

- 코드 조각이 실행되는 컨텍스트
- **함수가 호출될 때 결정되는 참조 값**
- this의 값은 함수가 **어떤 방식으로 호출(binding) 되었는지**에 따라 달라짐

## this 바인딩

- this라는 식별자에 가리키는 객체의 주소 값을 매핑하는 것

### new 바인딩

```jsx
function Person(name) {
	this.name = name;
}

const p = new Person("으아아악");
console.log(p.name); // 으아아악
```

- 생성자를 이용하여 생성할 객체에 대한 참조로 this를 사용
- `new` 를 붙이면 this는 **새로 만들어진 객체에 바인딩**

### 명시적 바인딩 (call/apply/bind)

```jsx
function hello() {
	console.log(this.name);
}

const user = { name: "으아아악" };

hello.call(user); // 으아아악
```

- `call`, `apply`, `bind`를 사용하여 **내가 명시한 객체에 바인딩**

### 암시적 바인딩

```jsx
const user = {
	name: "으아아악",
	hello() {
		console.log(this.name);
	}
};

user.hello(); // 으아아악
```

- 함수가 객체의 메서드로서 호출되는 상황에서 this가 바인딩 되는 것
- `obj.method()`
- this는 해당 함수를 **호출한 객체(컨텍스트 객체)에 바인딩**

> [!NOTE]
> 암시적 바인딩이 소실되는 경우
> - 콜백 함수의 매개변수로 메서드 함수가 전달 되는 경우, 바인딩이 소실되어 기본 바인딩과 같이 취급
> - 콜백 함수 내부에서 this는 더 이상 객체(위의 예시에서는 user)를 바라보지 않음

### 기본 바인딩 (나머지 전부)

```jsx
function hello() {
	console.log(this)
}

hello();
// strict mode => undefined
// non-strict => 브라우저 환경: window, Node 환경: global
```

- 기본 바인딩이 적용될 경우 this는 **전역 객체에 바인딩**
- 브라우저에서는 `window` , Node 에서는 `global` 객체를 가리킨다

### 화살표 함수

```jsx
const obj = {
  name: "으아아악",
  foo() {
    setTimeout(() => {
      console.log(this.name);
    }, 1000);
  }
};

obj.foo(); // 으아아악
```

- **화살표 함수 선언 당시의 Lexical Scope에 있는 this를 참조**
    - 화살표 함수는 자신만의 this를 가지지 않는다
    - 위의 예시에서 콜백 함수를 화살표 함수로 선언시에 this는 obj 객체를 가리키고 있다
- `call`, `apply`, `bind`, `new`로 오버라이드 불가능
- 콜백 함수로 사용할 때 유용

## 정리

> Javascript의 this는 함수가 선언된 위치가 아닌 어떤 방식으로 호출되었는지에 따라 동적으로 결정됨
> 대표적으로 new, 명시적, 암시적, 기본 바인딩 규칙이 있고 화살표 함수는 렉시컬 this를 사용