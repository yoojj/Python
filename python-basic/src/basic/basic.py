# 출력
print('출력')

var = '변수'
print(var, '출력')



# 입력 
string = input('글자 입력 :: ')
print(string)

num = eval(input('숫자 입력 :: '))
print(num)



# 포맷터
text = '포맷터'

print('%s 출력' %(text))        
print('{0} 출력' .format(text))
print('{0} {2} {1}'.format('이렇게', '가능', '순서 변경'))
print(f'{text} 출력')     
