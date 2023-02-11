import multiprocessing
import time

class Process(multiprocessing.Process):
    def run(self) -> None:
        print("work")

pr = Process()
pr.start()