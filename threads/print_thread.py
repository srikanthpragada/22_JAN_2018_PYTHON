from threading import Thread


class PrintThread(Thread):
    def run(self):
        for i in range(1, 11):
            print("Child ", i)


t1 = PrintThread()
t1.start()

for i in range(1, 50):
    print("Main " , i)
