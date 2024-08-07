# HTTP/HTTPS

## HTTP(HyperText Transfer Protocol)

- 인터넷 상에서 클라이언트와 서버가 데이터를 주고 받기 위한 통신 규약
- 상태 정보를 저장하지 않음(stateless)
- 클라이언트의 요청에 맞는 응답을 보낸 후 연결을 끊음(connectionless)
- 통신 간의 연결 상태 처리나 상태 정보를 관리할 필요가 없어 서버 디자인이 간단
- 각각의 HTTP 요청에 독립적으로 응답만 보낼 수 있음
- 이전 통신의 정보를 모르기 때문에 매번 인증이 필요
- 위의 문제를 해결하기 위해 쿠키나 세션을 사용하여 데이터를 처리
- 텍스트 교환이므로 정보를 주고 받을 때 제 3자에 의해 조회 될 수 있는 보안 이슈가 존재

## HTTPS(HyperText Transfer Protocol Secure)

- 인터넷 상에서 정보를 암호화하는 `SSL` 프로토콜을 사용하여 클라이언트와 서버가 데이터를 주고 받도록 하는 통신 규약
- 텍스트를 암호화하여 보냄
- HTTP는 SSL과 SSL은 TCP와 통신함으로써 암호화와 증명서, 안전성 보호 가능
- `SSL(Secure Socket Layer)` : 인터넷을 통해 전달되는 정보를 보호하기 위해 개발한 통신 규약