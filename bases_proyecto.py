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

# Esta funcion hace un analisis donde
# cuenta la longitud de valores de cada llave,
# del diccionario que se le proporciona. Regresa el top
# 'n' elementos que desees.


def analisis_conteo(datos, top_n):
    # La lista de llaves unicas son:
    nombres = datos.keys()
    # Encontremos la cantidad de repeticiones que hay
    # por cada categoria, guardamos el dato en par con
    # su nombre
    analisis_completo = []
    for nombre in nombres:
        repeticiones = len(datos[nombre])
        par = (repeticiones, nombre)
        analisis_completo.append(par)

    # Encontremos la suma del conteo total:
    suma_del_total = sum(repeticiones for repeticiones, _ in analisis_completo)

    # Ordenamos de menor a mayor
    analisis_completo = sorted(analisis_completo, reverse=True)

    # Escogemos el top
    top = analisis_completo[:top_n]
    # Encontramos la suma del conteo del top
    suma_del_top = sum(repeticiones for repeticiones, _ in top)

    # Calculamos el porcentaje que representa el top, dentro de
    # el total de datos
    porcentaje = 100 * (suma_del_top/suma_del_total)
    # Redondeamos el porcentaje a 2 decimas
    porcentaje = round(porcentaje, 2)

    # Regresamos los resultados:
    return porcentaje, top


def analisis_valor_total(datos, top_n):
    # La lista de llaves unicas son:
    nombres = datos.keys()
    # Por cada llave sumaremos el total_value de todos
    # los renglones que tenga, para conocer el valor total
    # que aporta esa categoria
    analisis_completo = []
    for nombre in nombres:
        # Primero la lista de los datos
        lista = datos[nombre]
        # Una sublista de todos los total_value, recordemos
        # que este dato es el ultimo elemento de cada renglon
        sublist_tot_value = [renglon[-1] for renglon in lista]
        # Sumamos todos los valores de esta lista
        suma_valor_total = sum(sublist_tot_value)
        par = (suma_valor_total, nombre)
        analisis_completo.append(par)

    # Encontremos la suma de toda de total_value de la lista entera de datos:
    suma_del_total = sum(
        suma_valor_total for suma_valor_total, _ in analisis_completo)

    # Ordenamos de menor a mayor
    analisis_completo = sorted(analisis_completo, reverse=True)

    # Escogemos el top
    top = analisis_completo[:top_n]
    # Encontramos la suma del conteo del top
    suma_del_top = sum(suma_valor_total for suma_valor_total, _ in top)

    # Calculamos el porcentaje que representa el top, dentro de
    # el total de datos
    porcentaje = 100 * (suma_del_top/suma_del_total)
    # Redondeamos el porcentaje a 2 decimas
    porcentaje = round(porcentaje, 2)

    # Regresamos los resultados:
    return porcentaje, top


