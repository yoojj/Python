# PEP8
Python Enhancement Proposal               
: 파이썬 코딩 스타일 가이드라인   

https://www.python.org/dev/peps/pep-0008/   


```bash

- 들여쓰기는 탭 사용 보다는 공백 4개 사용  
- 탭과 공백을 섞어서 사용 불가  
- 한 줄 글자 길이는 79자 이하로 작성   
- 튜플에서 후행 쉼표는 필수 사용이며 그 외는 선택 사용


# encoding  
- python2에서 ASCII 사용시 상단에 인코딩 선언 안함
- python2에서 UTF-8 사용시 상단에 인코딩 선언 필수
- python3에서 기본은 UTF-8 사용
- python3에서 UTF-8 사용시 파일 상단에 인코딩 선언 안함


# naming     
- protected 속성 :  _leading_underscore
- private 속성 : __double_leading_undersocre


# import  
- import 선언시 하나의 모듈만 선언
- import 순서는 표준 라이브러리, 서드파티, 로컬 라이브러리 순
```



[top](#)
