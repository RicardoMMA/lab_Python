#Diccionarios
MiDiccionario= {
    'Nombre': "John Connor" , "Edad": 22, "Ciudad" :"Barranquilla"}

#Acceder al valor del diccionario
nombre = MiDiccionario[ "Nombre"]
print("Diccionario Inicial: ", MiDiccionario)

#Modoficar
MiDiccionario["Profesion"]="Estudiante"
MiDiccionario ["Edad"]=25
print ("Diccionario modificado:", MiDiccionario)
print (nombre)
MiDiccionario["Genero Musical"]= "Diomedez"
print(MiDiccionario)