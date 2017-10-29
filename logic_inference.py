from __future__ import print_function, division
from sympy import *
import numpy as np
from sympy.logic.boolalg import Boolean

from sympy.core.compatibility import range
from sympy import default_sort_key
from sympy.logic.boolalg import Or, Not, conjuncts, disjuncts, to_cnf, to_int_repr, _find_predicates
from sympy.logic.inference import pl_true, literal_symbol, PropKB


#def makeTable(n):
#    return [[0] * n for i in range(n)]


def dpll_satisfiable(expr):
    clauses = conjuncts(to_cnf(expr))
    if False in clauses:
        return False
    symbols = sorted(_find_predicates(expr), key=default_sort_key)
    symbols_int_repr = set(range(1, len(symbols) + 1))
    clauses_int_repr = to_int_repr(clauses, symbols)
    result = dpll_int_repr(clauses_int_repr, symbols_int_repr, {})
    if not result:
        return result
    output = {}
    for key in result:
        output.update({symbols[key - 1]: result[key]})
    return output

def dpll_int_repr(clauses, symbols, model):
    # compute DP kernel
    P, value = find_unit_clause_int_repr(clauses, model)
    while P:
        model.update({P: value})
        symbols.remove(P)
        if not value:
            P = -P
        clauses = unit_propagate_int_repr(clauses, P)
        P, value = find_unit_clause_int_repr(clauses, model)
    P, value = find_pure_symbol_int_repr(symbols, clauses)
    while P:
        model.update({P: value})
        symbols.remove(P)
        if not value:
            P = -P
        clauses = unit_propagate_int_repr(clauses, P)
        P, value = find_pure_symbol_int_repr(symbols, clauses)
    # end DP kernel
    unknown_clauses = []
    for c in clauses:
        val = pl_true_int_repr(c, model)
        if val is False:
            return False
        if val is not True:
            unknown_clauses.append(c)
    if not unknown_clauses:
        return model
    P = symbols.pop()
    model_copy = model.copy()
    model.update({P: True})
    model_copy.update({P: False})
    symbols_copy = symbols.copy()
    return (dpll_int_repr(unit_propagate_int_repr(unknown_clauses, P), symbols, model) or
            dpll_int_repr(unit_propagate_int_repr(unknown_clauses, -P), symbols_copy, model_copy))

def pl_true_int_repr(clause, model={}):
    result = False
    for lit in clause:
        if lit < 0:
            p = model.get(-lit)
            if p is not None:
                p = not p
        else:
            p = model.get(lit)
        if p is True:
            return True
        elif p is None:
            result = None
    return result

def unit_propagate_int_repr(clauses, s):
    negated = {-s}
    return [clause - negated for clause in clauses if s not in clause]

def find_pure_symbol_int_repr(symbols, unknown_clauses):
    all_symbols = set().union(*unknown_clauses)
    found_pos = all_symbols.intersection(symbols)
    found_neg = all_symbols.intersection([-s for s in symbols])
    for p in found_pos:
        if -p not in found_neg:
            return p, True
    for p in found_neg:
        if -p not in found_pos:
            return -p, False
    return None, None

def find_unit_clause_int_repr(clauses, model):
    bound = set(model) | set(-sym for sym in model)
    for clause in clauses:
        unbound = clause - bound
        if len(unbound) == 1:
            p = unbound.pop()
            if p < 0:
                return -p, False
            else:
                return p, True
    return None, None

#answer = dpll_int_repr([{1}, {2}, {3}], {1, 2}, {3: False})
#print (answer)

# to do how to build clauses

"""
# ------test-------------
# table = makeTable(5)
# print (table)
table = np.zeros((5, 5))
#print (table)
table[1][1] = 9
table[1][2] = 1
table[2][1] = 1
print (table)
#print ([{1}, {2}, {3}])

clauses = []
# table[1][2]
disjuncts_left = 11
disjuncts_right = 13
disjuncts_up = 2
disjuncts_down = 22
disjuncts_up_left = 1
disjuncts_up_right = 3
disjuncts_down_left = 21
disjuncts_down_right = 23

#print ([{1}, {2}, {3}])
clauses.append({-1*disjuncts_left, disjuncts_right, disjuncts_up, disjuncts_down, disjuncts_up_left, disjuncts_up_right,
         disjuncts_down_left, disjuncts_down_right})
print (clauses)

#table[2][1]
disjuncts_left = 20
disjuncts_right = 22
disjuncts_up = 11
disjuncts_down = 31
disjuncts_up_left = 10
disjuncts_up_right = 12
disjuncts_down_left = 30
disjuncts_down_right = 32
clauses.append({disjuncts_left, disjuncts_right, -1*disjuncts_up, disjuncts_down, disjuncts_up_left, disjuncts_up_right,
         disjuncts_down_left, disjuncts_down_right})
print (clauses)

#print (dpll_int_repr(clauses, {11,21,22}, {11: True}))
# A & ~B


#from sympy.abc import A, B, C
#print (dpll_satisfiable(((A & ~B) | (~A & B)) & ((~A & C) | (A & ~C))))

symbol_test = ['x', 'y']
symbol_test2 = []
for i in range(2):
    symbol_test2.append(symbols(symbol_test[i]))

print (symbol_test2)
"""
#table = np.zeros((5, 5))
#print (table)
#table[1][1] = 9
#table[1][2] = 1
#table[2][1] = 1
#print (table)

'''
expr = []
for i in range(1,3):
    for j in range(1,3):
        if table[i][j] != 9 and table[i][j] != 0:  # encountering a mine.
            expr.append(symbols("table"+'['+str(i)+']'+'['+str(j)+']'))

'''
#from sympy.abc import A, B, D
#print (dpll([A, B, D], [A, B], {D: False}))









