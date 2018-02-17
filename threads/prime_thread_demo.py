from threading import Thread, active_count, current_thread
import math


class PrimeThread(Thread):
    def __init__(self, num):
        super().__init__()
        print("In thread : ", self.getName())
        self.num = num

    def run(self):
        for n in range(2, math.ceil(math.sqrt(self.num))):
            if self.num % n == 0:
                print(self.num, " is not a prime number!")
                break
        else:
            print(self.num, " is a prime number!")


nums = [393939393, 121212121212121, 2929293343434393213, 38433828284937493794837984739, 62551414124111, 20]

print("In thread", current_thread().getName())

for n in nums:
    t = PrimeThread(n)
    t.start()
    print("No. of thread active :", active_count())

