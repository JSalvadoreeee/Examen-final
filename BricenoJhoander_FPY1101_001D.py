productos={
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7','Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD','1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen3', 'Nvidia GTX1050'],

}
stock={
    '8475HD': [387990,10],
    '2175HD': [327990,4],
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21],
    '123FHD': [290890,32],
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1],
    'FS1230HD': [249990,0],
}
def stock_marca(marca):
    total_stock=0
    marca=marca.lower()
    for modelo, detalles in productos.items():
        if detalles[0].lower()==marca:
            total_stock+=stock.get(modelo, [0, 0])[1]
            print(f"El stock es: {total_stock}")
def busqueda_precio(p_min, p_max):
    resultado=[]
    for modelo, datos_stock in stock.items():
        precio, cantidad=datos_stock
        if p_min<=precio<=p_max and cantidad>0:
            marca=productos[modelo][0]
            resultado.append(f"{marca} - {modelo}")
    if resultado:
        resultado.sort()
        print("Los notebooks entre los precios consultados son:", resultado)
    else:
        print("No hay notebooks en ese rango de precios.")
def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0]= nuevo_precio
        return True
    else:
        return False
def menu():
    while True:
        print("\n***MENÚ PRINCIPAL***\n1. Stock marca.\n2. BUsqueda por precio.\n3. Actualizar precio.\n4. Salir")
        opcion=input("Ingrese una opción: ")
        if opcion == "1":
            marca=input("Ingrese marca a consultar: ")
            stock_marca(marca)
        elif opcion == "2":
            while True:
                try:
                    p_min=int(input("Ingrese precio minimo: "))
                    p_max=int(input("Ingrese precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros.")
            busqueda_precio(p_min, p_max)
        elif opcion == "3":
            while True:
                modelo=input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio=int(input("Ingrese precio nuevo: "))
                    actualizado=actualizar_precio(modelo, nuevo_precio)
                    if actualizado:
                        print("Precio actualizado")
                    else:
                        print("El modelo no existe")
                except ValueError:
                    print("Debe ingresar un precio valido")
                    continue
                seguir = input("Desea actualizar otro precio (s/n)?: ").lower()
                if seguir != "si":
                    break
        elif opcion== "4":
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción valida.")

menu()