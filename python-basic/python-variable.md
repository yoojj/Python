# Python Variable
: 변수 선언 및 초기화 없음  
: 변수 할당시 키-값을 생성하고 키가 존재하면 값을 업데이트함      


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
    # 지역 변수 : 전역 변수와 지역 변수의 이름이 같아도 스코프가 다르기 때문에 다른 변수
    num = 100
```



**변수 예약어**

- global
- nonlocal

```python
num = 0

def func():
    # 함수 내부에서 global 키워드를 사용해 전역 변수 생성   
    global num
    num = 1

print(num == 0)  

func()
print(num == 1)  
```



[top](#)
