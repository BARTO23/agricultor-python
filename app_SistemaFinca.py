import cls_agricultor as Agricultor
import cls_cultivos as Cultivos
import cls_labores as Labores
agricultores = []
cultivos = []
labores = []

# Menu del sistema
input("Bienvenido al sistema de Agricultura, presione enter para continuar")

while(True):
  print(f"""
            Menu Nuevo Registro \n\n
            1. Registrar Agricultor \n
            2. Registrar Cultivo \n
            3. Registrar Labor \n
            4. Salir \n
            """)
  opcion = input("Seleccione una opcion: ")

  if (opcion == "1"):
      id = input("Ingrese la identificacion del agricultor: ")
      nombre = input("Ingrese el nombre del agricultor: ")
      contacto = input("Ingrese el contacto del agricultor: ")
      finca = input("Ingrese la finca del agricultor: ")
      agricultor = Agricultor.Agricultor(id, nombre, contacto, finca)
      agricultores.append(agricultor)
      print("El agricultor ha sido registrado")
      input("Presione enter para continuar" )

  elif(opcion == "2"):
    codigo = input("Ingrese el codigo del cultivo: ")
    nombre = input("Ingrese el nombre del cultivo: ")
    area = input("Ingrese el area del cultivo: ")
    cultivo = input("Ingrese el tipo de cultivo: ")
    cultivo = Cultivos.Cultivos(codigo, nombre, area, cultivo)
    print("El cultivo ha sido registrado")
    
  elif(opcion == "3"):
    codigo_labor = input("Ingrese el codigo de la labor: ")
    nombre_labor = input("Ingrese el nombre de la labor: ")
    tiempo = input("Ingrese el tiempo de la labor: ")
    labor = Labores.Labores(codigo_labor, nombre_labor, tiempo)
    labores.append(labor)
    print("La labor ha sido registrada")
    
  elif(opcion == "4"):
    print("Gracias por usar el sistema")
    break
    
  
 

