'''
context manager annotation
keyword @contextlib.contextmanager, __enter__, __exit__
'''

#Ex1
#Use decorator

import contextlib
import time

@contextlib.contextmanager
def my_file_writer(file_name,method):
    f=open(file_name,method)
    yield f #__enter__
    f.close() #__exit__


with my_file_writer('testfile4.txt','w') as f:
    f.write('context manager test4, \n contextlib test4.')

#Ex2
#Use decorator
class ExecuteTimer():
    def __init__(self,msg):
        self.msg=msg

    def __enter__(self):
        self._start= time.monotonic()
        return self._start

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print("Logging exception {}".format((exc_type, exc_value, exc_traceback)))
        else:
            print('{} : {} s'.format(self.msg,time.monotonic()-self._start))
        return True

@contextlib.contextmanager
def ExecuteTimerDc(msg):
    start = time.monotonic()
    try: #__enter__
        yield start

    except BaseException as e:
        print('Logging exception : {} : {}'.format(msg,e))
        raise

    else:
        print('{}: {}s'.format(msg, time.monotonic()-start))


with ExecuteTimerDc('Start job') as v:
    print('Received start monotonic2:{}'.format(v))
    for i in range(400000):
        pass

    #raise ValueError('occured.')