from timeit import default_timer as timer


class Timer:
    def __init__(self):
        self.s = None
        self.e = None

    def start(self):
        self.s = timer()
        self.e = None

    def stop(self):
        if self.e is not None:
            raise Exception('run timer again')
        if self.s is None:
            raise Exception('timer is not running')
        self.e = timer()

    def elapsed(self):
        if self.s is None:
            raise Exception('timer is not running')
        if self.e is None:
            raise Exception('timer is still running ')
        return self.e - self.s

    def show(self):
        print(f'Elapsed: {self.elapsed()}[s]')
