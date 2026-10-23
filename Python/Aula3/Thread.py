import threading, time

class ExampleThread(threading.Thread):
    def __init__(self, times, delay):
        threading.Thread.__init__(self)
        self.times = times
        self.delay = delay

    def run(self):
        while self.times:
            print('{} - iterating: {}'.format(self.getName(), self.times))
            time.sleep(self.delay)
            self.times -= 1

print('Initializing...')
t1 = ExampleThread(10, 3)#vai rodar 10 vezes a cada 3 segundos
t2 = ExampleThread(15, 1)
t1.start()
t1.join()#aguarda a primeira rodar para rodar a segunda
t2.start()
t2.join()
print('Finished!')