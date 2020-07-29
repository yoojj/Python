# PEP8           
: 파이썬 코딩 스타일 가이드라인   

https://www.python.org/dev/peps/pep-0008/   


**PEP**    
Python Enhancement Proposal        
: 파이썬 개선 제안서


```bash

# whitespace
- 들여쓰기는 탭 사용보다 공백 4개를 사용  
- 탭과 공백을 섞어서 사용 불가  
- 변수 할당 앞 뒤에 공백 1개 사용   
- 리스트 인덱스, 함수 호출, 키워드 인수 할당에는 공백을 사용하지 않음
- 메서드는 빈 줄 하나로 구분
- 함수와 클래스는 빈 줄 두 개로 구분
- 한 줄 글자 길이는 79자 이하로 작성   


# encoding  
- python2에서 ASCII 사용시 상단에 인코딩 선언 안함
- python2에서 UTF-8 사용시 상단에 인코딩 선언 필수
- python3에서 기본은 UTF-8 사용
- python3에서 UTF-8 사용시 파일 상단에 인코딩 선언 안함


# naming     
- protected 속성 | _leading_underscore
- private 속성   | __double_leading_undersocre


# import  
- import 선언시 하나의 모듈만 선언
- import 순서는 표준 라이브러리, 서드파티, 로컬 라이브러리 순
```



[top](#)
