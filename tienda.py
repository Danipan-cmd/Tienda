from tkinter import Tk, StringVar, OptionMenu, Label, Entry, Button, Listbox, END, Frame, messagebox, font
from tkinter import ttk

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
    Dia("Domingo", {"Tecnologia": 0.30})
]

# Categorías de productos
categorias = {
    "Verduras": verduras,
    "Carnes": carnes,
    "Aseos": aseos,
    "Carnes_frias": carnes_frias,
    "Panaderias": panaderias
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

    producto.set(productos[0])
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

    # Calcular el precio total
    precio_total = 0
    kilos = 0
    productos = categorias[categoria_seleccionada]
    for p in productos:
        if (categoria_seleccionada == "Verduras" and p.verdura == producto_seleccionado) or \
           (categoria_seleccionada == "Carnes" and p.carne == producto_seleccionado) or \
           (categoria_seleccionada == "Aseos" and p.aseo == producto_seleccionado) or \
           (categoria_seleccionada == "Carnes_frias" and p.fria == producto_seleccionado) or \
           (categoria_seleccionada == "Panaderias" and p.panaderia == producto_seleccionado):
            if categoria_seleccionada in ["Verduras", "Carnes"]:
                precio_total = p.precio_por_kilo * cantidad_seleccionada
                kilos = cantidad_seleccionada
            else:
                precio_total = p.precio * cantidad_seleccionada
            descuento = descuentos_dia.get(categoria_seleccionada, 0)
            precio_total -= precio_total * descuento
            break

    # Guardar producto agregado
    productos_agregados.append((producto_seleccionado, cantidad_seleccionada, precio_total, kilos))
    actualizar_lista()

def actualizar_lista():
    lista_productos.delete(0, END)
    total = 0
    for producto, cantidad, precio, kilos in productos_agregados:
        if kilos > 0:
            lista_productos.insert(END, f"{producto} (x{kilos} kg): ${precio:.2f}")
        else:
            lista_productos.insert(END, f"{producto} (x{cantidad} unidades): ${precio:.2f}")
        total += precio
    total_label.config(text=f"Total: ${total:.2f}")

def reiniciar():
    global productos_agregados
    productos_agregados = []
    lista_productos.delete(0, END)
    total_label.config(text="Total: $0.00")
    cantidad.set("")
    producto.set("")

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
categoria.set("Verduras")
categoria_menu = OptionMenu(frame_izquierdo, categoria, *categorias.keys())
categoria_menu.grid(column=1, row=1, pady=5)
categoria.trace("w", actualizar_productos)

Label(frame_izquierdo, text="Producto", font=("Arial", 14, "bold"), bg="#ffffff").grid(column=0, row=2, pady=5)
producto = StringVar(raiz)
producto_menu = OptionMenu(frame_izquierdo, producto, [])
producto_menu.grid(column=1, row=2, pady=5)

Label(frame_izquierdo, text="Cantidad", font=("Arial", 14, "bold"), bg="#ffffff").grid(column=0, row=3, pady=5)
cantidad = StringVar(raiz)
Entry(frame_izquierdo, textvariable=cantidad).grid(column=1, row=3, pady=5)

Button(frame_izquierdo, text="Agregar Producto", command=agregar_producto).grid(column=0, row=4, columnspan=2, pady=10)
Button(frame_izquierdo, text="Reiniciar", command=reiniciar).grid(column=0, row=5, columnspan=2, pady=10)

# Contenedor derecho para mostrar los productos
frame_derecho = Frame(frame_principal, bg="#ffffff", relief="solid", borderwidth=2)
frame_derecho.pack(side="right", fill="both", expand=True, padx=20, pady=20)

Label(frame_derecho, text="Productos Agregados", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=10)
lista_productos = Listbox(frame_derecho, width=50, height=15, font=("Arial", 12), bg="#f0f0f0", selectmode="single")
lista_productos.pack(pady=10)

total_label = Label(frame_derecho, text="Total: $0.00", font=("Arial", 14, "bold"), bg="#ffffff")
total_label.pack(pady=10)

raiz.mainloop()
