import threading, time

class Tabuadas(threading.Thread):
    def __init__(self, valor):
        threading.Thread.__init__(self)
        self.valor = valor

    def run(self):
        counter = 1
        while counter <= 10:
            print('{} x {} = {}'.format(self.valor, counter, self.valor * counter))
            counter += 1

for x in range(1,11):
    t = Tabuadas(x)
    t.start()
    t.join()