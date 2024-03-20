# Constructor de cultivos

class Cultivos:
  def __init__(self, codigo, nombre, area, cultivo):
    self.codigo = codigo
    self.nombre = nombre
    self.area = area
    self.cultivo = cultivo
    
    #getters
    def getCodigo(self):
      return self.codigo
    
    def getNombre(self):
      return self.nombre
    
    def getArea(self):
      return self.area
    
    def getCultivo(self):
      return self.cultivo
    
    def getLabores(self):
      return self.labores
    
    #setters
    def setCodigo(self, codigo):
      self.codigo = codigo
      
    def setNombre(self, nombre):
      self.nombre = nombre
    
    def setArea(self, area):
      self.area = area
    
    def setCultivo(self, cultivo):
      self.cultivo = cultivo