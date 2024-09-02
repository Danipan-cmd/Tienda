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
    def __init__(self, panaderia, precio):
        self.panaderia = panaderia
        self.precio = precio
        
class Tecnologias: 
    def __init__(self, tecnología, precio, marca,tipo):
        self.tecnología = tecnología
        self.precio = precio
        self.marca = marca
        self.tipo=tipo

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
    Aseos("Detergente", 26000, "FAB"),
    Aseos("Limpiador_piso", 8800, "Aromax"),
    Aseos("Limpiador", 4700, "Fabuloso"),
    Aseos("Blanqueador", 3800, "Clorox"),
    Aseos("Suavizante", 6200, "Aromatel")
]

carnes_frias = [
    CarnesFrias("Rancherax7", 12000, "Salchicha ranchera"),
    CarnesFrias("Butifarrax18", 10000, "Butifarra"),
    CarnesFrias("Chorizo500g", 22000, "Chorizo"),
    CarnesFrias("Jamon400g", 10100, "Jamon Ahumado"),
    CarnesFrias("Jamonpollo230gr", 13900, "Jamon de Pollo"),
    CarnesFrias("Mortadela460g", 10100, "Mortadela tradicional")
]

panaderias = [
    Panaderias("Mogolla", 1200),
    Panaderias("Bimbonetes", 2100),
    Panaderias("Croissantx20", 5800),
    Panaderias("Ponque Casero", 5600),
    Panaderias("Pan tajado", 7300)
]

tecnologias= [
    Tecnologias("Smart_tv_40 Samgung", 7000000, "Samsung", "TV"),
    Tecnologias("Samsung Galaxy A54", 2200000, "Samsung","Celular"),
    Tecnologias("Lenovo Ideapad 3",2000000 , "Lenovo","Computador"),
    Tecnologias("Sony WH-1000XM4", 1300000, "Sony","Audifonos"),
    Tecnologias("PlayStation 5 (PS5)",2200000 , "Sony", "Consola")
]


# Días y descuentos
class Dia:
    def __init__(self, dia, descuentos):
        self.dia = dia
        self.descuentos = descuentos

dias = [
    Dia("Lunes", {"Verduras": 0.15}),
    Dia("Martes", {"Carnes": 0.20}),
    Dia("Miercoles", {"Aseos": 0.15}),
    Dia("Jueves", {"Carnes_frias": 0.15}),
    Dia("Viernes", {"Panaderias": 0.20}),
    Dia("Sabado", {"Lacteos": 0.25}),
    Dia("Domingo", {"Tecnología": 0.30})
]

