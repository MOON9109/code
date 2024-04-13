#__enter__, __exit__, exception

#context_manager: 원하는 타이밍 정확하게 리소스를 할당 및 제공 반환하는 역할

#Ex1

file=open('./textfile1.txt','w')
try:
    file.write('context manager test1\nContextlib Text1.')

finally:
    file.close()

#Ex2
with open('./textfile2.txt','w') as f:
    f.write('context manager test2\nContextlib Text2.')
    #with 문 사용하면 close 사용하지 않아도 자동으로 반환 (with에 포함되어 있음)

#Ex3
#context manager with exception handling
class MyFileWriter():
    def __init__(self,file_name,method):
        print('MyFileWriter started : __init__')
        self.file_obj=open(file_name,method)

    def __enter__(self):
        print('MyFileWriter started : __enter__')
        return self.file_obj
    def __exit__(self, exc_type, value, trace_back):
        print('MyFileWriter started : __exit__')
        if exc_type:
            print('Logging exception {}'.format((exc_type, value, trace_back)))

        self.file_obj.close()

with MyFileWriter('./textfile3.txt','w') as f:
    f.write('context manager test3\nContextlib Text3.')