import time
import itertools

passwd = ("".join(x) for x in itertools.product("0123456789",repeat=3))





while True:
    try:
        time.sleep(0.5)
        str = next(passwd)
        print(str)
    except StopIteration as e:
        break