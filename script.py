print("Hola mundo")
'''* Declara una clase Vehiculo con las siguientes propuedades:
  num_bastidor  y peso. Los métodos son:

   * impuestobase():depende del peso, y se calcula con la siguiente formula:
      0.45*peso.

* Existen dos clases que heredan de vehiculo: Electrico y combustion. El objeto electrico tiene como propiedad precio, y el objeto combustión la propiedad cilidrada. Los vehiculos electricos tributan 9% de su precio más el impuesto base, mientras que los vehiculos de combustión tributan el triple de su cilindrada más el impuesto base. implementa un método en ambas subclases que calcules el impuesto total en ambos casos

* Instancia 2 vehiculos de cada tipo y muesta el impuesto que se paga'''
#Creamos la clase padre vehiculo

class vehiculo:

  def __init__(self,num_bastador,peso):

    self.num_bastidor=num_bastador
    self.peso=peso

  #def impuesto_base(self):
   # impuesto_base=0.45*self.peso
    #return impuesto_base

  def __str__(self):
    print(f'EL vehiculo con peso {self.peso} y el numero de bastidores {self.num_bastidor}')

  def impuesto_base(self):
    return 0.45*self.peso
v1=vehiculo(4,6000)

#Creamos la clase hija electrico
class electrico(vehiculo):
  def __init__(self,num_bastidor,peso,precio):
    super().__init__(num_bastidor,peso)
    self.precio=precio

  def impuesto_total(self):
    return self.precio*0.09 + super().impuesto_base


  def __str__(self):
    return super().__str__ + f" Vehiculo electrico de precio:{self.precio} "

#Creamos la clase hija combustible
class combustion(vehiculo):
  def __init__(self,num_bastidor,peso,cilindrada):
    super().__init__(num_bastidor,peso)
    self.cilindrada=cilindrada

  def impuesto_total(self):
    return self.cilindrada*3 + super().impuesto_base

  def __str__(self):
    return super().__str___ + f" Vehiculo combustion de cilindrada:{self.cilindrada} "

e1=electrico(8,250,20000)
e2=electrico(10,500,50000)
c1=combustion(5,400,2600)
c2=combustion(3,1000,1500)

vehiculos=[e1,e2,c1,c2]

for x in range(len(vehiculos)):
  print(vehiculos[x])
  print(vehiculos[x].impuesto_total())
