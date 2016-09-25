#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):

    def product(self, op1, op2):
        return op1 * op2

    def division(self, op1, op2):
        return op1 / op2
        
        
if __name__ == "__main__":

    calculadorahija = CalculadoraHija()
    
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    
    if sys.argv[2] == "suma":
        resultado = calculadorahija.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        resultado = calculadorahija.minus(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        resultado = calculadorahija.product(operando1, operando2)
    elif sys.argv[2] == "divide":
        try:
            resultado = calculadorahija.division(operando1, operando2)
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")
            
    else:
        sys.exit("Incorrect operation")
    
    print(resultado)
