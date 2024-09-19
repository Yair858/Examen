class Persona:
    def __init__(self, nombre,):
        self.nombre = nombre
        self.distancia_recorrida = None
    def caminar(self):
        self.distancia_recorrida += 2 

class atleta(Persona):
    def __init__(self,nombre):
        super().__init_(nombre)
        self.calorias_consumidas = None
    
    def entrenar(self, distancia=10):
        self.distancia_recorrida += distancia 
        self.distancia_recorrida += distancia * 500
    
    def competir(self, distancia=50):
        self.distancia_recorrida += distancia
        self.distancia_recorrida += distancia * 750 
                 

import unittest
class tetsPersona(unittest.TestCase):
    def entrenar(self):
        p = Persona('Juan')
        p.caminar()
        self.assertEqual(p.distancia_recorrida, 2)

class testAtleta(unittest.TestCase):
    
    def test_entrenar_con_distancia(self):
        a = atleta('Juan')
        a.entrenar(10)
        self.assertEqual(a.distancia_recorrrida,10)
        self.assertEqual(a.calorias_consumidas,5000)
 
    def test_competir_con_distancia(self):
        a = atleta('Juan')
        a.competir(20)
        self.assertEqual(a.distancia_recorrrida,20)
        self.assertEqual(a.calorias_consumidas,15000)

if __name__ =='__main__':
    unittest.main()
