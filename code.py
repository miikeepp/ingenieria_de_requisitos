#Ejemplo # 2.5
class Terreno:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
baseTerreno = float(input("Ingresa la longitud de la base del terreno (En unidades): "))
alturaTerreno = float(input("Ingresa la altura del terreno (En unidades): "))
terreno = Terreno(baseTerreno, alturaTerreno)
area = terreno.calcular_area()
print(f"El area del terreno con forma A es: {area} unidades cuadradas.")
#Ejemplos # 2.7
class ProductorLeche:
    def __init__(self, litros):
        self.litros = litros  
    def ConvertirAGalones(self):
        return self.litros / 3.785
    def MostrarGalones(self):
        galones = self.ConvertirAGalones()
        print(f"El productor de leche produce {galones:.2f} galones")
#Ejemplos # 2.9 
class Trabajador:
    def __init__(self, HorasTrabajadas, PagoHoras):
        self.HorasTrabajadas = HorasTrabajadas
        self.PagoHoras = PagoHoras
    def Calcular_sueldo_Semanal(self):
        return self.HorasTrabajadas * self.PagoHoras
    horas = float(input("Ingrese el numero de horas trabajadas :"))
    pago = float(input("Ingresa el pago por semanas :"))
    Trabajador = Trabajador(horas, pago)
    SueldoSemanl = Trabajador.calcular_sueldo_semanal ()
    print(f"El sueldo semanal del trabajador es : {SueldoSemanl}.")