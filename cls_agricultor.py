#un agricultor, realiza diferentes labores de campo, las cuales pueden ser:
#- siembra
#- cosecha
#- aplicacion de fertilizante
#- aplicacion de matamalesa
# cada cultivo tiene la siguiente informacion:
#codigo, nombre, area (en metros cuadrador), cultivo; el agricultor debe ejecutar varias labores a los cultivos
#lo cual implica llevar un registro de cada vez que se realiza una labor en un cultivo

#del agricultor se tiene:
#- identificacion
#- nombre
#- contacto
#- finca

# labores: codigo, nombre y tiempo
# las labores son: 1: siembra, 2: cosecha, 3: aplicacion de fertilizante, 4: aplicacion de matamalesa

# Constructor de la clase

class Agricultor:
  def __init__(self, id, nombre, contacto, finca):
    self.id = id
    self.nombre = nombre
    self.contacto = contacto
    self.finca = finca
    self.labores = [0, "siembra", "cosecha", "aplicacion de fertilizante", "aplicacion de matamalesa"]
    
    
    #getters
    def getId(self):
      return self.identificacion
    
    def getNombre(self):
      return self.nombre
    
    def getContacto(self):
      return self.contacto
    
    def getFinca(self):
      return self.finca
    
    def getLabores(self):
      return self.labores
    
    #setters
    
    def setIdentificacion(self, identificacion):
      self.identificacion = identificacion
      
    def setNombre(self, nombre):
      self.nombre = nombre
      
    
    
    