class MaquinaBateria:
    def __init__(self):
        self.tamaños = ["grande", "mediano", "pequeño"]
        self.cantidad_triturada = {"grande":0,"mediano":0,"pequeño":0}
        self.tamaño_seleccionado = ""
        pass
    def seleccionar_tamaño (self):
        numero_seleccionado = 0
        while (numero_seleccionado < 1 or numero_seleccionado > 3):
            print ("1.pequeño")
            print ("2.mediano")
            print ("3.grande")
            try:
                numero_seleccionado = int(input("Ingrese el numero correcto del tamaño: "))
                if numero_seleccionado < 1 or numero_seleccionado > 3:
                    raise Exception("el numero tiene que estar entre 1 y 3")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        self.tamaño_seleccionado = self.tamaños [3 - numero_seleccionado]#guardando el string  de self tamaño con una resta 

    def triturar_bat (self):
        if self.tamaño_seleccionado == "":
            print ("tienen que señalar un tamaño")
            return
         
        self.cantidad_triturada [self.tamaño_seleccionado] += 1 # cantidad triturada es = a cantidad triturada + 1
        print ("bateria de tamaño " + self.tamaño_seleccionado + " triturada")

    def sumergir (self):
        if self.cantidad_triturada ["grande"] + self.cantidad_triturada ["mediano"] + self.cantidad_triturada ["pequeño"] == 0:
            print ("No hay elementos para Sumergir")
            return
        print ("Se han sumergido con éxito " + str(self.cantidad_triturada ["grande"]) + " baterías grandes, " + str(self.cantidad_triturada ["mediano"]) + " baterías medianas y " + str(self.cantidad_triturada ["pequeño"]) + " baterías pequeñas.")
        self.cantidad_triturada ["pequeño"] = 0
        self.cantidad_triturada ["mediano"] = 0
        self.cantidad_triturada ["grande"] = 0

    def __str__(self):
        texto = "actualmente en la máquina hay " + str(self.cantidad_triturada ["grande"]) + " baterías grandes, " + str(self.cantidad_triturada ["mediano"]) + " baterías medianas y " + str(self.cantidad_triturada ["pequeño"]) + " baterías pequeñas."
        return texto 
        
        globa

MaquinaTrituradora = MaquinaBateria () 

print (MaquinaTrituradora)
MaquinaTrituradora.triturar_bat()
MaquinaTrituradora.seleccionar_tamaño()
MaquinaTrituradora.sumergir()
MaquinaTrituradora.triturar_bat()
MaquinaTrituradora.triturar_bat()
MaquinaTrituradora.triturar_bat()
MaquinaTrituradora.seleccionar_tamaño()
MaquinaTrituradora.triturar_bat()
MaquinaTrituradora.triturar_bat()
print (MaquinaTrituradora)
MaquinaTrituradora.sumergir()
print (MaquinaTrituradora)





 
#baterias = ["mediano","pequeño","grande","grande","pequeño","pequeño"]
