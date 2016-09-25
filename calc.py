#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def plus(op1, op2):
    """ Function to sum the operands """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2
    

def product(op1, op2):
	"""Function to multiplicate the operands"""
	return op1 * op2
	

def division(op1, op2):
	"""Function to divide the operands"""
	return op1 / op2
	

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = minus(operando1, operando2)
    elif sys.argv[2] == "multiplicacion":
        result = product(operando1, operando2)
    elif sys.argv[2] == "division":
        try:
            result = division(operando1, operando2)
        except ZeroDivisionError:
            sys.exit("No puedo dividir entre 0")
            
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
