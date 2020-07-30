# Python
: 명령형 프로그래밍 언어인 ABC의 영향을 받은 프로그래밍 언어    
: 멀티 패러다임 언어 (명령형, 함수형, 객체 지향)        
: 동적 타입 언어이나 3.5 버전부터 Type Hinting과 MyPy를 통해 데이터 타입을 검사        

- PEP
    - [PEP8](./pep8.md)
- [Python Install](#python-install)
- [Python Programming Language](./python-basic/)
- Python Tool
    - [Python Package Manager](./python-tool/pyhton-package-manager.md)
    - [Python Environment Manager](./python-tool/python-environment-manager.md)
    - [Anaconda](./python-tool/anaconda.md)
    - [Jupyter Notebook](./python-tool/jupyter-notebook.md)
- [Python WSGI](./wsgi.md)
- Python Web Framework
    - Django
    - Flask
    - Pyramid
- [Data Science](./python-data-science/)



## Python Install

```bash
$ wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz
$ tar -xvf Python-3.5.1.tar.xz

$ cd Python-3.5.1
$ ./configure --enable-optimizations
$ make altinstall

# 설치 확인
$ python3.5 --verseion


# REPL
$ python3.5
>>> exit()
```



[top](#)
