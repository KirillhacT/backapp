import multiprocessing
from multiprocessing import Pipe
#Pipe - технология передачи данных между процессами

def send_data(conn):
    conn.send("hello world")
    conn.close() #Закрывает канал

if __name__ == '__main__':
    # a - является каналом для передачи данных
    # b - является каналом для получения данных
    # a, b = Pipe()
    # a.send([1, "hello"])
    # print(b.recv())
    output_c, input_c = Pipe()
    p = multiprocessing.Process(target=send_data, args=(input_c,))
    p.start()
    p.join()
    print(f"data: {output_c.recv()}")
