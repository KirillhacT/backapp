import time
import threading

#Поток демон завершается с завершением программы
def get_data(data):
    for _ in range(5):
        print(f"[{threading.currentThread().name}] - [{data}]")
        time.sleep(1)

thr = threading.Thread(target=get_data, args=(str(time.time()),), daemon=False)
thr.setDaemon(True)
thr.start()
time.sleep(2)
print("finish")
