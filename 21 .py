import random

def hacerpinta(pinta, numero):
    if numero <= 10 and numero > 1:
        return [[numero, pinta]]+hacerpinta(pinta, numero+1)
    else:
        if numero == 1:
            return[["A", pinta]]+hacerpinta(pinta, numero+1)
        else:
             if numero > 10:
                  if numero == 11:
                        return [["J", pinta]]+hacerpinta(pinta, numero+1)
                  else:
                        if numero == 12:
                             return [["Q", pinta]]+hacerpinta(pinta, numero+1)
                        else:
                            if numero ==13:
                                 return [["K", pinta]]+hacerpinta(pinta, numero+1)
                            else:
                                if numero >= 14:
                                    return []
                 
           
       

def hacernaipecompleto():
    return hacerpinta("diamante",1)+hacerpinta("corazones",1)+hacerpinta("picas",1)+hacerpinta("trebol",1)



def barajar(lista):
    random.shuffle(lista)
    return lista

def sacarprimeracarta(lista):
    return [lista.pop(0)]


    
def sacarvalor(lista):
    if lista[0]=="J" or lista[0]=="Q" or lista[0]=="K":
        return 10
    else:
        if lista[0]=="A":
            return 11
        else:
            return lista[0]
            
        
def sacardelista(lista, n, funcion):
    if n < len(lista) and funcion == "sumar":
        return sacarvalor(lista[n])+sacardelista(lista, n+1, funcion)
    else:
        if n < len(lista) and funcion == "aces":
            return contarrecursivo(lista[n], "A")+sacardelista(lista, n+1, funcion)
        else:
            if n >= len(lista):
                return 0
                
            
def contarrecursivo(mano, objeto):
    if mano[0]== objeto:
        return 1
    else:
        return 0



    
    
    

def hacercuentaconaces(mano,decision):
    if decision == "si" and sacardelista(mano, 0 , "aces")!=0:
        return (sacardelista(mano,0,"aces")-1)+(sacardelista(mano,0,"sumar")-((sacardelista(mano,0,"aces")-1)*11))
    else:
        if decision == "no" and sacardelista(mano, 0 , "aces")!=0:
            return sacardelista(mano,0,"aces")+(sacardelista(mano,0,"sumar")-(sacardelista(mano,0,"aces")*11))
        else:
            if decision!= "si" or decision!="no":
                return sacardelista(mano,0,"sumar")
                
            


    



def pedirdato(funcion, jugador):
    if funcion == "pedir carta":
        return raw_input(" El jugador quiere pedir carta S(si) N(no) ")
    else:
        if funcion == "que aces":
            return int(input("tiene dos opciones ya que cuenta con aces en su baraja "+ str(hacercuentaconaces(jugador, "si"))+ " o " +str(hacercuentaconaces(jugador, "no"))+" ")) 
        else:
            return "no ha elegido un caracter valido para continuar"
        

def verificaropcion(opcion, jugador):
    if opcion == hacercuentaconaces(jugador, "si"):
        return hacercuentaconaces(jugador, "si")
    else:
        if opcion == hacercuentaconaces(jugador, "no"):
            return hacercuentaconaces(jugador, "no")
        else:
            return verificaropcion(pedirdato("que aces", jugador),jugador)
        
                
def conacesocinaces(jugador):
    if sacardelista(jugador,0,"aces") >= 1:
        return verificaropcion(pedirdato("que aces", jugador),jugador)
    else:
        if sacardelista(jugador,0,"aces") == 0:
            return hacercuentaconaces(jugador, "no hay nada")

def verificar21(sumatoria,jugador, baraja):
    if sumatoria < 21:
        return pedircarta(jugador,baraja,pedirdato("pedir carta", jugador))
    else:
        if sumatoria == 21:
            return 21
        else:
            if sumatoria > 21:
                return 22

def pedircarta(jugador, baraja, funcion):
    if funcion == "S":
        return jugador.extend(sacarprimeracarta(baraja))
    else:
        if funcion == "N":
            return False
        else:
            return pedircarta(jugador, baraja, pedirdato("pedir carta", jugador))
        
def repetir(jugador,baraja , funcion):
    if funcion == False:
        return conacesocinaces(jugador)
    else:
        if funcion > 21:
            print "creo que te has pasado"
            return 22
        else:
            if funcion == 21:
                print "enhorabuena tienes veintiuna"
                return 21
            else:
                print jugador
                return repetir(jugador, baraja, verificar21(conacesocinaces(jugador),jugador, baraja))

def IA(casa, baraja, juegojugador):
    if sumarIA(casa) < juegojugador and juegojugador <= 21:
       casa.extend(sacarprimeracarta(baraja))
       print casa
       print sumarIA(casa)
       return IA(casa, baraja, juegojugador)
    else:
        return comparar(juegojugador,sumarIA(casa))
    
      
       
def sumarIA(casa):
    if sacardelista(casa,0,"aces") >= 1:
        if (hacercuentaconaces(casa, "si") >= hacercuentaconaces(casa, "no")) and hacercuentaconaces(casa, "si") <= 21:
            print hacercuentaconaces(casa, "si")
            return hacercuentaconaces(casa, "si")
        else:
            return hacercuentaconaces(casa, "no")
    else:
        if sacardelista(casa,0,"aces") < 1:
            print hacercuentaconaces(casa, "no hay nada")
            return hacercuentaconaces(casa, "no hay nada")
        
        
            
    
        

def comparar(juegojugador, juegocasa):
    
    if juegojugador < juegocasa and (juegocasa <= 21 and juegojugador <= 21):
        return "juego para la casa"
    else:
        if juegojugador > juegocasa and (juegocasa <= 21 and juegojugador <= 21):
            return "juego para el jugador"
        else:
            if juegojugador == juegocasa and (juegocasa <= 21 and juegojugador <= 21):
                return "juego en empate"
            else:
                if juegojugador <= 21 and juegocasa > 21:
                    return "juego para el jugador "
                else:
                    if juegojugador > 21 and juegocasa <= 21:
                        return "juego para la casa"
                    
                        
                

    
        
                
             



def juego(baraja, casa , jugador):
    if raw_input(" El jugador quiere jugar S(si) N(no) ") == "S":
        barajar(baraja)
        jugador.extend(sacarprimeracarta(baraja))
        casa.extend(sacarprimeracarta(baraja))
        jugador.extend(sacarprimeracarta(baraja))
        casa.extend(sacarprimeracarta(baraja))
        print "la mano del jugador es "+str(jugador)
        print "la mano de la casa es "+str(casa[0])
        print IA(casa, baraja, repetir(jugador, baraja, verificar21(conacesocinaces(jugador),jugador, baraja)))
        print "mano final del jugador"+str(jugador)
        print "mano final de la casa"+str(casa)
        return juego(hacernaipecompleto(),[],[])
    else:
        print "hasta luego"


juego(hacernaipecompleto(),[],[])








    
                        
                    
                    
               
            
        
