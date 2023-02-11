import multiprocessing
def end_func(responce):
    print(responce)

def out(x):
    print(f"value: {x}")
    return f"new_{x}"

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as pool:
        for i in range(10):
            pool.apply_async(out, args=(i, ), callback=end_func)
        pool.close()
        pool.join()