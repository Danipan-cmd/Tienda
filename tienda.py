from tkinter import Tk, StringVar, Frame, Label, OptionMenu, Entry, Button, Listbox, END, messagebox, Toplevel, Checkbutton, IntVar, ttk
import datetime

# Definición de clases
class Verduras:
    def __init__(self, verdura, precio_por_kilo): 
        self.verdura = verdura
        self.precio_por_kilo = precio_por_kilo

class Carnes: 
    def __init__(self, carne, precio_por_kilo):
        self.carne = carne
        self.precio_por_kilo = precio_por_kilo

class Aseos: 
    def __init__(self, aseo, precio, marca):
        self.aseo = aseo
        self.precio = precio
        self.marca = marca

class CarnesFrias: 
    def __init__(self, fria, precio, marca):
        self.fria = fria
        self.precio = precio
        self.marca = marca

class Panaderias: 
    def __init__(self, panaderia, precio,marca):
        self.panaderia = panaderia
        self.precio = precio
        self.marca=marca
        
class Lacteos: 
    def __init__(self, lacteo, precio, marca):
        self.lacteo = lacteo
        self.precio = precio
        self.marca = marca
        
class Tecnologias: 
    def __init__(self, tecnología, precio, marca, tipo):
        self.tecnología = tecnología
        self.precio = precio
        self.marca = marca
        self.tipo = tipo
class Festivo:
    def __init__(self, festivo, descuentos_marca):
        self.festivo = festivo
        self.descuentos_marca = descuentos_marca

festivos = [
    Festivo(26, {"Samsung": 0.10, "Alpina": 0.10}),
    Festivo(30, {"Lenovo": 0.12, "Aromatel": 0.10}),
    Festivo(10, {"FAB": 0.10, "Delipavo": 0.15}),
    Festivo(1, {"Cunit": 0.09, "Bimbo": 0.10}),
    Festivo(15, {"Fresscampo": 0.08, "Cunit": 0.11}),
    Festivo(20, {"Yogo Yogo": 0.10, "Clorox": 0.09}),
    Festivo(25, {"Samsung": 0.15, "Pietram": 0.06})
]

# Listas de productos
verduras = [
    Verduras("Tomate", 1700),
    Verduras("Zanahoria", 1600),
    Verduras("Lechuga", 1800),
    Verduras("Pepino", 1600),
    Verduras("Cebolla", 3200),
    Verduras("Pimenton", 3800),
    Verduras("Perejil", 14000)
]

carnes = [
    Carnes("Molida", 29000),
    Carnes("Costilla", 21000),
    Carnes("Panza", 23000),
    Carnes("Lengua", 22000),
    Carnes("Higado", 19000)
]

aseos = [
    Aseos("Detergente-1kg-FAB", 26000, "FAB"),
    Aseos("Limpiador-500LM-Aroxamn", 8800, "Aromax"),
    Aseos("Limpiador-600ml-Fabuloso", 4700, "Fabuloso"),
    Aseos("Blanqueador-1L-Clorox", 3800, "Clorox"),
    Aseos("Suavizante-300ML-Aromatel", 6200, "Aromatel"),
    Aseos("Suavizante-1L-Aromatel", 6200, "Aromatel")
]

carnes_frias = [
    CarnesFrias("Ranchera-x7-Cunit", 12000, "Ranchera"),
    CarnesFrias("Ranchera-x14-Cunit", 15000, "Ranchera"),
    CarnesFrias("Butifarra-x18-Cunit", 10000, "Cunit"),
    CarnesFrias("Chorizo-500g-cunit", 22000, "Cunit"),
    CarnesFrias("Jamon-400g-Delipavo", 10100, "Delipavo"),
    CarnesFrias("Jamonpollo-230gr-Macpollo", 13900, "Macpollo"),
    CarnesFrias("Jamonpollo-200gr-Pietram", 11900, "Pietram"),
    CarnesFrias("Mortadela460g", 10100, "Cunit")
]

