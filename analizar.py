#!/usr/bin/env python3
from sys import stdin, argv

from automata.base.exceptions import AutomatonException

from palindromos import palindromos as dtm

def evaluar(w, debug=False):
    if debug:
        for c in dtm.read_input_stepwise(w):
            c.print()
        return True
    return dtm.accepts_input(w)


if __name__ == '__main__':
    for w in stdin:
        res = False
        try:
            res = evaluar(w.strip(), '--debug' in argv) # strip saca el enter del final
        except AutomatonException as ex:
            print(ex.args)
        if (res):
            print('ACEPTA')
        else:
            print('RECHAZA')
