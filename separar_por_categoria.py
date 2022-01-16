import csv


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


def divisor(datos, columnas_divisoras):
    datos_separados = {}
    # Renglon por renglon vamos a encontrar
    # en las columnas indicadas el valor
    # categorico (en direction sera export o import
    # en transport_mode sera sea, air, etc)
    for renglon in datos:
        # En esta lista guardaremos la categoria del
        # renglon, que es la combinacion de 1 o mas
        # columnas
        categoria = []
        for columna in columnas_divisoras:
            categoria.append(renglon[columna])
        # Convertimos esa lista llamada categoria
        # en un string, usamos la funcion 'join'
        # que nos permite decirle con que caracter unir
        # la lista, en este caso un guion -
        key = '-'.join(categoria)
        # Para guardar los datos por separado, usamos un diccionario
        # esto nos permite recordar el nombre de cada categoria
        # usando el metodo .keys() en el diccionario
        if key not in datos_separados:
            datos_separados[key] = [renglon]
        else:
            datos_separados[key].append(renglon)
    return datos_separados


def main():
    # Primero leemos el archivo con
    # 'with- open'
    # Nos vamos a apoyar de una variable que
    # guardara los datos en bruto:
    synlog_db_raw = []

    with open('synergy_logistics_database.csv', 'r', newline='') as synergy_db_csv:
        # Leemos sldb con la funcion csv.reader()
        db = csv.reader(synergy_db_csv)
        # Nos brincamos el primer elemento, que es el encabezado
        # aqui el nombre de la variable es guion bajo, es una
        # practica comun llamar variables como guin bajo cuando
        # no se planea usar
        _ = next(db)

        # Ahora guardamos el resto de lineas en nuestra lista
        for line in db:
            synlog_db_raw.append(line)

    print('\nMini muestra para ver lo que guardamos en nuestra variable inicial:')
    for elemento in synlog_db_raw[:5]:
        print(elemento)

    # Convertimos el ultimo elemento de nuestras listas en
    # numero entero, y tenemos la base de datos procesada
    # y lista para operar
    synlog_db = []
    for lista in synlog_db_raw:
        # Convertimos el ultimo elemento en entero
        lista[-1] = int(lista[-1])
        # Guardamos en la lista nueva
        synlog_db.append(lista)

    print('\nMini muestra para ver como quedo despues de la conversion:')
    for row in synlog_db[:5]:
        print(row)
    # Como resultado obtenemos una lista de listas que
    # contienen cada conjunto de valores de una entrada.

    # Dividamos los datos 'db' en las categorias de exportaciones
    # e importaciones antes de continuar, la columna que indica
    # esta direccion es la numero 1:
    div_por_direccion = divisor(synlog_db, [1])
    print('\nVeamos las llaves que usaremos para identificar cada lista dentro del diccionario:')
    llaves = div_por_direccion.keys()
    for llave in llaves:
        print(llave)
    print('\nSi deseas revisar que contiene el diccionario para una llave en especifico:')
    subconjunto = div_por_direccion['Exports']
    for elemento in subconjunto[:5]:
        print(elemento)

    # Ahora separemos la base de datos limpia de nuevo, por medio
    # de transporte, que es la columna 7 (comenzando a contar desde 0)
    # y direccion de envio:
    dir_transp = divisor(synlog_db, [1, 7])
    print('\nVeamos las llave:')
    for llave in dir_transp.keys():
        print(llave)

    # Un peque;o codigo que imprime los primeros 2 renglones
    # de cada llave
    for llave in dir_transp.keys():
        print('\nCategoria: ', llave)
        renglones = dir_transp[llave]
        for renglon in renglones[:2]:
            print(renglon)


if __name__ == '__main__':
    main()
