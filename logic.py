from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent, disjuncts, conjuncts, to_cnf
from sympy.core import Symbol, sympify
from sympy.logic.boolalg import Boolean
import re
from sympy import symbols
from sympy.logic.boolalg import Equivalent, Implies
from sympy.logic.inference import pl_true, satisfiable, PropKB
from sympy.utilities.pytest import raises, XFAIL
from sympy.logic import simplify_logic

# for test import

import logic_inference

class PropKB():
    def __init__(self, sentence = None):
        self.clauses = []
        self.expr = True
        if sentence:
            self.tell(sentence)

    def tell(self, sentence):
        for c in conjuncts(to_cnf(sentence)):
            if not c in self.clauses:
                self.clauses.append(c)


    def kbTell(self, sentence):
        self.expr = self.expr & sentence
        print self.expr


    def kbAsk(self,query):

        return logic_inference.dpll_satisfiable(self.expr & query)

    #def ask(self, query):
    #    if len(self.clauses) == 0:
    #        return False
    #    from sympy.logic.algorithms.dpll import dpll
    #    query_conjuncts = self.clauses[:]
    #    query_conjuncts.extend(conjuncts(to_cnf(query)))
    #    s = set()
    #    for q in query_conjuncts:
    #        s = s.union(q.atoms(Symbol))
    #    return dpll(query_conjuncts, list(s), {})


    def retract(self, sentence):
        for c in conjuncts(to_cnf(sentence)):
            if c in self.clauses:
                self.clauses.remove(c)


def test_PropKB():
    kb = PropKB()
    A, B, C = symbols('A, B, C')
    #kb.tell(((A&~B)|(~A&B)))
    #kb.tell((A&~C)|(~A&C))
    kb.tell(A&~B)
    kb.tell(~A&B)
    kb.tell(A&~C)
    kb.tell(~A&C)
    kb.ask(A)
    print (kb.ask(A))


#test_PropKB()


#import numpy as np
#table = np.zeros((5, 5))
#print (table)
#table[1][1] = 1
#table[1][2] = 9
#table[1][3] = 1
#table[2][2] = 1
#print (table)

def set_dict_perm(table, i ,j):
    dict_perm = []
    if table[i - 1][j] == -1: dict_perm.append("t_" + str(i-1) + '_' + str(j)) # up
    if table[i + 1][j] == -1: dict_perm.append("t_" + str(i+1) + '_' + str(j)) # down
    if table[i][j - 1] == -1: dict_perm.append("t_" + str(i) + '_' + str(j-1)) # left
    if table[i][j + 1] == -1: dict_perm.append("t_" + str(i) + '_' + str(j+1)) # right
    if table[i - 1][j - 1] == -1: dict_perm.append("t_" + str(i-1) + '_' + str(j-1)) # up_left
    if table[i - 1][j + 1] == -1: dict_perm.append("t_" + str(i-1) + '_' + str(j+1)) # up_right
    if table[i + 1][j - 1] == -1: dict_perm.append("t_" + str(i+1) + '_' + str(j-1)) # down_left
    if table[i + 1][j + 1] == -1: dict_perm.append("t_" + str(i+1) + '_' + str(j+1)) # down_right

    return dict_perm


def perm_1(kb, table, a, b):
    dict_perm = set_dict_perm(table, a, b)
    if len(dict_perm) == 0:
        kb.tell(True)
        return None

    dnf = False
    cnt = 0
    #print dnf
    for i in range(len(dict_perm)):
        literal = symbols(dict_perm[i])
        for j in range(len(dict_perm)):
            if i == j: continue
            tmp = ~symbols(dict_perm[j])
            literal = literal & tmp
        if cnt == 0:
            dnf = literal
            #print "print DNF"
            #print dnf
            cnt += 1
        else:
            dnf = dnf | literal
            print "dnf"
            print dnf
        if dnf == False: continue
        #print dnf
        kb.kbTell(dnf)

def perm_2(kb,table,i,j):
    dict_perm = set_dict_perm(table, i, j)
    if len(dict_perm) == 0:
        kb.tell(True)
        return None

    dnf = False
    cnt = 0
    for i in range(len(dict_perm)):
        literal = symbols(dict_perm[i])
        for j in range(len(dict_perm)):
            if i == j: continue
            literal = literal & symbols(dict_perm[j])
            for k in range(len(dict_perm)):
                if k == j or k == i: continue
                tmp = ~symbols(dict_perm[k])
                literal = literal & tmp
        if cnt == 0:
            dnf = literal
            cnt += 1
        else:
            dnf = dnf | literal
        #print dnf
        if dnf == False: continue
        kb.kbTell(dnf)

