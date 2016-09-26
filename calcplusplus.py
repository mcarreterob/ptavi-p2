#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

with open(sys.argv[1]) as csvFile:
    operaciones = csv.reader(csvFile)
    calculatorplus = calcoohija.CalculadoraHija()

    for line in operaciones:
        operacion = line.pop(0)
        try:
            if operacion == 'suma':
                resultado = 0
                for operando in line:
                    resultado = resultado + \
                        calculatorplus.plus(int(operando), 0)
                print(resultado)

            elif operacion == 'resta':
                resultado = line.pop(0)
                for operando in line:
                    resultado = int(resultado) - \
                        calculatorplus.minus(int(operando), 0)
                print(resultado)

            elif operacion == 'multiplica':
                resultado = 1
                for operando in line:
                    resultado = resultado = int(resultado) * \
                        calculatorplus.product(int(operando), 1)
                print(resultado)

            elif operacion == 'divide':
                resultado = line.pop(0)
                for operando in line:
                    try:
                        resultado = int(resultado) / \
                            calculatorplus.division(int(operando), 1)

                    except ZeroDivisionError:
                        sys.exit('Division by zero is not allowed')
                print(resultado)

            else:
                sys.exit('Incorrect operation')

        except ValueError:
            sys.exit('Error: Non numerical parameters')

csvFile.close()
