Excuted with output. Please check.

PS D:\KIMO\Company_Assignment> python setup_db.py 
Courses data has been successfully added to MongoDB.
PS D:\KIMO\Company_Assignment> python main.py    
PS D:\KIMO\Company_Assignment> pytest test_main.py
================================================================== test session starts ===================================================================
platform win32 -- Python 3.12.3, pytest-8.3.2, pluggy-1.5.0
rootdir: D:\KIMO\Company_Assignment
plugins: anyio-4.4.0
collected 4 items

test_main.py ....                                                                                                                                   [100%]

=================================================================== 4 passed in 1.74s ==================================================================== 
PS D:\KIMO\Company_Assignment> git init
Reinitialized existing Git repository in D:/KIMO/Company_Assignment/.git/
PS D:\KIMO\Company_Assignment> git add .
warning: in the working copy of 'courses.json', LF will be replaced by CRLF the next time Git touches it
PS D:\KIMO\Company_Assignment> git commit -m "commited"
[main (root-commit) 4eea956] commited
 8 files changed, 578 insertions(+)
 create mode 100644 Dockerfile
 create mode 100644 __pycache__/main.cpython-312.pyc
 create mode 100644 __pycache__/test_main.cpython-312-pytest-8.3.2.pyc
 create mode 100644 courses.json
 create mode 100644 main.py
 create mode 100644 requirements.txt
 create mode 100644 setup_db.py
 create mode 100644 test_main.py
