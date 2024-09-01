from tkinter import Tk, StringVar, OptionMenu, Label
class Verduras:
    def __init__(self, verdura, precio_por_kilo): 
        self.verdura = verdura
        self.precio_por_kilo = precio_por_kilo
verdura1 = Verduras("Tomate", 1700)
verdura2 = Verduras("Zanahoria", 1600)
verdura3 = Verduras("Lechuga", 1800)
verdura4 = Verduras("Pepino", 1600)
verdura5 = Verduras("Cebolla", 3200)
verdura6 = Verduras("Pimenton", 3800)
verdura7 = Verduras("Perejil", 14000)


class Carnes: 
    def __init__(self, carne, precio_por_kilo):
        self.carne = carne
        self.precio_por_kilo = precio_por_kilo
carne1 = Carnes("Molida", 29000)
carne2 = Carnes("Costilla", 21000)
carne3 = Carnes("Panza", 23000)
carne4 = Carnes("Lengua", 22000)
carne5 = Carnes("Higado", 19000)

 
class Aseos: 
    def __init__(self, aseo, precio, marca):
        self.aseo = aseo
        self.precio = precio
        self.marca = marca
aseo1 = Aseos("Detergente", 26000, "FAB")
aseo2 = Aseos("Limpiador_piso", 8800, "Aromax")
aseo3 = Aseos("Limpiador", 4700, "Fabuloso")
aseo4 = Aseos("Blanqueador", 3800, "Clorox")
aseo5 = Aseos("Suavizante", 6200, "Aromatel")



class Carnes_frias: 
    def __init__(self, fria, precio, marca):
        self.fria = fria
        self.precio = precio
        self.marca = marca
fria1 = Carnes_frias("Rancherax7", 12000, "Salchicha ranchera")
fria2 = Carnes_frias("Butifarrax18", 10000, "Butifarra")
fria3 = Carnes_frias("Chorizo500g", 22000, "Chorizo")
fria4 = Carnes_frias("Jamon400g", 10100, "Jamon Ahumado")
fria5 = Carnes_frias("Jamonpollo230gr", 13900, "Jamon de Pollo")
fria6 = Carnes_frias("Mortadela460g", 10100, "Mortadela tradicional")



class panaderías: 
    def __init__(self, panadería, precio):
        self.panadería = panadería
        self.precio = precio
panadería1 = panaderías("Mogolla", 1200)
panadería2 = panaderías("Bimbonetes", 2100)
panadería3 = panaderías("Croissantx20", 5800)
panadería4 = panaderías("Ponque Casero", 5600)
panadería5 = panaderías("Pan tajado", 7300)


class lacteos: 
    def __init__(self, lacteo, precio, marca):
        self.lacteo = lacteo
        self.precio = precio
        self.marca = marca
lacteo1 = lacteos("Yogurt bolsa", 4400, "Yogo Yogo")
lacteo2 = lacteos("Avena Deslactosada",9100 , "Alpina")
lacteo3 = lacteos("Yox", 1700, "Alpina")
lacteo4 = lacteos("Bon Yurt", 2900, "Alpina")
lacteo5 = lacteos("Leche entera", 5100, "Alpina")

class tecnologías: 
    def __init__(self, tecnología, precio, marca):
        self.tecnología = tecnología
        self.precio = precio
        self.marca = marca
tecnología1 = tecnologías("Smart_tv_40", 700000000, "Samsung")
tecnología2 = tecnologías("Celular", 2200000, "Samsung Galaxy A54")
tecnología3 = tecnologías("Computador",2000000 , "Lenovo Ideapad 3")
tecnología4 = tecnologías("Audifonos", 1300000, "Sony WH-1000XM4")
tecnología5 = tecnologías("PlayStation 5 (PS5)",2200000 , "Samsung")

class dia:
    def __init__(self, dia, descuentos):
        self.dia = dia
        self.descuentos = descuentos
d1 = dia("Lunes", 0.15)
d2 = dia("Martes", 0.20)
d3 = dia("Miercoles", 0.15)
d4 = dia("Jueves", 0.15)
d5 = dia("Viernes", 0.20)
d6 = dia("Sabado", 0.25)
d7 = dia("Domingo", 0.30)   
raiz = Tk()
raiz.title("Ventas")
raiz.minsize(width=300, height=400)
etiqueta1 = Label(raiz, text="Introduce el día de la semana", font=("Arial", 14))
etiqueta1.grid (column=0,row=1)
raiz.geometry("300x300+1200+100")
raiz.configure (background="#aba6a4")
Desp=StringVar(raiz)
Desp.set("")
opciones = [d1.dia, d2.dia, d3.dia, d4.dia, d5.dia, d6.dia, d7.dia]
opcion = OptionMenu(raiz,Desp, *opciones)
opcion.grid(column=0,row=2)
etiqueta1 = Label(raiz, text="Intoducir producto", font=("Arial", 14))
etiqueta1.grid (column=0,row=3)
etiqueta1 = Label(raiz, text="Intoducir marca", font=("Arial", 14))
etiqueta1.grid (column=0,row=5)




raiz.mainloop()