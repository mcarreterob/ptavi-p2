#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():

    def plus(self, op1, op2):
        return op1 + op2
    
    def minus(self, op1, op2):
        return op1 - op2


if __name__ == "__main__":

    calculadora = Calculadora()
    
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
        
    if sys.argv[2] == "suma":
        resultado = calculadora.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        resultado = calculadora.minus(operando1, operando2)
        
    else:
        sys.exit("Solo puedo sumar y restar")
        
    print(resultado)
