from threading import Thread, active_count, current_thread
import math
import time

class PrimeThread(Thread):
    def __init__(self, num,file):
        super().__init__()
        self.num = num
        self.file = file

    def run(self):
        for n in range(2, math.ceil(math.sqrt(self.num))):
            if self.num % n == 0:
                time.sleep(1)
                self.file.write( str(self.num) + " is not a prime number!\n")
                break
        else:
            self.file.write( str(self.num) + " is a prime number!\n")


nums = [393939393, 121212121212121, 2929293343434393213, 38433828284937493794837984739, 62551414124111, 20]

f  = open("primes.txt","wt")

for n in nums:
    t = PrimeThread(n,f)
    t.start()


# wait until child threads are terminated
while active_count() > 1:
    print("waiting....")
    time.sleep(1)


f.close()

