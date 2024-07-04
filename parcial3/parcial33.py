def registrar_usuario():
    print("\n***** Bienvenido a SurExplora *****")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    ciudad = input("Ingrese su ciudad de origen: ")
    
    while True:
        tour = input("Ingrese su destino (Torres del Paine/Carretera Austral/Chiloé): ")
        if tour.lower() in ['torres del paine', 'carretera austral', 'chiloé']:
            break
        else:
            print("Destino no válido. Por favor ingrese uno de los destinos permitidos.")
    
    while True:
        try:
            cantidad_personas = int(input("Ingrese la cantidad de personas para el tour: "))
            if cantidad_personas > 0:
                break
            else:
                print("La cantidad de personas debe ser mayor que cero.")
        except ValueError:
            print("Por favor ingrese un número válido para la cantidad de personas.")

    with open('datostour.txt', 'a' , encoding='utf-8') as file:
        file.write(f"{nombre}, {apellido}, {ciudad}, {tour}, {cantidad_personas}\n")

    print(f"Usuario {nombre} {apellido}, ingresado correctamente.\n")




def lista_reserva():
    print("***** Listado de reservas *****")
    try:
        with open('datostour.txt', 'r', encoding='utf-8') as file:
            for l in file:
                nombre, apellido, ciudad, tour, cantidad_personas = l.strip().split(', ')
                print(f"Nombre: {nombre}, Apellido: {apellido}, Ciudad: {ciudad}, Destino: {tour}, Cantidad de Personas: {cantidad_personas}")
    except FileNotFoundError:
        print("Aun no hay reservas registradas")


def detalle_por_destino():
    print("\nBuscar tour por Destino")
    tour_buscar = input("Introduce el destino a buscar: ")
    found = False

    try:
        with open('datostour.txt', 'r', encoding='utf-8') as file:
            for l in file:
                nombre, apellido, ciudad, tour, cantidad_personas= l.strip().split(', ')
                if tour.lower() == tour_buscar.lower():
                    print(f"Nombre: {nombre}, Apellido: {apellido}, Ciudad: {ciudad}, Destino: {tour}, Cantidad de personas: {cantidad_personas}")
                    found = True
            if not found:
                print(f"No se encontró tour al destino {tour_buscar}")
    except FileNotFoundError:
        print("Aun no hay reservas registradas")


def main():
    while True:
        print("1. Registrar Reserva")
        print("2. Listar Todas las Reservas")
        print("3. Imprimir Detalle de Reserva por Destino")
        print("4. Salir del programa")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            lista_reserva()
        elif opcion == '3':
            detalle_por_destino()
        elif opcion == '4':
            print("Hasta luego, saliendo del programa")
            break  
        else:
            print("Opción no válida. Por favor ingrese una opción del 1 al 4.\n")


if __name__ == '__main__':
    main()
