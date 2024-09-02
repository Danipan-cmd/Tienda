from tkinter import Tk, StringVar, OptionMenu, Label, Entry, Button, Listbox, END

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
    cantidad_seleccionada = float(cantidad.get())

    # Buscar el día seleccionado
    descuentos_dia = {}
    for d in dias:
        if d.dia == dia_seleccionado:
            descuentos_dia = d.descuentos
            break

    # Calcular el precio total
    precio_total = 0
    productos = categorias[categoria_seleccionada]
    for p in productos:
        if (categoria_seleccionada == "Verduras" and p.verdura == producto_seleccionado) or \
           (categoria_seleccionada == "Carnes" and p.carne == producto_seleccionado) or \
           (categoria_seleccionada == "Aseos" and p.aseo == producto_seleccionado) or \
           (categoria_seleccionada == "Carnes_frias" and p.fria == producto_seleccionado) or \
           (categoria_seleccionada == "Panaderias" and p.panaderia == producto_seleccionado):
            precio_total = p.precio_por_kilo * cantidad_seleccionada if categoria_seleccionada in ["Verduras", "Carnes"] else p.precio * cantidad_seleccionada
            descuento = descuentos_dia.get(categoria_seleccionada, 0)
            precio_total -= precio_total * descuento
            break

    # Guardar producto agregado
    productos_agregados.append((producto_seleccionado, precio_total))
    actualizar_lista()

def actualizar_lista():
    lista_productos.delete(0, END)
    for producto, precio in productos_agregados:
        lista_productos.insert(END, f"{producto}: ${precio:.2f}")

# Configuración de la interfaz gráfica
raiz = Tk()
raiz.title("Caja Registradora")
raiz.geometry("500x500")
raiz.configure(background="#aba6a4")

Label(raiz, text="Introduce el día de la semana", font=("Arial", 14)).grid(column=0, row=0, padx=10, pady=10)
Desp = StringVar(raiz)
Desp.set(dias[0].dia)
OptionMenu(raiz, Desp, *[d.dia for d in dias]).grid(column=1, row=0, padx=10, pady=10)

Label(raiz, text="Selecciona la categoría", font=("Arial", 14)).grid(column=0, row=1, padx=10, pady=10)
categoria = StringVar(raiz)
categoria.set("Verduras")
OptionMenu(raiz, categoria, *categorias.keys(), command=actualizar_productos).grid(column=1, row=1, padx=10, pady=10)

Label(raiz, text="Selecciona el producto", font=("Arial", 14)).grid(column=0, row=2, padx=10, pady=10)
producto = StringVar(raiz)
producto_menu = OptionMenu(raiz, producto, "")
producto_menu.grid(column=1, row=2, padx=10, pady=10)
actualizar_productos()

Label(raiz, text="Introduce la cantidad (kg/unidades)", font=("Arial", 14)).grid(column=0, row=3, padx=10, pady=10)
cantidad = StringVar(raiz)
Entry(raiz, textvariable=cantidad).grid(column=1, row=3, padx=10, pady=10)

Button(raiz, text="Agregar Producto", command=agregar_producto).grid(column=0, row=4, columnspan=2, pady=10)

Label(raiz, text="Productos Agregados", font=("Arial", 14)).grid(column=0, row=5, padx=10, pady=10)
lista_productos = Listbox(raiz, width=50, height=10)
lista_productos.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

raiz.mainloop()
