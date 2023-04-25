# This is a sample Python script.
import random
import sys

from fpdf import fpdf

import pdfwriter


# Press Mayús+F10 to execute it or replace it with your code.
# Press Dou2ble Shift to search everywhere for classes, files, tool windows, actions, and settings.

def read_data():
    if len(sys.argv) != 5:
        raise Exception("Número de parámetros inválido\n\tpython main.py [question_file] [num_questions] [num_versions] [test_name]")
    fich = sys.argv[1]
    open_f = open(fich, "r")
    n = int(sys.argv[2])
    versions = int(sys.argv[3])
    name = sys.argv[4]
    lines = open_f.readlines()
    # print(n, lines, len(lines))
    if n > len(lines):
        raise Exception("El número de preguntas solicitadas es mayor que las preguntas aportadas")
    return versions, lines, n, name


def get_map(data):
    preguntas = dict()
    for line in data:
        sp_line = line.strip("\n").split("#")
        preguntas[sp_line[0]] = sp_line[1:]
    return preguntas


def generate_random_test(data_map, n):
    preguntas = dict()
    respuestas = dict()
    indice_preguntas = sorted(generar_numeros_aleatorios(n, len(data_map) - 1))
    i = 0
    for p in data_map.keys():
        if i in indice_preguntas:
            resp, index = shuffle_and_find_zero_position(data_map[p])
            preguntas[p] = resp
            respuestas[p] = index
        i += 1
    return preguntas,  respuestas


def shuffle_and_find_zero_position(arr):
    resp = arr[0]
    random.shuffle(arr)
    zero_position = arr.index(resp)
    return arr, zero_position

def generar_numeros_aleatorios(n, x):
    # print(n, x)
    numeros = random.sample(range(x+1), n)
    # print(numeros)
    return numeros


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    versions, data, question_number, name = read_data()
    for i in range(versions):
        data_map = get_map(data)
        preguntas_test, respuestas_test = generate_random_test(data_map, question_number)
        # print(data_map)
        # print(preguntas_test)
        # print(respuestas_test)
        pdfwriter.generatePDF.generarTest(preguntas_test, respuestas_test, version=i)
        pdfwriter.generatePDF.generarTest(preguntas_test, respuestas_test, True, version=i, title=name)
    # print(generar_numeros_aleatorios(10, 11))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