# Categorías de productos
categorias = {
    "Verduras": verduras,
    "Carnes": carnes,
    "Aseos": aseos,
    "Carnes_frias": carnes_frias,
    "Panaderias": panaderias,
    "Tecnología":tecnologias
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
        productos= [p.tecnología for p in categorias[categoria_seleccionada]]

    producto.set('')
    menu = producto_menu["menu"]
    menu.delete(0, "end")
    for prod in productos:
        menu.add_command(label=prod, command=lambda value=prod: producto.set(value))

def agregar_producto():
    dia_seleccionado = Desp.get()
    categoria_seleccionada = categoria.get()
    producto_seleccionado = producto.get()
    
    try:
        cantidad_seleccionada = float(cantidad.get())
        if cantidad_seleccionada <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
    except ValueError as e:
        messagebox.showerror("Error", f"Cantidad inválida: {e}")
        return

    # Buscar el día seleccionado
    descuentos_dia = {}
    for d in dias:
        if d.dia == dia_seleccionado:
            descuentos_dia = d.descuentos
            break

    # Calcular el precio total y descuento aplicado
    precio_total = 0
    kilos = 0
    descuento_aplicado = 0
    productos = categorias[categoria_seleccionada]
    for p in productos:
        if (categoria_seleccionada == "Verduras" and p.verdura == producto_seleccionado) or \
           (categoria_seleccionada == "Carnes" and p.carne == producto_seleccionado) or \
           (categoria_seleccionada == "Aseos" and p.aseo == producto_seleccionado) or \
           (categoria_seleccionada == "Carnes_frias" and p.fria == producto_seleccionado) or \
           (categoria_seleccionada == "Panaderias" and p.panaderia == producto_seleccionado) or \
            (categoria_seleccionada == "Tecnología" and p.tecnología == producto_seleccionado):
            if categoria_seleccionada in ["Verduras", "Carnes"]:
                precio_total = p.precio_por_kilo * cantidad_seleccionada
                kilos = cantidad_seleccionada
            else:
                precio_total = p.precio * cantidad_seleccionada
            descuento = descuentos_dia.get(categoria_seleccionada, 0)
            descuento_aplicado = precio_total * descuento
            precio_total -= descuento_aplicado
            break

    # Guardar producto agregado con descuento
    productos_agregados.append((producto_seleccionado, cantidad_seleccionada, precio_total, kilos, descuento_aplicado))
    actualizar_lista()

def validar_entrada(texto):
     return texto.isdigit() or (texto.startswith('-') and texto[1:].isdigit()) or texto == ""

def actualizar_lista():
    lista_productos.delete(0, END)
    total = 0
    for producto, cantidad, precio, kilos, descuento in productos_agregados:
        if kilos > 0:
            lista_productos.insert(END, f"{producto} (x{kilos} kg): ${precio:.2f} (Descuento: ${descuento:.2f})")
        else:
            lista_productos.insert(END, f"{producto} (x{cantidad} unidades): ${precio:.2f} (Descuento: ${descuento:.2f})")
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
    ventana_eliminar.geometry("400x400")

    Label(ventana_eliminar, text="Selecciona los productos a eliminar:").pack(pady=10)

    var_list = []
    for producto, cantidad, precio, kilos, descuento in productos_agregados:
        var = IntVar()
        Checkbutton(ventana_eliminar, text=f"{producto} (x{cantidad}) - ${precio:.2f}", variable=var).pack(anchor="w")
        var_list.append(var)

    Button(ventana_eliminar, text="Eliminar Seleccionados", command=eliminar_seleccionados).pack(pady=20)

def generar_factura():
    factura = "Factura:\n"
    total = 0

    for producto, cantidad, precio, kilos, descuento in productos_agregados:
        if kilos > 0:
            factura += f"{producto} (x{kilos} kg): ${precio:.2f} (Descuento: ${descuento:.2f})\n"
        else:
            factura += f"{producto} (x{cantidad} unidades): ${precio:.2f} (Descuento: ${descuento:.2f})\n"
        total += precio
    
    factura += "-----------------------------\n"
    factura += f"Total: ${total:.2f}\n"

    # Guardar la factura en un archivo con nombre único basado en fecha y hora
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"factura_{timestamp}.txt"

    with open(nombre_archivo, "w") as f:
        f.write(factura)

    messagebox.showinfo("Factura Generada", f"Factura guardada como {nombre_archivo}")
    reiniciar()

def reiniciar():
    Desp.set("")
    categoria.set("")
    producto.set("")
    cantidad.set("")
    productos_agregados.clear()
    actualizar_lista()

# Configuración de la interfaz gráfica
raiz = Tk()
raiz.title("Caja Registradora")
raiz.geometry("700x500")
raiz.configure(background="#f7f7f7")

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

Label(frame_izquierdo, text="Categoría", font=("Arial", 14, "bold"), bg="#ffffff").grid(column=0, row=1, pady=5)
categoria = StringVar(raiz)
categoria.set("")
categoria_menu = OptionMenu(frame_izquierdo, categoria, *categorias.keys())
categoria_menu.grid(column=1, row=1, pady=5)
categoria.trace("w", actualizar_productos)

Label(frame_izquierdo, text="Producto", font=("Arial", 14, "bold"), bg="#ffffff").grid(column=0, row=2, pady=5)
producto = StringVar(raiz)
producto_menu = OptionMenu(frame_izquierdo, producto, [])
producto_menu.grid(column=1, row=2, pady=5)

Label(frame_izquierdo, text="Cantidad", font=("Arial", 14, "bold"), bg="#ffffff").grid(column=0, row=3, pady=5)
cantidad = StringVar(raiz)
entrada = StringVar()
validacion = raiz.register(validar_entrada)
Entry(frame_izquierdo, textvariable=entrada, validate="key", validatecommand=(validacion, '%P'))
Entry(frame_izquierdo, textvariable=cantidad).grid(column=1, row=3, pady=5)
Button(frame_izquierdo, text="Agregar Producto", command=agregar_producto).grid(column=0, row=4, columnspan=2, pady=10)

# Botón de eliminar
Button(frame_izquierdo, text="Eliminar", command=abrir_ventana_eliminar).grid(column=0, row=5, columnspan=2, pady=10)

# Contenedor derecho para la lista de productos agregados y total
frame_derecho = Frame(frame_principal, bg="#ffffff", relief="solid", borderwidth=2)
frame_derecho.pack(side="right", fill="both", expand=True, padx=20, pady=20)

Label(frame_derecho, text="Productos Agregados", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=10)
lista_productos = Listbox(frame_derecho, width=50, height=15, font=("Arial", 12), bg="#f0f0f0", selectmode="single")
lista_productos.pack(pady=10)

total_label = Label(frame_derecho, text="Total: $0.00", font=("Arial", 14, "bold"), bg="#ffffff")
total_label.pack(pady=10)
Button(frame_izquierdo, text="Generar Factura", command=generar_factura).grid(column=0, row=6, columnspan=2, pady=10)

raiz.mainloop()