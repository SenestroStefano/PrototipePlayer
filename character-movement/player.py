import pygame
import global_var as Glob

#Player Class
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

        #indicazione grandezza (statica)
        self.width = 16 * Glob.MULT / Glob.Player_proportion
        self.height = 16 * Glob.MULT / Glob.Player_proportion

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = "Red"

        #indicazione velocità (dinamica)
        self.setVelocitaX(0)
        self.setVelocitaY(0)

        #pulsanti cliccati si/no
        self.setLeftPress(False)
        self.setRightPress(False)
        self.setUpPress(False)
        self.setDownPress(False)
        self.speed = Glob.Player_speed

        self.Last_keyPressed = "Null"

        #hitbox del player
        self.setHitbox()
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self):
        #indicazione velocità (dinamica)
        self.setVelocitaX(0)
        self.setVelocitaY(0)
        if self.getLeftPress() and not self.getRightPress():
            self.setVelocitaX(-Glob.Player_speed)
        if self.getRightPress() and not self.getLeftPress():
            self.setVelocitaX(Glob.Player_speed)
        if self.getUpPress() and not self.getDownPress():
            self.setVelocitaY(-Glob.Player_speed)
        if self.getDownPress() and not self.getUpPress():
            self.setVelocitaY(Glob.Player_speed)
        
        self.setPositionX(self.getPositionX()+self.getVelocitaX())
        self.setPositionY(self.getPositionY()+self.getVelocitaY())

        self.rect = pygame.Rect(int(self.x), int(self.y), self.width, self.height)

        self.setHitbox()
        self.rect = pygame.Rect(self.hitbox) # indico la hitbox (mesh) del Player

    def HasCollision(self, object):
    
        def Confronta(value):   # Creo una funziona dato che la utilizzo piu' volte e se gli passo "x" fa una cosa mentre se gli passo "y" ne fa un'altra
            
            #self.finish()    # ogni volta che collido stoppo l'animazione del player

            if value=="x":  # confronto il valore passato

                if self.x >= object.x:  # confronto se la posizione del player delle x è maggiore o uguale della posizione delle x dell'oggetto di cui ho collisione
                    self.x += Glob.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setLeftPress(False)    # ogni volta che collido dal lato sinistro non posso riandare a ricliccare il pulsante destro
                    return True # ritorno un valore perchè dopo lo vado ad utilizzare
                elif self.x <= object.x:
                    self.x -= Glob.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setRightPress(False)    # ogni volta che collido dal lato destro non posso riandare a ricliccare il pulsante sinistro
                    return False # ritorno un valore perchè dopo lo vado ad utilizzare

            if value=="y":  # confronto il valore passato

                if self.y >= object.y:  # confronto se la posizione del player delle y è maggiore o uguale della posizione delle y dell'oggetto di cui ho collisione
                    self.y += Glob.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setUpPress(False)    # ogni volta che collido dal lato basso non posso riandare a ricliccare il pulsante alto
                    return True # ritorno un valore perchè dopo lo vado ad utilizzare
                elif self.y <= object.y:
                    self.y -= Glob.Player_speed    # ogni volta che collido vado a settare la posizione del player indietro grazie alla sua velocità
                    self.setDownPress(False)    # ogni volta che collido dal lato alto non posso riandare a ricliccare il pulsante basso
                    return False # ritorno un valore perchè dopo lo vado ad utilizzare
            

        if self.rect.colliderect(object):   # Metodo di pygame che confronta se due rettangoli collidono

            # Setto diverse variabili per non ripeterli nei confronti
            w = (self.Last_keyPressed == "Up")
            a = (self.Last_keyPressed == "Left")
            
            s = (self.Last_keyPressed == "Down")
            d = (self.Last_keyPressed == "Right")

            
            a1 = (self.getRightPress() and w or self.getLeftPress() and w)
            b1 =  (self.getLeftPress() and s or self.getRightPress() and s)

            c1 =  (self.getUpPress() and a or self.getDownPress() and a)
            d1 =  (self.getUpPress() and d or self.getDownPress() and d)

            # print("\n\nSinistro o Destro and Sù: ",str(a1))
            # print("Sinistro o Destro and Giù: ",str(b1))
            # print("Alto o Basso and Sinistra: ",str(c1))
            # print("Alto o Basso and Destra: ",str(d1))

            # print("\nup: "+str(self.getUpPress())+" |down: "+str(self.getDownPress())+" |left: "+str(self.getLeftPress())+" |right: "+str(self.getRightPress())+"\n")
            
            if self.Last_keyPressed != "Null":  # Confronto se il giocatore è fermo o si sta muovendo

                if (a1 or b1) and (not c1 and not d1):  # se è stato premuto il pulsante destro/sinistro e NON quello alto o basso mentre si ha una collisione allora:

                    Confronta("x")  # richiamo la funzione

                    if Confronta("x"):  # se la funzione mi ritorna True allora:
                        self.setLeftPress(False)
                    else:  # se la funzione mi ritorna False allora:
                        self.setRightPress(False)

                    self.Last_keyPressed = "Null"   # Variabile usata per non dare errori dato che l'ultimo pulsante cliccato sono l'insieme di due in contemporanea

                    
                if (c1 or d1) and (not a1 and not b1):  # se è stato premuto il pulsante alto/basso e NON con quello sinistro o destro mentre si ha una collisione allora:

                    Confronta("y")  # richiamo la funzione

                    if Confronta("y"):  # se la funzione mi ritorna True allora:
                        self.setUpPress(False)
                    else:  # se la funzione mi ritorna False allora:
                        self.setDownPress(False)

                    self.Last_keyPressed = "Null"   # Variabile usata per non dare errori dato che l'ultimo pulsante cliccato sono l'insieme di due in contemporanea
                    

                if (self.getRightPress() or self.getLeftPress() or a or d) and (not w and not s):   # Qua altri confronti con unicamente con un pulante a volta cliccato sinistra/destra
                    Confronta("x")
                
                if (self.getUpPress() or self.getDownPress() or w or s) and (not d and not a):   # Qua altri confronti con unicamente con un pulante a volta cliccato alto/basso
                    Confronta("y")
            else:
                Confronta("y")
                Confronta("x")
                #self.setAllkeys(None)

