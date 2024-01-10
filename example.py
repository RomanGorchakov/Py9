#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

def tail_call_optimized(g):
"""
Эта программа показыает работу декоратора, который производит оптимизацию
хвостового вызова. Он делает это, вызывая исключение, если оно является его
прародителем, и перехватывает исключения, чтобы подделать оптимизацию хвоста.
Эта функция не работает, если функция декоратора не использует хвостовой вызов.
"""

    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while True:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException, e:
                    args = e.args
                    kwargs = e.kwargs

    func.__doc__ = g.__doc__
    return func

@tail_call_optimized
def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)

if __name__ == '__main__':
    print(fib(10000))