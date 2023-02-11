import multiprocessing


def end_func(responce):
    print(responce)
def out(x, y, z):
    print(f"value: {x} {y} {z}")
    return (x, y, z,)


if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as pool:
        # pool.starmap(out, [(1, 2, 3), (4, 5, 6)])
        pool.starmap_async(out, [(1, 2, 3), (4, 5, 6)], callback=end_func)
        pool.close()
        pool.join()