# ---------- self.set() ----------

    def setPositionX(self, x):
        self.x = x

    def setPositionY(self, y):
        self.y = y

    def setVelocitaX(self, x):
        self.__velX = x

    def setVelocitaY(self, y):
        self.__velY = y

    def setRightPress(self, r):
        self.__right_pressed = r

    def setLeftPress(self, l):
        self.__left_pressed = l

    def setUpPress(self, u):
        self.__up_pressed = u

    def setDownPress(self, d):
        self.__down_pressed = d

    def setAllkeys(self, v):
        
        if (v != True and v != False):
            return

        self.setUpPress(v)
        self.setDownPress(v)
        self.setLeftPress(v)
        self.setRightPress(v)

    def setHitbox(self):
        #self.hitbox = (self.x + 15 * Glob.MULT /Glob.Player_proportion, self.y + 17 * Glob.MULT /Glob.Player_proportion, 24* Glob.MULT /Glob.Player_proportion, 43 * Glob.MULT /Glob.Player_proportion)
        self.hitbox = (self.rect)

# ---------- self.get() ----------

    def getPositionX(self):
        return self.x

    def getPositionY(self):
        return self.y

    def getVelocitaX(self):
        return self.__velX

    def getVelocitaY(self):
        return self.__velY

    def getRightPress(self):
        return self.__right_pressed

    def getLeftPress(self):
        return self.__left_pressed

    def getUpPress(self):
        return self.__up_pressed

    def getDownPress(self):
        return self.__down_pressed