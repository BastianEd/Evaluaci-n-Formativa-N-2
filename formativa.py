'''
Mensaje para profe benja, le seré bien sincero no pude hacer que me salieran los Handroll que no pidió el cliente 😔

'''

#Dependencias de Python
import os, time

#Variables
Pikachu_Roll = 4500
Otaku_Roll = 5000
Pulpo_Venenoso_Roll = 5200
Anguila_Eléctrica_Roll = 4800
contador_productos = 0

while True:
    print(f'\n-- Menú Principal --\n1. Generar venta\n2. Detalle de Pedido \n3. Salir\n')
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print("Bienvenido a Sushi Delivery")
        print("Tiene Codio de descuento:")
        print("1.Si\n2.No")
        descuento = int(input("Ingrese una opción: "))
        if descuento == 1:
            Codigo_Dct = str(input('Ingrese un codigo de Descuento: '))
            #Calcular Descuentos
            if Codigo_Dct == 'soyotaku':
                print("Tienes un 10% de descuento")
                Descuento = 0.10
            else:
                print("código no válido")
        elif descuento == 2:  
            Descuento = 0.00
            
        time.sleep(1)
        os.system('cls')
        total = 0
        articulos = []
        while True:
            # Menu con los Productos
            print(f'\n-- Menú de venta --\n1. Pikachu Roll {Pikachu_Roll}\n2. Otaku Roll {Otaku_Roll}\n3. Pulpo Venen Roll {Pulpo_Venenoso_Roll}\n4.Anguila Eléctrica Roll {Anguila_Eléctrica_Roll}') 
            print("¿Qué desea ordenar?")
            opcion_producto = str(input("Ingrese el número del producto ( X para terminar): "))
            if opcion_producto.lower()  == "x":
                    time.sleep(1.2)
                    os.system('cls')
                    break
            elif int(opcion_producto) == 1:
                nombre_producto = "Pikachu Roll"
                precio = Pikachu_Roll
            elif int(opcion_producto) == 2:
                nombre_producto = "Otaku Roll"
                precio = Otaku_Roll
            elif int(opcion_producto) == 3:
                nombre_producto = "Pulpo Venenoso Roll"
                precio = Pulpo_Venenoso_Roll
            elif int(opcion_producto) == 4:
                nombre_producto = "Anguila Eléctrica Roll"
                precio = Anguila_Eléctrica_Roll
            else:
                print("Opción no válida, Intente nuevamente")
                continue
            cantidad = int(input(f"Ingrese la cantidad de {nombre_producto}: "))
            print(f'Ordenaste {cantidad} de {nombre_producto} ')
            print('...')
            time.sleep(1.2)
            os.system('cls')
            contador_productos += cantidad
            subtotal = precio * cantidad
            # pedido[nombre_producto] = pedido.get(nombre_producto, 0) + cantidad
            articulos.append((nombre_producto, (0 + cantidad), precio, subtotal))
            total += subtotal 
            total_con_descuento = total - ((total*Descuento)/100)
    
    if opcion == 2:
            print(f"******************************")
            print(f"TOTAL PRODUCTOS: {contador_productos}")
            print(f"******************************")
            for producto, cantidad, precio, subtotal in articulos:
                print(f"{producto} : {0 + cantidad}")
            print(f"******************************")
            print(f"Subtotal por pagar: {subtotal:.0f}")
            print(f"Descuento por código: {Descuento:.0f}")
            print(f"TOTAL: {total_con_descuento:.0f}")
    #Salir                
    elif opcion == 3:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, intente nuevamente.") 
