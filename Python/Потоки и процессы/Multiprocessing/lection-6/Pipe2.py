import time
from multiprocessing import Pipe, Process

def getter(*pipe):
    out, inp = pipe
    inp.close()
    while True:
        try:
            print(f"data: {out.recv()}")
        except:
            break
def setter(sequence, input_c):
    for item in sequence:
        time.sleep(0.5)
        input_c.send(item)



if __name__ == '__main__':
    output_c, input_c = Pipe()
    pr = Process(target=getter, args=(output_c, input_c, ))
    pr.start()

    output_c.close()
    setter(list(range(10)), input_c)
    output_c.close()
    input_c.close()
    pr.join()
