C++로 작성된 오픈소스 문서 지향(Document-Oriented) 적 Cross-platform DB

Not Only SQL

### Document?

한 개 이상의 key-value pair로 이루어져 있다

RDMS의 record와 비슷한 개념 

Dynamic Schema를 가지고 있다. 같은 Collection 내 Document 끼리 다른 Schema를 가지고 있을 수 있다.

### Collections?

Document의 상위 레이어에 위치, Document의 그룹이다.

RDMS의 table과 비슷한 개념이지만, schema를 따로 가지지 않는다.

### 몽고디비 뿌수는 설명서

[Mongodb | VELOPERT.LOG](https://velopert.com/category/dev-log/tech-log/mongodb)

### Docker-Compose 로 몽고디비

[Mongodb를 Docker Container로 띄우기](https://basketdeveloper.tistory.com/34)
[Docker에서 MongoDB 설치하기](https://elfinlas.github.io/2019/02/11/docker-on-mongo/)

### Compass ( MySQL WorkBench와 같은 것 )
[설명서](https://docs.ncloud.com/ko/database/database-10-5.html)

### Code Structure
- Docker : 도커 컴포즈 코드 ( yaml )
- Test : 연결 테스트
- Tutorials_W3school : W3school 예제 코드 따라한 코드
- Uploader : CSV 파일을 MongoDB로 업로드
- MLLoader : Pytorch DataLoader (딥러닝용)