panaderias = [
    Panaderias("Mogolla-x4-Guadalupe", 1200,"Guadalupe"),
    Panaderias("Pan tajado-550gr-Guadalupe", 1200,"Guadalupe"),
    Panaderias("Pan tajado-730gr-Bimbo",6400,"Bimbo"),
    Panaderias("Croissant-x5-Fresscampo", 5800,"Fresscampo"),
    Panaderias("Ponque Casero vainilla-220gr-Bimbo", 5600,"Bimbo"),
    Panaderias("Ponque Casero marmoleado-220gr-Bimbo", 5600,"Bimbo"),
]

lacteos=[
    Lacteos("Yogurt_bolsa-x8-Yogo", 4400, "Yogo Yogo"),
    Lacteos("Yogurt_bolsa-1L-Yogo", 6000, "Yogo Yogo"),
    Lacteos("Avena_Deslactosada",9100 , "Alpina"),
    Lacteos("Yox", 1700, "Alpina"),
    Lacteos("Bon Yurt", 2900, "Alpina"),
    Lacteos("Leche_entera", 5100, "Alpina"),
]

tecnologias = [
    Tecnologias("Smart_tv_40 Samsung", 7000000, "Samsung", "TV"),
    Tecnologias("Samsung Galaxy A54", 2200000, "Samsung", "Celular"),
    Tecnologias("Lenovo Ideapad 3", 2000000, "Lenovo", "Computador"),
    Tecnologias("Sony WH-1000XM4", 800000, "Sony", "Audífonos"),
    Tecnologias("PlayStation 5 (PS5)", 2200000, "Sony", "Consola")
]

# Días y descuentos
class Dia:
    def __init__(self, dia, descuentos_categoria):
        self.dia = dia
        self.descuentos_categoria = descuentos_categoria


dias = [
    Dia("Lunes", {"Verduras": 0.15}),
    Dia("Martes", {"Carnes": 0.20}),
    Dia("Miércoles", {"Aseos": 0.15}),
    Dia("Jueves", {"Carnes_frias": 0.15}),
    Dia("Viernes", {"Panaderias": 0.20}),
    Dia("Sábado", {"Lacteos": 0.25}),
    Dia("Domingo", {"Tecnología": 0.30})
]




# Categorías de productos
categorias = {
    "Verduras": verduras,
    "Carnes": carnes,
    "Aseos": aseos,
    "Carnes_frias": carnes_frias,
    "Panaderias": panaderias,
    "Tecnología": tecnologias,
    "Lacteos":lacteos
}

# Funciones de la interfaz
productos_agregados = []

def actualizar_productos(*args):
    categoria_seleccionada = categoria.get()
    productos = []

    if categoria_seleccionada == "Verduras":
        productos = [p.verdura for p in categorias[categoria_seleccionada]]
    elif categoria_seleccionada == "Carnes":
        productos = [p.carne for p in categorias[categoria_seleccionada]]
    elif categoria_seleccionada == "Aseos":
        productos = [p.aseo for p in categorias[categoria_seleccionada]]
    elif categoria_seleccionada == "Carnes_frias":
        productos = [p.fria for p in categorias[categoria_seleccionada]]
    elif categoria_seleccionada == "Panaderias":
        productos = [p.panaderia for p in categorias[categoria_seleccionada]]
    elif categoria_seleccionada == "Tecnología":
        productos = [p.tecnología for p in categorias[categoria_seleccionada]]
    elif categoria_seleccionada == "Lacteos":
        productos = [p.lacteo for p in categorias[categoria_seleccionada]]

    producto.set('')
    menu = producto_menu["menu"]
    menu.delete(0, "end")
    for prod in productos:
        menu.add_command(label=prod, command=lambda value=prod: producto.set(value))

