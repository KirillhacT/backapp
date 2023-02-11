import threading
import time


def progress_bar(steps: int) -> None:
    for i in range(1, steps + 1):
        print(f"Загрузка \r{i}%", end="")
        time.sleep(0.05)
prog = threading.Thread(target=progress_bar, args=(int(100),))
prog.start()
prog.join()
print("\rПоздравляем, вы анимешник!", end="")
