import time
import numpy as np
import sys

#imprimir con retraso
def imprimir_con_retraso(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def validacion_movimiento():
        while True:
                try:
                    i = int(input('Elige un movimiento: '))
                    if i <= 0 or i >= 5:
                        print("Vuelve a selecionar movimiento")
                    else:
                        return i  
                except TypeError:
                    print("Error, vuelve a selecionar")
                except ValueError:
                    print("Error, vuelve a selecionar")


#Clases------------------------------------------------
#clase para crear pokemon
class Pokemon():
    
    def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud ='======================='):
        #guardar variables y atributos del pokemon
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['ataque']
        self.defensa = EVs['defensa']
        self.puntos_de_salud = puntos_de_salud
        self.barras = 20

    def impresa(self, Pokemon2):
        "'Imprimir informacion de lucha'"
        print("----BATALLA POKEMON----")
        print(f"\n{self.nombre}")
        print("tipo/",self.tipos)
        print("Ataque/", self.ataque)
        print("Defensa/", self.defensa)
        print("Nv./", 3*(1+np.mean([self.ataque,self.defensa])))
        print("\nVS")
        print(f"\n{Pokemon2.nombre}")
        print("tipo/", Pokemon2.tipos)
        print("ataque/", Pokemon2.ataque)
        print("Defensa/", Pokemon2.defensa)
        print("Nv./", 3*(1+np.mean([Pokemon2.ataque,Pokemon2.defensa])))
        time.sleep(2)


    def ventaja(self,Pokemon2):
        #Ventajas del tipo de pokemon
        version = ['fuego','agua','planta']
        
        for i,k in enumerate(version):
            #son del mismo tipo 
            if self.tipos == k:
                if Pokemon2.tipos == k:
                    cadena_1_ataque = "\nNO es muy efectivo..."
                    cadena_2_ataque = "\nNO es muy efectivo..."
                
            #Pokemon2 es fuerte
            if Pokemon2.tipos == version[(i+1)%3]:
                Pokemon2.ataque *= 2
                Pokemon2.defensa *= 2
                self.ataque /= 2
                self.defensa /= 2
                cadena_1_ataque = '\nNO es muy efectivo...'
                cadena_2_ataque = '\nEs muy efectivo!'
                
            #Pokemon2 es debil
            if Pokemon2.tipos == version[(i+2)%3]:
                self.ataque *=2
                self.defensa *=2
                Pokemon2.ataque /=2
                Pokemon2.defensa /=2
                cadena_1_ataque = '\nEs muy efectivo!'
                cadena_2_ataque = '\nNo es muy efectivo...'
            
            return cadena_1_ataque, cadena_2_ataque

    

    def turno(self, Pokemon2, cadena_1_ataque, cadena_2_ataque):
        #Compara los puntos de salud de los pokemones
        while (self.barras > 0) and (Pokemon2.barras > 0):
            #imprimir los puntos de salud de cada pokemon
            imprimir_con_retraso(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}\n")
            imprimir_con_retraso(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")

            #Pokemon 1------------------------------------------------------------------------------------------------------------
            imprimir_con_retraso(f"Adelante {self.nombre}!\n")
            for i, x in enumerate(self.movimientos):
                print(f"{i+1}.", x)
            
            #Evaluar que selecione los movimientos de la lista
            index = validacion_movimiento()
                
            imprimir_con_retraso(f"\n{self.nombre} uso {self.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_1_ataque)

            # Determinar el dano
            Pokemon2.barras -= self.ataque
            Pokemon2.puntos_de_salud = ""

            #agregar barras adicionales
            for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.puntos_de_salud += "="
            
            time.sleep(2)
            #imprimir los puntos de salud de cada pokemon
            imprimir_con_retraso(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}\n")
            imprimir_con_retraso(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
            time.sleep(.5)

            #Combrobar si ganaste
            if Pokemon2.barras <= 0:
                imprimir_con_retraso("\n..." + Pokemon2.nombre + ' se debilito, ya no puede continuar.')
                break

        #Pokemon 2--------------------------------------------------------------------------------------------------------------
            imprimir_con_retraso(f"Adelante {Pokemon2.nombre}!\n")
            for i, x in enumerate(Pokemon2.movimientos):
                print(f"{i+1}.", x)
            
            #Evaluar que selecione los movimientos de la lista
            index = validacion_movimiento()
            
            imprimir_con_retraso(f"\n{Pokemon2.nombre} uso {Pokemon2.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_2_ataque)

            # Determinar el dano
            self.barras -= Pokemon2.ataque
            self.puntos_de_salud = ""

            #agregar barras adicionales
            for j in range(int(self.barras+.1*self.defensa)):
                self.puntos_de_salud += "="
            
            time.sleep(2)
            #imprimir los puntos de salud de cada pokemon
            imprimir_con_retraso(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}\n")
            imprimir_con_retraso(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
            time.sleep(.5)

            #Combrobar si ganaste
            if self.barras <= 0:
                imprimir_con_retraso("\n..." + self.nombre + ' se debilito, ya no puede continuar.')
                break

    def lucha(self, Pokemon2):
        #imprimir informacion de la lucha
        self.impresa(Pokemon2)

        #Considerar las ventajas
        cadena_1_ataque, cadena_2_ataque = self.ventaja(Pokemon2)

        #Ahora la lucha
        self.turno(Pokemon2,cadena_1_ataque,cadena_2_ataque)

        dinero = np.random.choice(5000)
        imprimir_con_retraso(f"\nEl oponente te paga ${dinero}.\n")


if __name__ == '__main__':
    #Crear Pokemon
    
    
    Charizard = Pokemon('Charizard', 'fuego', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ataque':12, 'defensa': 8})
    Blastoise = Pokemon('Blastoise', 'agua', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ataque': 10, 'defensa':10})
    Venusaur = Pokemon('Venusaur', 'planta', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ataque':9, 'defensa':12})

    #Charmander = Pokemon('Charmander', 'fuego', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ataque':4, 'defensa':2})
    #Squirtle = Pokemon('Squirtle', 'agua', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ataque': 3, 'defensa':3})
    #Bulbasaur = Pokemon('Bulbasaur', 'planta', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ataque':2, 'defensa':4})

    #Charmeleon = Pokemon('Charmeleon', 'fuego', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ataque':6, 'defensa':5})
    #Wartortle = Pokemon('Wartortle', 'agua', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ataque': 5, 'defensa':5})
    #Ivysaur = Pokemon('Ivysaur\t', 'planta', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ataque':4, 'defensa':6})

    pok = [Charizard,Blastoise,Venusaur]
    
    imprimir_con_retraso(f"Duelo Pokemon\nSelecione sus pokemon\n")
    print("[1]Charizard\n[2]Blastoise\n[3]Venusaur\n")
    j1 = int(input("Entrenador 1: "))
    j2 = int(input("Entrenador 2: "))
    
    pok[j1-1].lucha(pok[j2-1])
    

    #Charizard.lucha(Blastoise) # listos para luchar