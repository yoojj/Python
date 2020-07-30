# Jupyter Notebook
: 소스 코드를 브라우저에서 실행하고 확인하는 대화식 환경 지원  


```bash
# 설치
$ conda install jupyter


# 실행
$ jupyter notebook
$ jupyter notebook --port 9999

## 브라우저없이 실행
$ jupyter notebook --no-browser


# 설치한 커널 목록 확인
$ jupyter kernelspec list

# C 커널 추가
$ pip install jupyter-c-kernel


# ipynb 파일 변환
$ jupyter nbconvert [파일명].ipynb --to script
$ jupyter nbconvert [파일명].ipynb --to pdf
```
