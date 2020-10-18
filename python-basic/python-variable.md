# Python Variable
: 변수 선언(declaration) 및 초기화 없음   
: 변수 할당(assignment)시 키/값을 생성하고 키가 존재하면 값을 업데이트함      
: 상수를 지원하지 않으나 python3.8부터 지원하는 final 키워드 통해 재할당 방지  
&nbsp; (https://www.python.org/dev/peps/pep-0591/)   


**변수 할당**

```python
# 키 = 값
num = 0

# 체인 할당
n1, n2, n3 = 1, 2, 3

# 언더스코어 사용
n1, *_ , n5 = (1, 2, 3, 4, 5)
n1 == 1

# id() : 객체의 id 값 반환  
n1 = n2 = 1
id(n1) == id(n2)
```


**변수 종류**

- 전역 변수
- 지역 변수
- 매개 변수

```python
# 전역 변수
num = 0

def func(str='매개 변수'):
    # 지역 변수 : 전역 변수와 지역 변수의 이름이 같아도 스코프가 다르므로 다른 변수로 취급
    num = 100
```



**변수 예약어**

- global
- nonlocal

```python
# global
num = 0

def func():
    # 함수 내부에서 global 키워드를 사용해 전역 변수 생성   
    global num
    num = 1

print(num == 0)  

func()
print(num == 1)  


# nonlocal
num = 0

def outer():
    num = 1
    print(num == 1)

    def inner():
        # 외부 함수의 변수에 영향을 미치며 전역 변수에 영향을 미치지 않음 
        nonlocal num
        num = 10

    inner()
    print(num == 10)

outer()
print(num == 0)
```



**변수 타입**   
: python3.5부터 패키지를 통해 타입 검사 지원   
&nbsp; (https://www.python.org/dev/peps/pep-0484/)

- typeshed
- MyPy
- PyType

```python
# variable_name : type

string: str = ""

numbers: List[int] = [1,2,3,4,5]
```



[top](#)
