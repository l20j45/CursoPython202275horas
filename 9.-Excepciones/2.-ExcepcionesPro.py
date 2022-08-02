if __name__ == '__main__':
    resultado = None

    try:
        a = int(input('Primero numero: '))
        b = int(input('Segundo numero: '))
        resultado=a/b
    except ZeroDivisionError as e:
       print(f'Zero ocurrio un error {e}, {type(e)}')
    except TypeError as e:
        print(f'Type ocurrio un error {e}, {type(e)}')
    except Exception as e:
        print(f'Padre ocurrio un error {e}, {type(e)}')
    else:
        print('no hubi ningun error pa')
    finally:
        print('se ejecuto el bloque finally')
    print(f'Ressultado: {resultado}')
    print('Continuamos')