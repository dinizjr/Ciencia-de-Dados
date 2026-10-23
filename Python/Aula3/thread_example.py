import threading, time


class ExampleThread(threading.Thread):
    def __init__(self, times, delay):
        threading.Thread.__init__(self)
        self.counter = times
        self.delay = delay

    def run(self):
        while self.counter:
            print('{} - iterating: {}'.format(self.getName(), self.counter))
            time.sleep(self.delay)
            self.counter -= 1

print('Initializing...')
t1 = ExampleThread(10, 3)
t2 = ExampleThread(15, 1)
t1.start()
t2.start()
t1.join()
t2.join()
print('Finished!')
