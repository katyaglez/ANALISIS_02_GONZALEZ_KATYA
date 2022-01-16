import csv

# Esta simple funcion te devuelve el promedio de la columna
# 'total_value' para una lista de datos.


def calculadora_promedio_valor(datos):
    num_datos = len(datos)
    total = 0
    for row in datos:
        valor = row[9]
        total += valor
    promedio = total / num_datos
    return promedio


def analizar(dict):
    analisis = []
    for llave in dict:
        # En la variable 'analisis'
        # guardaremos una lista de varias
        # sublistas de la forma:
        # [llave, promedio]
        #   - llave: es el nombre de la categoria
        #     que se analiza
        #   - promedio: el resultado de la funcion
        #     promedio aplicada al conjunto de datos
        sub_lista = [llave]
        promedio_valor = calculadora_promedio_valor(dict[llave])
        sub_lista.append(f'Promedio de \'total value\': {promedio_valor}')

        # Puedes dise;ar mas funciones que hagan operaciones
        # sobre un conjunto de datos, como unicamente un conteo,
        # encontrar el valor mas grande, etc.

        # Concluimos el analisis y lo agregamos al resto
        analisis.append(sub_lista)
    # al final regresamos una lista con el analisis de cada
    # llave del diccionario de categorias
    return analisis

# Esta funcion divide los datos de acuerdo a la lista
# de parametros que se le indique por ejemplo
# [1, 2, 3, 7]
# Dividiria la lista de datos en 'direction', 'origin',
# 'destination' y 'transport_mode'
# Recibe una lista y entrega un diccionario,
# donde cada llave es el nombre de la columna
# y el valor para esa llave es una lista de listas,
# que contiene los datos pertenecientes a esa llave o
# 'categoria'


def divisor(datos, cols):
    datos_separados = {}
    for row in datos:
        vals = []
        for col in cols:
            vals.append(row[col])
        key = '-'.join(vals)
        if key not in datos_separados:
            datos_separados[key] = [row]
        else:
            datos_separados[key].append(row)
    return datos_separados


def procesador(datos):
    # Paso 1, separar el string
    # en una lista de strings
    datos_paso_1 = []
    for renglon in datos:
        renglon_separado = renglon.split(',')
        datos_paso_1.append(renglon_separado)
        # print(renglon_separado)
    # Paso 2, remover caracteres indeseados.
    # Estos pueden ser espacios al principio
    # o final de cada string, igual que
    # caracteres especiales '\n', '\r', '\t'
    datos_paso_2 = []
    for lista in datos_paso_1:
        lista_limpia = []
        for elemento in lista:
            elemento_limpio = elemento.strip()
            lista_limpia.append(elemento_limpio)
        datos_paso_2.append(lista_limpia)
        # print(lista_limpia)
    # Finalmente convertimos en numero entero
    # a los strings que podrian ser numeros
    # (id, year, total_value)
    datos_paso_3 = []
    for lista in datos_paso_2:
        lista_con_conversiones = []
        for elemento in lista:
            # Realizamos esta conversion unicamente
            # si se cumple la condicion de
            # .isdigit() o sea entero.
            if elemento.isdigit():
                elemento = int(elemento)
            # A pesar de que haya hecho o no
            # la conversion, agregamos el elemento
            # a nuestra lista.
            lista_con_conversiones.append(elemento)
        datos_paso_3.append(lista_con_conversiones)
        # print(lista_con_conversiones)
    # Retornamos esta lista como resultado de la funcion
    return datos_paso_3


def lector():
    # Lista vacia, donde guardaremos cada dato
    syn_log_db = []

    with open('synergy_logistics_database.csv', 'r', newline='') as sldb:
        # Leemos sldb con la funcion csv.reader()
        db = csv.reader(sldb, delimiter=',')
        # Saltamos el encabezado del CSV,
        # Lo que nos interesa son los datos
        # unicamente, al mismo tiempo podemos hacer
        # la exploracion del tipo de dato
        primer_elemento = next(db)
        # tipo = type(primer_elemento)
        # print(tipo)
        # Cada elemento de 'db' es una lista.
        # <class 'list'>
        for row in sldb:
            syn_log_db.append(row)
    # Como resultado de la funcion, retornamos
    # el contenido del csv en forma de lista
    return syn_log_db


def main():
    db = lector()
    # Mini muestra para ver el resultado de la funcion lector:
    # for row in db[:5]:
    #     print(row, type(row))
    # Lo que nos retorna es una lista de strings, que
    # cambiaremos a una lista con variables independientes
    # usando la funcion procesador

    db = procesador(db)
    # Mini muestra para ver el resultado de la funcion procesador:
    # for row in db[:5]:
    #     print(row)
    # Como resultado obtenemos una lista de listas que
    # contienen cada conjunto de valores de una entrada.

    # Dividamos los datos 'db' en las categorias de exportaciones
    # e importaciones antes de continuar, la columna que indica
    # esta direccion es la numero 1:
    div_por_direccion = divisor(db, [1])
    # veamos las 'llaves' que usaremos para identificar
    # cada lista dentro del diccionario:
    llaves = div_por_direccion.keys()
    # for llave in llaves:
    #     print(llave)
    # Si deseas revisar que contiene el diccionario para cada
    # llave
    # for llave in llaves:
    #     print(f'\n\t{llave}:\n')
    #     print(div_por_direccion[llave][:5])
    # Ahora hagamos un peque;o analisis a estos datos:
    analisis = analizar(div_por_direccion)
    # for analisis_de_categoria in analisis:
    #     print(analisis_de_categoria)
    
    # Finalmente un ejemplo donde esta todo junto:
    # para los medios de transporte
    # prueba cambiar los elementos de la lista [7],
    # agrega mas columnas por ejemplo [1, 7] para 
    # dividir el dataset en 'direction' y 
    # 'total_value' al mismo tiempo
    div_por_medio = divisor(db, [7])
    analisis = analizar(div_por_medio)
    # especio en blanco antes de imprimir
    print('\n' * 3)
    for a in analisis:
        titulo = a[0]
        print(f'\tAnalisis de: {titulo}:')
        for resultado_de_operacion in a[1:]:
            print(resultado_de_operacion)
        print('\n')
    # la anterior manera de imprimir el analisis
    # puede encapsularse en una funcion, intenta
    # desarrollarla
    # pista: los argumentos/parametros de la funcion
    # es unicamente la variable 'analisis'


if __name__ == '__main__':
    main()
