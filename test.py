from sympy import *
from sympy.logic.algorithms.dpll import *

from sympy import symbols
from sympy.logic.boolalg import Equivalent, Implies
from sympy.logic.inference import pl_true, satisfiable, PropKB
from sympy.logic.algorithms.dpll import dpll, dpll_satisfiable, \
    find_pure_symbol, find_unit_clause, unit_propagate, \
    find_pure_symbol_int_repr, find_unit_clause_int_repr, \
    unit_propagate_int_repr
from sympy.utilities.pytest import raises, XFAIL

#A, B, C = symbols('A,B,C')
#t_2_6 = symbols('t_2_6')
#t_1_6 = symbols('t_2_7')
#t_4_5 = symbols('t_4_5')
#t_2_7 = symbols('t_2_7')
#print find_unit_clause(False, {t_2_6: False, t_1_6: True, t_2_7: False, t_4_5:True})
#l = [1,2,3,4,5,6]
#for i in range (1,1+3):
#    print l[i]
'''
kb = PropKB()
A, B, C, D, E ,F, G, H,I= symbols('A,B,C,D,E,F,G,H,I')
kb.tell((~A & B)|(A&~B))
kb.tell((~A&B&C)|(A&~B&C)|(A&B&~C))

kb.tell((~B&C&D&E)|(B&~C&D&E)|(B&C&~D&E)|(B&C&D&~E))
kb.tell(E)
kb.tell((~E&~F&G&H)|(~E&F&~G&H)|(~E&F&G&~H)|(H&~F&~G&H)|(H&~F&G&~H)|(H&F&~G&~H))
kb.tell((~G&H&I)|(G&~H&I)|(G&H&~I))
'''
#print kb.ask(A)
#print to_dnf((~A & B)|(A&~B))
#E & ((A & ~B) | (B & ~A)) & ((A & B & ~C) | (A & C & ~B) | (B & C & ~A)) & ((G & H & ~I) | (G & I & ~H) | (H & I & ~G)) & ((B & C & D & ~E) | (B & C & E & ~D) | (B & D & E & ~C) | (C & D & E & ~B)) & ((H & ~F & ~G) | (F & G & ~E & ~H) | (F & H & ~E & ~G) | (F & H & ~G & ~H) | (G & H & ~E & ~F) | (G & H & ~F & ~H))

#expr = (to_dnf((~A & B)|(A&~B)))&to_dnf((~A&B&C)|(A&~B&C)|(A&B&~C))&to_dnf((~B&C&D&E)|(B&~C&D&E)|(B&C&~D&E)|(B&C&D&~E))&(E)&to_dnf((~E&~F&G&H)|(~E&F&~G&H)|(~E&F&G&~H)|(H&~F&~G&H)|(H&~F&G&~H)|(H&F&~G&~H))&to_dnf((~G&H&I)|(G&~H&I)|(G&H&~I))
#print (dpll_satisfiable(expr&A))
#print (dpll_satisfiable(expr&~A))


#print (kb.ask(A))
#print (kb.ask(B))
#print (kb.ask(C))
#print (kb.ask(D))
#print (kb.ask(E))
#print (kb.ask(F))
#print (kb.ask(G))
#print (kb.ask(H))
#print (kb.ask(I))
#print (kb.ask(C))
#print (kb.ask(B))

import logic

def test_KB_tell():
    import logic
    A, B, C, D, E, F, G, H, I = symbols('A,B,C,D,E,F,G,H,I')
    kb=logic.PropKB()
    kb.kbTell((~A & B)|(A&~B))
    kb.kbTell((~A & B & C) | (A & ~B & C) | (A & B & ~C))

    kb.kbTell((~B & C & D & E) | (B & ~C & D & E) | (B & C & ~D & E) | (B & C & D & ~E))
    kb.kbTell(E)
    kb.kbTell((~E & ~F & G & H) | (~E & F & ~G & H) | (~E & F & G & ~H) | (H & ~F & ~G & H) | (H & ~F & G & ~H) | (
    H & F & ~G & ~H))
    kb.kbTell((~G & H & I) | (G & ~H & I) | (G & H & ~I))

    print kb.kbAsk(A)

test_KB_tell()
