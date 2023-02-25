import time
import multiprocessing

# ~~ 코드를 실행했는데, 이 코드를 수행하는데 걸린 시간??

def add_func(start, end, li):
    for i in range(start, end + 1):
        li.put(i)

# main thread

# target -> 쓰레드가 실행할 함수
li = multiprocessing.Queue()
th = multiprocessing.Process(target = add_func, args=(0, 100000000 // 2, li))
th2 = multiprocessing.Process(target= add_func, args=(100000000 // 2, 100000000, li))


s = time.time()

th.start() # 해당 쓰레드가 일 하러 감.
th2.start()
th.join() # 이 매서드를 실행한 쓰레드에 th ( thread ) 를 join
th2.join()

#print(result) # print 를 실행한 장소 ( main thread )
f = time.time()

li.put('end')

sum = 0

while True:
    t = li.get()
    if t == 'end':
        break
    else:
        sum = sum + t


print(f"실행 소유시간 : {f-s}")