def areaRect(largo, ancho):
    area=largo*ancho
    return area

def perimetroRect(la, an):
    perimetro=(la+an)*2
    return perimetro


def main_2():
    ll=(float(input('Dame el largo: ')))
    aa=(float(input('Dame el ancho: ')))
    clave= input('Escribe "a" para el area o "p" para el perimetro')
    if clave =='a':
        ar=areaRect(ll, aa)
        print('El area es:  ' + str(ar))
    elif clave == "p":
        pe= perimetroRect(ll, aa)
        print('El perimetro es:  ' + str(pe))
    
    else:
        print('Opcion no valida')
        
main_2()
