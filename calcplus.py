#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fich = open(sys.argv[1], 'r')
operaciones = fich.readlines()
calculator = calcoohija.CalculadoraHija()

for line in operaciones:
    # crea una lista con los elementos del fichero separados por comas
    elements = line.split(',')
    # .pop(0) devuelve el primer elemento de la lista y lo borra,
    # quedando solo los operandos
    operacion = elements.pop(0)
    try:
        if operacion == 'suma':
            # hay que inicializar el resultado, al ser una suma, a 0 vale
            resultado = 0
            for operando in elements:
                # por cada elemento de la lista suma lo que ya lleva mas el elemento
                resultado = resultado + calculator.plus(int(operando), 0)
            print(resultado)

        elif operacion == 'resta':
            # En este caso habra que inicializar resultado al elemento mayor,
            # en este caso el primer elemento de la lista
            resultado = elements.pop(0)
            for operando in elements:
                resultado = int(resultado) - calculator.minus(int(operando), 0)
            print(resultado)

        elif operacion == 'multiplica':
            # multiplicar por 1 no afecta, asi que inicio resultado a 1
            resultado = 1
            for operando in elements:
                resultado = int(resultado) * \
                    calculator.product(int(operando), 1)
            print(resultado)

        elif operacion == 'divide':
            # Al igual que en la resta, inicio el resultado al primer elemento
            # de la lista(el mas mayor)
            resultado = elements.pop(0)
            for operando in elements:
                try:
                    resultado = int(resultado) / \
                        calculator.division(int(operando), 1)

                except ZeroDivisionError:
                    sys.exit('Division by zero is not allowed')
            print(resultado)

        else:
            sys.exit('Incorrect operation')

    except ValueError:
        sys.exit('Error: Non numerical parameters')

fich.close()
