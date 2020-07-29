# Python Function

1. 함수 선언
2. 메모리에 함수 객체 생성
3. 함수 객체를 가르키는 함수 레퍼런스 생성
4. 생성된 함수 레퍼런스를 통해 함수 사용


**종류**   
- 내장 함수
- 모듈 함수
- 사용자 정의 함수


```python
def 함수명(인자):
    실행 코드
    return 리턴 값


# 이름없는 한 줄 짜리 함수
lambda 인자: 실행 코드
lambda 인자1, 인자2: 실행 코드

# pass : 아무것도 하지 않는 함수
def func():
    pass
```


**return**    
- 함수 실행이 끝나면 호출한 곳으로 돌아감
- 모든 객체 값 리턴
- 여러개 값 리턴 가능하며 내부적으로 튜플로 묶임
- 값 리턴없이 종료를 위해서만 사용 가능
- 리턴이 없어도 구문이 끝나면 함수 종료


**parameter default value**

```python
def func(num=0):
    print(num)

func()
```


**arguments**   

```python
# *arguments -- tuple
def func(*args):
    print(args)


#  **keyword argument -- dictionary
def func(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}' .format(key, value))

func(num1=1, num2=2, num3=3)
```
