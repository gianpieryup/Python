# Diccionario para almacenar el inventario
inventario = {}
contador_codigo = 1

def mostrar_menu():
    """Muestra el menú principal."""
    print("Menú para la Gestión de Productos:\n")
    print("1. Registro: Alta de productos nuevos.")
    print("2. Búsqueda: Consulta de datos de un producto específico.")
    print("3. Actualización: Modificar los datos de un producto.")
    print("4. Eliminación: Dar de baja productos.")
    print("5. Listado: Listado completo de los productos en la base de datos.")
    print("6. Reporte de Bajo Stock: Lista de productos con cantidad bajo mínimo.")
    print("7. Salir.")

def registrar_producto():
    """Registra un nuevo producto en el inventario."""
    global contador_codigo
    print("\nRegistro de Producto Nuevo")
    
    nombre = input("Nombre del producto: ").strip()
    descripcion = input("Descripción del producto: ").strip()
    
    # Validar el precio
    while True:
        try:
            precio = float(input("Precio del producto: "))
            if precio > 0:
                break
            print("El precio debe ser mayor a 0.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número decimal mayor a 0.")

    # Validar el stock
    while True:
        try:
            cantidad = int(input("Cantidad en stock: "))
            if cantidad >= 0:
                break
            print("El stock no puede ser negativo.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número entero.")

    categoria = input("Categoría del producto: ").strip()

    # Registrar producto en el inventario
    inventario[f"PROD-{contador_codigo}"] = {
        "nombre": nombre,
        "descripcion": descripcion,
        "cantidad": cantidad,
        "precio": precio,
        "categoria": categoria
    }
    print(f"Producto registrado con éxito. Código asignado: PROD-{contador_codigo}")
    contador_codigo += 1

def mostrar_productos():
    """Muestra todos los productos en el inventario."""
    print("\nListado Completo de Productos")
    if not inventario:
        print("El inventario está vacío. No hay productos registrados.")
    else:
        for codigo, datos in inventario.items():
            print(f"Código: {codigo}")
            print(f"  Nombre      : {datos['nombre']}")
            print(f"  Descripción : {datos['descripcion']}")
            print(f"  Cantidad    : {datos['cantidad']}")
            print(f"  Precio      : ${datos['precio']:.2f}")
            print(f"  Categoría   : {datos['categoria']}")
            print("-" * 50)

def actualizar_producto():
    """Actualiza los datos de un producto existente."""
    print("\nActualizar Producto")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()

    if codigo in inventario:
        print(f"Producto encontrado: {inventario[codigo]['nombre']}")
        print("Ingrese los nuevos datos del producto (presione Enter para dejar sin cambios).")
        
        nuevo_nombre = input("Nuevo nombre: ").strip()
        nueva_descripcion = input("Nueva descripción: ").strip()

        # Validar nueva cantidad
        while True:
            nueva_cantidad = input("Nueva cantidad en stock: ").strip()
            if not nueva_cantidad:
                break
            try:
                nueva_cantidad = int(nueva_cantidad)
                if nueva_cantidad >= 0:
                    break
                print("La cantidad no puede ser negativa.")
            except ValueError:
                print("Entrada no válida. Debe ser un número entero.")
        
        # Validar nuevo precio
        while True:
            nuevo_precio = input("Nuevo precio: ").strip()
            if not nuevo_precio:
                break
            try:
                nuevo_precio = float(nuevo_precio)
                if nuevo_precio > 0:
                    break
                print("El precio debe ser mayor a 0.")
            except ValueError:
                print("Entrada no válida. Debe ser un número decimal.")
        
        nueva_categoria = input("Nueva categoría: ").strip()

        # Actualizar los datos
        if nuevo_nombre:
            inventario[codigo]["nombre"] = nuevo_nombre
        if nueva_descripcion:
            inventario[codigo]["descripcion"] = nueva_descripcion
        if nueva_cantidad != '':
            inventario[codigo]["cantidad"] = nueva_cantidad
        if nuevo_precio != '':
            inventario[codigo]["precio"] = nuevo_precio
        if nueva_categoria:
            inventario[codigo]["categoria"] = nueva_categoria

        print("Producto actualizado con éxito.")
    else:
        print(f"No se encontró un producto con el código {codigo}.")

def eliminar_producto():
    """Elimina un producto del inventario."""
    print("\nEliminar Producto")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()

    if codigo in inventario:
        del inventario[codigo]
        print(f"Producto con código {codigo} eliminado exitosamente.")
    else:
        print(f"No se encontró un producto con el código {codigo}.")

def buscar_producto():
    """Busca un producto en el inventario por su código y muestra su información."""
    print("\nBuscar Producto")
    codigo = input("Ingrese el código del producto que desea buscar: ").strip()

    if codigo in inventario:
        producto = inventario[codigo]
        print(f"\nProducto encontrado con el código: {codigo}")
        print(f"  Nombre      : {producto['nombre']}")
        print(f"  Descripción : {producto['descripcion']}")
        print(f"  Cantidad    : {producto['cantidad']}")
        print(f"  Precio      : ${producto['precio']:.2f}")
        print(f"  Categoría   : {producto['categoria']}")
        print("-" * 50)
    else:
        print(f"No se encontró un producto con el código {codigo}.")

def reporte_bajo_stock():
    """Genera un reporte de productos con cantidad igual o inferior a un límite."""
    print("\nReporte de Bajo Stock")
    
    while True:
        try:
            limite = int(input("Ingrese el límite de stock para el reporte: "))
            if limite >= 0:
                break
            print("El límite de stock no puede ser negativo. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")

    print(f"\nProductos con stock igual o inferior a {limite}:")
    productos_en_bajo_stock = [
        (codigo, datos) for codigo, datos in inventario.items() if datos["cantidad"] <= limite
    ]

    if not productos_en_bajo_stock:
        print("No hay productos con stock igual o inferior al límite especificado.\n")
    else:
        for codigo, producto in productos_en_bajo_stock:
            print(f"Código: {codigo}")
            print(f"  Nombre      : {producto['nombre']}")
            print(f"  Descripción : {producto['descripcion']}")
            print(f"  Cantidad    : {producto['cantidad']}")
            print(f"  Precio      : ${producto['precio']:.2f}")
            print(f"  Categoría   : {producto['categoria']}")
            print("-" * 50)

# Programa principal
while True:
    mostrar_menu()
    try:
        opcion = int(input("Por favor, seleccione una opción (1-7): "))

        if opcion == 7:
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        elif opcion == 1:
            registrar_producto()
        elif opcion == 2:
            buscar_producto()
        elif opcion == 3:
            actualizar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            mostrar_productos()
        elif opcion == 6:
            reporte_bajo_stock()
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 7.")

    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número del 1 al 7.")

    print("\n")  # Salto de línea para mejor visualización