def agregar_producto():
    dia_seleccionado = Desp.get()
    festivo_seleccionado = DespFestivo.get()  # Asegúrate de usar la variable correcta para el festivo
    categoria_seleccionada = categoria.get()
    producto_seleccionado = producto.get()
    
    try:
        cantidad_seleccionada = float(cantidad.get())
        if cantidad_seleccionada <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
    except ValueError as e:
        messagebox.showerror("Error", f"Cantidad inválida: {e}")
        return

    # Buscar el descuento del día de la semana
    descuentos_categoria = {}
    for d in dias:
        if d.dia == dia_seleccionado:
            descuentos_categoria = d.descuentos_categoria
            break
    
    # Buscar el descuento del día festivo
    descuentos_marca = {}
    for f in festivos:
        if f.festivo == int(festivo_seleccionado):  # Convertir a entero para comparar
            descuentos_marca = f.descuentos_marca
            break

    # Calcular el precio total y descuento aplicado
    precio_total = 0
    kilos = 0
    descuento_aplicado_categoria = 0
    descuento_aplicado_marca = 0
    productos = categorias[categoria_seleccionada]
    for p in productos:
        if (categoria_seleccionada == "Verduras" and p.verdura == producto_seleccionado) or \
           (categoria_seleccionada == "Carnes" and p.carne == producto_seleccionado) or \
           (categoria_seleccionada == "Aseos" and p.aseo == producto_seleccionado) or \
           (categoria_seleccionada == "Carnes_frias" and p.fria == producto_seleccionado) or \
           (categoria_seleccionada == "Panaderias" and p.panaderia == producto_seleccionado) or \
           (categoria_seleccionada == "Tecnología" and p.tecnología == producto_seleccionado) or \
           (categoria_seleccionada == "Lacteos" and p.lacteo == producto_seleccionado):
           
            if categoria_seleccionada in ["Verduras", "Carnes"]:
                precio_total = p.precio_por_kilo * cantidad_seleccionada
                kilos = cantidad_seleccionada
            else:
                precio_total = p.precio * cantidad_seleccionada

            # Aplicar descuento por categoría
            descuento_aplicado_categoria = precio_total * descuentos_categoria.get(categoria_seleccionada, 0)
            precio_total -= descuento_aplicado_categoria

            # Aplicar descuento adicional por marca si el producto tiene atributo marca
            if hasattr(p, 'marca'):
                descuento_aplicado_marca = precio_total * descuentos_marca.get(p.marca, 0)
                precio_total -= descuento_aplicado_marca

            break

    # Verificar si el producto ya ha sido agregado
    for i, (prod, cant, precio, kg, desc) in enumerate(productos_agregados):
        if prod == producto_seleccionado:
            # Actualizar la cantidad y el precio total
            nueva_cantidad = cant + cantidad_seleccionada
            nuevo_precio_total = (precio / cant) * nueva_cantidad
            descuento_total = desc + descuento_aplicado_categoria + descuento_aplicado_marca

            productos_agregados[i] = (prod, nueva_cantidad, nuevo_precio_total, kg + kilos, descuento_total)
            actualizar_lista()
            return

    # Guardar producto agregado con descuento si no estaba antes
    productos_agregados.append((producto_seleccionado, cantidad_seleccionada, precio_total, kilos, descuento_aplicado_categoria + descuento_aplicado_marca))
    actualizar_lista()


def validar_entrada(texto):
    return texto.isdigit() or (texto.startswith('-') and texto[1:].isdigit()) or texto == ""

def actualizar_lista():
    lista_productos.delete(0, END)
    total = 0
    for producto, cantidad, precio, kilos, descuento in productos_agregados:
        if kilos > 0:
            if descuento > 0:
                lista_productos.insert(END, f"{producto} (x{kilos} kg): ${precio:.2f}")
                lista_productos.insert(END, f"  Descuento: ${descuento:.2f}")
            else:
                lista_productos.insert(END, f"{producto} (x{kilos} kg): ${precio:.2f}")
        else:
            if descuento > 0:
                lista_productos.insert(END, f"{producto} (x{cantidad} unidades): ${precio:.2f}")
                lista_productos.insert(END, f"  Descuento: ${descuento:.2f}")
            else:
                lista_productos.insert(END, f"{producto} (x{cantidad} unidades): ${precio:.2f}")
        total += precio
    total_label.config(text=f"Total: ${total:.2f}")

