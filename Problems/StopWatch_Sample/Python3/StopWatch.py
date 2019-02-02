# coding: utf-8

import time


def main():
    time0 = time.time()

    print("Hit Return Key...")
    time0 = time.time()

    input()

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
