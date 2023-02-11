import multiprocessing
import time

def test():
    for _ in range(5):
        print(f"{multiprocessing.current_process()}", time.time())
        time.sleep(1)

if __name__ == '__main__':
    prcs = []
    # multiprocessing.freeze_support()
    for i in range(3):
        prc = multiprocessing.Process(target=test, name=f"prc-{i}")
        prcs.append(prc)
        prc.start()
    for pr in prcs:
        pr.join()
    #join Дожидается того момента, когда процесс будет завершен
    time.sleep(5)

    print("Процесс завершен")
    # prc.is_alive() # Проверяет, существует ли процесс
    # prc.kill() # Убивает процесс
    # prc.pid # id процесса
    # prc.terminate() # Также убирает процесс