def validar_usuario(usuario, contrasena):
    return usuario == "admin" and contrasena == "1092024"

def abrir_ventana_eliminar():
    def validar_y_abrir():
        usuario = entrada_usuario.get()
        contrasena = entrada_contrasena.get()
        if validar_usuario(usuario, contrasena):
            ventana_acceso.destroy()
            abrir_ventana_seleccion()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    ventana_acceso = Toplevel(raiz)
    ventana_acceso.title("Acceso Administrador")
    ventana_acceso.geometry("300x200")
    
    Label(ventana_acceso, text="Usuario:").pack(pady=5)
    entrada_usuario = Entry(ventana_acceso)
    entrada_usuario.pack(pady=5)
    
    Label(ventana_acceso, text="Contraseña:").pack(pady=5)
    entrada_contrasena = Entry(ventana_acceso, show="*")
    entrada_contrasena.pack(pady=5)
    
    Button(ventana_acceso, text="Ingresar", command=validar_y_abrir).pack(pady=10)

def abrir_ventana_seleccion():
    def eliminar_seleccionados():
        seleccionados = [i for i, var in enumerate(var_list) if var.get()]
        for i in sorted(seleccionados, reverse=True):
            productos_agregados.pop(i)
        actualizar_lista()
        ventana_eliminar.destroy()

    ventana_eliminar = Toplevel(raiz)
    ventana_eliminar.title("Eliminar Productos")
    ventana_eliminar.geometry("500x400")

    Label(ventana_eliminar, text="Selecciona los productos a eliminar:").pack(pady=10)

    var_list = []
    for producto, cantidad, precio, kilos, descuento in productos_agregados:
        var = IntVar()
        Checkbutton(ventana_eliminar, text=f"{producto} (x{cantidad}) - ${precio:.2f}", variable=var).pack(anchor="w")
        var_list.append(var)

    Button(ventana_eliminar, text="Eliminar Seleccionados", command=eliminar_seleccionados).pack(pady=20)

def generar_factura():
    fecha = datetime.datetime.now().strftime("%d/%m/%Y")
    factura = f"Factura - {fecha}\n"
    factura += "-" * 80 + "\n"  # Ampliar la línea divisoria para ajustarse al nuevo ancho
    factura += f"{'Producto':<35} {'Cantidad':<10} {'Precio Unitario':<15} {'Descuento':<15} {'Total':<15}\n"
    factura += "-" * 80 + "\n"
    
    total = 0
    for producto, cantidad, precio, kilos, descuento in productos_agregados:
        if kilos > 0:
            precio_unitario = precio / kilos
            descuento_str = f"${descuento:.2f}" if descuento > 0 else "N/A"
            factura += f"{producto:<35} {kilos:<10} {precio_unitario:<15.2f} {descuento_str:<15} ${precio:.2f}\n"
        else:
            precio_unitario = precio / cantidad
            descuento_str = f"${descuento:.2f}" if descuento > 0 else "N/A"
            factura += f"{producto:<35} {cantidad:<10} {precio_unitario:<15.2f} {descuento_str:<15} ${precio:.2f}\n"
        total += precio

    factura += "-" * 80 + "\n"
    factura += f"{'Total':<60} ${total:.2f}\n"

    # Guardar la factura en un archivo con nombre único basado en fecha y hora
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"factura_{timestamp}.txt"

    with open(nombre_archivo, "w") as f:
        f.write(factura)

    messagebox.showinfo("Factura Generada", f"Factura guardada como {nombre_archivo}")
    reiniciar()


def reiniciar():
    Desp.set("")
    DespFestivo.set("")
    categoria.set("")
    producto.set("")
    cantidad.set("")
    productos_agregados.clear()
    actualizar_lista()

