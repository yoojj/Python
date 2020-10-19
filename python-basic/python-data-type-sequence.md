# Sequences Type
: 순서를 가진 요소들의 집합    
: 시퀀스의 인덱스를 통해 요소에 접근     


**Immutable**  
- [String](#string)
- [Tuple](#tuple)
- [Bytes](#bytes)

**Mutable**  
- List
- Byte Array


**sequence slicing**  

> [0:n-1:step]

범위 | 설명
---|---
[:]    | 0 ~ 마지막 요소 슬라이싱
[::2]  | 2칸 단위로 슬라이싱
[::-1] | 요소를 역으로 슬라이싱
[m:n]  | m ~ n 요소 슬라이싱
[:n]   | 0 ~ n 요소 슬라이싱
[m:]   | m부터 끝까지 요소 슬라이싱
[:-n]  | 0부터 시작해 끝에서 n번째 인덱스까지 요소 슬라이싱
[-:m]  | 끝에서 m번째부터 시작에 끝까지 요소 슬라이싱



## String


```python
line = ' '
line = " "
multiline = ''' '''


s = 'string'
print(s[0] == 's')
print(list(s))

print(s[-1] == 'g')
print(s[:3] == 'str')


print(s.encode('ascii'))
print(s.encode('utf-8'))
print(s.encode('utf-16'))


# format
print('{3} {4}' .format(1, 2, 3, 4, 5))


# f-string -- python3.6부터 지원
s = '변수'
print(f'{s} 출력')
```



## Bytes
: 바이트 배열을 담는 객체  

```
(input)              (output)
 bytes  -->  str  -->  bytes  
     decode()   encode()
```

```python
# 객체 생성
b = bytes(5)


b = b'byte'

print(b)
print(b[0] == 98)
print(list(b))
print(type(b))


s = 'string'
b = s.encode('utf_16')

print(b.decode('utf_16') == 'string')
```



## Tuple
: 값을 변경할 수 없는 객체가 순서대로 나열된 객체

```python
t = (1,2,3,4,5)

print(t)
print(type(t))
print(t[0] == 1)


# 주의
t = ()
print(type(t)) # tuple

not_tuple = (1)
print(type(not_tuple)) # int


# 튜플 삭제
t = (1,2,3,4,5)
del t
print(t) # NameError: name 't' is not defined
```



## List
: 값을 변경할 수 있는 객체가 순서대로 나열된 객체    
: + 연산자를 통해 객체를 연결해 새로운 객체 생성      
: * 연산자를 통해 객체를 반복해 새로운 객체 생성    

```python
l = []
print(type(l))


array = [1,2,3,4,5]

# 크기 반환
print(len(array) == 5)

# 요소 확인
print(5 in array)


# 연산자 사용
a = [1,2,3]
b = [4,5,6]

print(a + b)
print(a * b[0])
```



## Byte Array
: 바이트 배열을 담는 객체  

```python
# 객체 생성
b = bytearray(5)

print(b)
print(type(b))
```


[top](#)
