# Contructor de labores
class Labores:
  def __init__(self, codigo, nombre, tiempo):
    self.codigo = codigo
    self.nombre = nombre
    self.tiempo = tiempo
    
    #getters
    def getCodigo(self):
      return self.codigo
    
    def getNombre(self):
      return self.nombre
    
    def getTiempo(self):
      return self.tiempo
    
    #setters
    def setCodigo(self, codigo):
      self.codigo = codigo
      
    def setNombre(self, nombre):
      self.nombre = nombre
      
    def setTiempo(self, tiempo):
      self.tiempo = tiempo
    
    