def main():
    # Primero leemos el archivo con
    # 'with- open'
    # Nos vamos a apoyar de una variable (en este caso una
    # lista vacia) que
    # guardara los datos en bruto:
    synlog_db_raw = []

    with open('synergy_logistics_database.csv', 'r', newline='') as synergy_db_csv:
        # Leemos synergy_db_csv con la funcion csv.reader()
        db = csv.reader(synergy_db_csv)
        # Nos brincamos el primer elemento, que es el encabezado
        # aqui el nombre de la variable es guion bajo _ . Esto es una
        # practica en python, de nombrar variables como guion bajo cuando
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

    '''

        SECCION DE EJEMPLO
        Ejemplo de como usar el divisor de datos

    '''
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
    """
    
    
        TERMINA SECCION DE EJEMPLO

    
    """
    """
    
        SECCION DE EJEMPLO
        Ejemplo de como analizar un conjunto de datos.
        Caso: Explorando la opcion 1
    
    """
    # Quiero, para el primer ejercicio encontrar
    # las 10 rutas mas demandadas. Necesito dividir
    # la base de datos en primer lugar por direction.
    dividido_direction = divisor(synlog_db, [1])

    # Hagamos el analisis por cada llave (export, import):
    for llave in dividido_direction.keys():
        datos = dividido_direction[llave]
        # Dividimos los datos en las columnas de
        # origin,destination,transport_mode
        div_por_rutas = divisor(datos, [2, 3, 7])
        # queremos un top 10, definamos el 10 como variable.
        top_n = 10
        print(f'\n>>>>>\tAnalisis para {llave}:')
        """
        Primero el analisis de demanda, o sea la freciencia de
        uso de cada ruta
        """
        porcentaje, lista = analisis_valor_total(div_por_rutas, top_n)
        print(f'\n\tTop {top_n} rutas mas demandadas:')
        for ruta in lista:
            repeticiones = ruta[0]
            nombre = ruta[1]
            print(f'>{repeticiones}: {nombre}')
        print(
            f'\tLas previas {top_n} rutas representan el {porcentaje}% del total de demandas')
        """
        Ahora un analisis por valor de ingreso total
        """
        porcentaje, lista = analisis_valor_total(div_por_rutas, top_n)
        print(f'\n\tTop {top_n} rutas de mayor valor:')
        for num, ruta in enumerate(lista):
            nombre = ruta[1]
            print(f'>{num+1}: {nombre}')
        print(
            f'\tLas previas {top_n} rutas representan el {porcentaje}% del total del valor global')
    """
    

        TERMINA SECCION DE EJEMPLO


    """
    # Consigna para terminar el proyecto necesitas:
    # Para la opcion 2:
    #   - volver a crear un for como el anterior, ya que seguiremos
    #     analizando de acuerdo a importaciones y exportaciones
    #   - dividir los datos en la columna de transport_mode, ejemplo:
    #       div_transp_mode = divisor(datos, [7])
    #   - definir un top_n = 3
    #   - utilizar la funcion analisis_conteo() y analisis_valor_total()
    #     con los datos div_transp_mode y top_n.
    #   - efectivamente imprimir los resultados
    # Para la opcion 3:
    #   - Crear un for de nuevo, ya que seguiremos
    #     analizando de acuerdo a importaciones y exportaciones
    #   - dividir los datos en la columna de origin, ejemplo:
    #       div_origin = divisor(datos, [2])
    #   - definir dos top_n, por ejemplo:
    #       top_conteo, top_valor = 10, 10
    #   - utilizar la funcion analisis_conteo() y analisis_valor_total()
    #     con los datos div_transp_mode y top_conteo o top_valor.
    #   - el paso que varia en este caso es que deben ajustar ambos top
    #     a un numero mas grande o mas peque;o de paises, para obtener el
    #     numero adecuado de paises que representen el 80%  
    #   - efectivamente imprimir los resultados


    dividido_direction = divisor(synlog_db,[2])

    # Hagamos el analisis por cada llave (export, import):
    for llave in dividido_direction.keys():
        datos = dividido_direction[llave]
        # Dividimos los datos en las columnas de
        # transport mode
        div_transp_mode = divisor(datos, [2, 3, 7])
        
        top_n = 3
        print(f'\n>>>>>\tAnalisis para {llave}:')
        
        analisis_conteo, lista = analisis_conteo(div_transp_mode, top_n)
        print(f'\n\tTop {top_n} rutas mas demandadas:')
        for ruta in lista:
            repeticiones = ruta[0]
            nombre = ruta[1]
            print(f'>{repeticiones}: {nombre}')
        print(
            f'\tLos medios de transporte {top_n} representan el {analisis_conteo}% del total de medios usados')
        """
        Ahora un analisis por valor de ingreso total
        """
        analisis_conteo, lista = analisis_valor_total(div_transp_mode, top_n)
        print(f'\n\tTop {top_n} medios de transporte:')
        for num, ruta in enumerate(lista):
            nombre = ruta[1]
            print(f'>{num+1}: {nombre}')
        print(
            f'\tLas previas {top_n} medios de transporte representan el {analisis_conteo} del total del valor global')

    for llave in dividido_direction.keys():
        datos = dividido_direction[llave]
        # Dividimos los datos en las columnas de
        # origin,destination,transport_mode
        div_origin= divisor(datos, [2,])
    
        top_n = 10
        top_conteo,top_valor = 10,10
        print(f'\n>>>>>\tAnalisis para {llave}:')
       
        analisis_conteo, lista = analisis_conteo(div_origin, top_n)
        print(f'\n\tTop {top_n} rutas origen :')
        for ruta in lista:
            repeticiones = ruta[0]
            nombre = ruta[1]
            print(f'>{repeticiones}: {nombre}')
        print(
            f'\tLas previas {top_n} rutas representan el {analisis_conteo}% del total de demandas')
        
        analisis_conteo, lista = analisis_valor_total(div_origin, top_n)
        print(f'\n\tTop {top_n} rutas de mayor valor:')
        for num, ruta in enumerate(lista):
            nombre = ruta[1]
            print(f'>{num+1}: {nombre}')
        print(
            f'\tLas previas {top_n} rutas representan el {analisis_conteo}% del total del valor global')

            
if __name__ == '__main__':
    main()