# Configuración de la interfaz gráfica
raiz = Tk()
raiz.title("Caja Registradora")
raiz.geometry("800x600")
raiz.configure(background="#f7f7f7")

raiz.state('zoomed')

# Crear contenedor principal
frame_principal = Frame(raiz, bg="#f7f7f7")
frame_principal.pack(expand=True, fill="both")

# Contenedor izquierdo para la selección de productos
frame_izquierdo = Frame(frame_principal, bg="#ffffff", relief="solid", borderwidth=2)
frame_izquierdo.pack(side="left", fill="y", padx=20, pady=20)

# Estilos
estilo = ttk.Style()
estilo.configure("TLabel", font=("Arial", 12), background="#ffffff")
estilo.configure("TButton", font=("Arial", 12), padding=6)
estilo.configure("TEntry", font=("Arial", 12), padding=6)

Label(frame_izquierdo, text="Día de la semana", font=("Arial", 14, "bold"), bg="#ffffff").grid(column=0, row=0, pady=10)
Desp = StringVar(raiz)
Desp.set("")
opciones = [d.dia for d in dias]
OptionMenu(frame_izquierdo, Desp, *opciones).grid(column=1, row=0, pady=10)

Label(frame_izquierdo, text="Día festivo", font=("Arial", 14, "bold"), bg="#ffffff").grid(column=0, row=1, pady=10)
DespFestivo = StringVar(raiz)
DespFestivo.set("")  
opciones_festivo = [f.festivo for f in festivos]
OptionMenu(frame_izquierdo, DespFestivo, *opciones_festivo).grid(column=1, row=1, pady=5)

Label(frame_izquierdo, text="Categoría", font=("Arial", 14, "bold"), bg="#ffffff").grid(column=0, row=2, pady=5)
categoria = StringVar(raiz)
categoria.set("")
categoria_menu = OptionMenu(frame_izquierdo, categoria, *categorias.keys())
categoria_menu.grid(column=1, row=2, pady=5)
categoria.trace("w", actualizar_productos)

Label(frame_izquierdo, text="Producto", font=("Arial", 14, "bold"), bg="#ffffff").grid(column=0, row=3, pady=5)
producto = StringVar(raiz)
producto_menu = OptionMenu(frame_izquierdo, producto, [])
producto_menu.grid(column=1, row=3, pady=5)

Label(frame_izquierdo, text="Cantidad", font=("Arial", 14, "bold"), bg="#ffffff").grid(column=0, row=4, pady=5)
cantidad = StringVar(raiz)
entrada = StringVar()
validacion = raiz.register(validar_entrada)
Entry(frame_izquierdo, textvariable=entrada, validate="key", validatecommand=(validacion, '%P'), width=10).grid(column=1, row=4, pady=5)
Entry(frame_izquierdo, textvariable=cantidad, width=10).grid(column=1, row=4, pady=5)

Button(frame_izquierdo, text="Agregar Producto", command=agregar_producto).grid(column=0, row=5, columnspan=2, pady=10)
Button(frame_izquierdo, text="Eliminar", command=abrir_ventana_eliminar).grid(column=0, row=6, columnspan=2, pady=10)
Button(frame_izquierdo, text="Generar Factura", command=generar_factura).grid(column=0, row=7, columnspan=2, pady=10)

# Contenedor derecho para la lista de productos agregados y total
frame_derecho = Frame(frame_principal, bg="#ffffff", relief="solid", borderwidth=2)
frame_derecho.pack(side="right", fill="both", expand=True, padx=20, pady=20)

Label(frame_derecho, text="Productos Agregados", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=10)
lista_productos = Listbox(frame_derecho, font=("Arial", 12), bg="#f0f0f0", selectmode="single")
lista_productos.pack(fill="both", expand=True, pady=10)

total_label = Label(frame_derecho, text="Total: $0.00", font=("Arial", 14, "bold"), bg="#ffffff")
total_label.pack(pady=10)

raiz.mainloop()

