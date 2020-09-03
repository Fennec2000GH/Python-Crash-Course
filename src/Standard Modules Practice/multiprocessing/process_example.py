
import math
from multiprocessing import Process


def square(n: int) -> None:
    """Squares an integer"""
    print(f'{n}^2 = {int(math.pow(n, 2))}')


if __name__ == '__main__':
    p1 = Process(target=square, args=(1,), name='1 squared')
    p2 = Process(target=square, args=(4,), name='4 squared')
    p3 = Process(target=square, args=(8,), name='8 squared')
    p4 = Process(target=square, args=(12,), name='12 squared')

    # Process properties
    print(f'p1 pid = {p1.pid}')
    print(f'p1 daemon {p1.daemon}')
    print(f'p1 authkey = {p1.authkey.decode(encoding="UTF-8", errors="ignore")}')
    print(f'p1 exitcode before start = {p1.exitcode}')

    p1.start()
    p2.start()
    p3.start()
    p3.terminate()
    p4.start()
    p4.kill()

    p1.join(timeout=3)
    p2.join()
    p3.join()
    p4.join()

    print(f'Is p1 still alive? {p1.is_alive()}')
    print(f'p1 sentinel = {p1.sentinel}')
    print(f'p1 exitcode after join = {p1.exitcode}')

    p1.close()
    p2.close()
    p3.close()
    p4.close()
