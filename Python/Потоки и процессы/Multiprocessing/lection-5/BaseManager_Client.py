from multiprocessing.managers import BaseManager
import multiprocessing

if __name__ == '__main__':
    BaseManager.register("get")
    manager = BaseManager(address=("127.0.0.1", 4444), authkey=b'abc')
    print("client connected")
    manager.connect()
    result = manager.get()
    print(f"result: {result}")