def perm_3(kb,table,i,j):
    dict_perm = set_dict_perm(table, i, j)
    if len(dict_perm) == 0:
        kb.tell(True)
        return None

    dnf = False
    cnt = 0
    for i in range(len(dict_perm)):
        literal = symbols(dict_perm[i])
        for j in range(len(dict_perm)):
            if i == j: continue
            literal = literal & symbols(dict_perm[j])
            for k in range(len(dict_perm)):
                if k == j or k == i: continue
                literal = literal & symbols(dict_perm[k])
                for p in range(len(dict_perm)):
                    if p == k or p ==j or p == i: continue
                    tmp = ~symbols(dict_perm[p])
                    literal = literal & tmp
        if cnt == 0:
            dnf = literal
            cnt += 1
        else:
            dnf = dnf | literal
        if dnf == False: continue
        kb.kbTell(dnf)

def perm_4(kb,table,i,j):
    dict_perm = set_dict_perm(table, i, j)
    if len(dict_perm) == 0:
        kb.tell(True)
        return None

    dnf = False
    cnt = 0
    for i in range(len(dict_perm)):
        literal = symbols(dict_perm[i])
        for j in range(len(dict_perm)):
            if i == j: continue
            literal = literal & symbols(dict_perm[j])
            for k in range(len(dict_perm)):
                if k == j or k == i: continue
                literal = literal & symbols(dict_perm[k])
                for p in range(len(dict_perm)):
                    if p == k or p ==j or p==i: continue
                    literal = literal & symbols(dict_perm[p])
                    for q in range(len(dict_perm)):
                        if q == p or q == k or q ==j or q == i : continue
                        tmp = ~symbols(dict_perm[q])
                        literal = literal & tmp
        if cnt == 0:
            dnf = literal
            cnt += 1
        else:
            dnf = dnf | literal
        if dnf == False: continue
        kb.kbTell(dnf)

#kb = PropKB()
#for i in range(1,4):
#    for j in range(1,4):
#        if table[i][j] == 0: continue
#        if table[i][j] == 1 and table[i][j] != 9 and table[i][j] != 0: perm_1(kb, table, i, j)
#        elif table[i][j] == 2 and table[i][j] != 9 and table[i][j] != 0: perm_2(kb,table, i, j)
#print (kb.ask(symbols('t_1_2')))
#print (kb.ask(~symbols('t_1_1')))
def dim_adjust(table, dim):
    import numpy as np
    ret = np.zeros((dim+2, dim+2))
    for i in range(1, dim+1):
        for j in range(1, dim+1):
            ret[i][j] = table[i-1][j-1]
    print ret
    return ret

def solver(pos, table, count):
    #print "table"
    #print table
    dim = len(table)
    print "dim"
    print dim
    a = pos[count][0]
    b = pos[count][1]
    print "a, b"
    print a, b
    kb = PropKB()
    board = dim_adjust(table, dim)
    print board
    for i in range (1, dim+1):
        for j in range(1, dim+1):
            if board[i][j] == 0 or board[i][j] == -1: continue
            elif board[i][j] == 1 : perm_1(kb, board, i, j)
            elif board[i][j] == 2 : perm_2(kb, board, i, j)
            elif board[i][j] == 3 : perm_3(kb, board, i, j)
            elif board[i][j] == 4 : perm_4(kb, board, i, j)

    nomine = []
    mine = []
    pos = 't_' + str(a+1) + '_' + str(b+1)
    result1 = kb.kbAsk(symbols(pos))
    result2 = kb.kbAsk(~symbols(pos))
    if result1 != False and result2 == False:
        mine.append((a, b))
    elif result1 == False and result2 != False:
        nomine.append((a, b))
    elif result1 != False and result2 != False:
        mine.append((a, b))
        nomine.append((a, b))

    '''
    for i in range (1, dim+1):
        for j in range (1, dim +1):
            if board[i][j] == -1:
                pos = 't_' + str(i) + '_' + str(j)
                result1 = kb.kbAsk(symbols(pos))
                result2 = kb.kbAsk(~symbols(pos))
                if result1 != False and result2 == False:
                    mine.append((i-1, j-1))
                elif result1 == False and result2 != False:
                    nomine.append((i-1,j-1))
                elif result1 != False and result2 != False:
                    mine.append((i-1,j-1))
                    nomine.append((i-1,j-1))
        print "mine"
        print mine
    '''
    #pos = 't_' + str(a+1) + '_' + str(b+1)
    #result = kb.ask(symbols(pos))
    #print result
    #nomine = []
    #mine = []
    #if result != False:
    #    mine.append((a, b))
    print "mine"
    print mine
    return nomine, mine
    #print a


import numpy as np
table = np.zeros((3, 3))
#print (table)
table[0][0] = 9
table[0][1] = 1
table[1][0] = 1

#print (table)
#solver(table, 3, 0, 0)


