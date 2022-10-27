import pygame, sys, os
import global_var as Glob


def get_font(size):
    return pygame.font.Font("freesansbold.ttf", size)

def inizializza():
    global clock, player, sceltaG, Folder_walkO, Folder_walkVD, Folder_walkVU

    sceltaG = "Senex"

    Folder_walkO = '../animation/'+sceltaG+'/WalkOrizontal'
    Folder_walkVD = '../animation/'+sceltaG+'/WalkVerticalD'
    Folder_walkVU = '../animation/'+sceltaG+'/WalkVerticalU'

    def riempi(percorso):
        FileNames = os.listdir(percorso)

        # Ordino i file e gli appendo ad una lista, in modo che le animazioni siano lineari e ordinate
        FileNames.sort()
        sorted(FileNames)

        for filename in FileNames:
            if percorso == Folder_walkO:
                #print("Trovato Percorso WO")
                Glob.PlayerWalkingO.append(filename)
            if percorso == Folder_walkVD:
                #print("Trovato Percorso WVD")
                Glob.PlayerWalkingVD.append(filename)
            if percorso == Folder_walkVU:
                #print("Trovato Percorso WVU")
                Glob.PlayerWalkingVU.append(filename)

            #print("File name:"+filename+"\n\n")

    riempi(Folder_walkO)
    riempi(Folder_walkVD)
    riempi(Folder_walkVU)

    Player_width, Player_height = pygame.image.load(Folder_walkVU+"/Walk0.png").convert().get_width()*Glob.MULT, pygame.image.load(Folder_walkVU+"/Walk0.png").convert().get_height()*Glob.MULT

    sprite_image = (Glob.PlayerWalkingVU, Glob.PlayerWalkingVU, Glob.PlayerWalkingO)

    # General setup
    clock = pygame.time.Clock()

    player = Player(x = Glob.screen_width/2-Player_width/2, y = Glob.screen_height/2-Player_height/2, width = Player_width, height = Player_height, char_image = sprite_image)

class Debug():
    def log(self, flag):

        if flag:

            key = ""

            if player.getUpPress():
                key = "up"
            elif player.getDownPress():
                key = "down"
            elif player.getLeftPress():
                key = "left"
            elif player.getRightPress():
                key = "right"
            
            FPS_TEXT = get_font(8*int(Glob.MULT)).render("FPS: "+str(int(clock.get_fps())), True, "white")
            FPS_RECT = FPS_TEXT.get_rect(center=(Glob.screen_width-40*Glob.MULT, 20*Glob.MULT))

            DROP_TEXT = get_font(5*int(Glob.MULT)).render("DROP "+str(100-int(clock.get_fps()*100/Glob.FPS))+"%", True, "red")
            DROP_RECT = DROP_TEXT.get_rect(center=(Glob.screen_width-95*Glob.MULT, 20*Glob.MULT))

            KEY_TEXT = get_font(10*int(Glob.MULT)).render(key, True, "blue")
            KEY_RECT = KEY_TEXT.get_rect(center=(Glob.screen_width-140*Glob.MULT, 20*Glob.MULT))


            Glob.screen.blit(KEY_TEXT, KEY_RECT)

            if int(clock.get_fps()) <= (Glob.FPS-(Glob.FPS/20)):
                #print("Gli fps sono scesi: "+str(clock.get_fps()))
                Glob.screen.blit(DROP_TEXT, DROP_RECT)
                

            Glob.screen.blit(FPS_TEXT, FPS_RECT)

class Player():
    def __init__(self, x, y, width, height, char_image):

        #stato attuale dell'animazione
        self.setIsWalking(False)

        #indicazione posizione (dinamica)
        self.setPositionX(int(x))
        self.setPositionY(int(y))


        self.Name_animationWVD = Folder_walkVD
        self.Name_animationWVU = Folder_walkVU
        self.Name_animationWO = Folder_walkO

        #indicazione grandezza (statica)
        self.width = width
        self.height = height
        
        # setta a video l'immagine del giocatore
        self.character = pygame.image.load(
        os.path.join(self.Name_animationWVD, "Walk0.png"))

        # animazione di walking
        self.animationWO = char_image[2]
        self.current_spriteWO = 0 # indica il corrente sprite generato e ciclato

        self.animationWVU = char_image[1]
        self.current_spriteWVU = 0

        self.animationWVD = char_image[0]
        self.current_spriteWVD = 0

        #pulsanti cliccati si/no
        self.setLeftPress(False)
        self.setRightPress(False)
        self.setUpPress(False)
        self.setDownPress(False)
        
        # setta l'immagine di animazione attuale di walking
        self.image = self.animationWVD[0]

# ---------- self.set() ----------

    def setPositionX(self, x):
        self.x = x

    def setPositionY(self, y):
        self.y = y

    def setIsWalking(self, val):
        self.__is_walking = val

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


# ---------- self.get() ----------

    def getPositionX(self):
        return self.x

    def getPositionY(self):
        return self.y

    def getRightPress(self):
        return self.__right_pressed

    def getLeftPress(self):
        return self.__left_pressed

    def getUpPress(self):
        return self.__up_pressed

    def getDownPress(self):
        return self.__down_pressed

    def getIsWalking(self):
        return self.__is_walking

    # aggiorna a schermo l'immagine attuale del Player
    def character_update(self,var):

        # Controlla se l'animazione è attiva
        if self.getIsWalking():

            self.current_spriteWO += 0.2 / Glob.Delta_Time # è un float perchè quando arriverà ad un int l'animazione cambiera quindi è come se fosse un delay
            self.current_spriteWVD += 0.2 / Glob.Delta_Time
            self.current_spriteWVU += 0.2 / Glob.Delta_Time

            # Controllo di non uscire dal range dei frames possibili
            if self.current_spriteWO >= len(self.animationWO):
                self.current_spriteWO = 0

            # setta l'immagine di animazione attuale di walking
            self.image = self.animationWO[int(self.current_spriteWO)]

            if self.current_spriteWVD >= len(self.animationWVD):
                self.current_spriteWVD = 0
            
            self.image = self.animationWVD[int(self.current_spriteWVD)]

            if self.current_spriteWVU >= len(self.animationWVU):
                self.current_spriteWVU = 0
            
            self.image = self.animationWVU[int(self.current_spriteWVU)]

            #print(self.current_spriteWO)

            if var==0:
                self.character = pygame.image.load(
                os.path.join(self.Name_animationWVD,self.image))

            if var==1:
                self.character = pygame.image.load(
                os.path.join(self.Name_animationWVU,self.image))

            if var==2:
                self.character = pygame.image.load(
                os.path.join(self.Name_animationWO,self.image)) # carica l'immagine presa dalla cartella Walk

            if var==3:
                immagine = pygame.image.load(
                os.path.join(self.Name_animationWO,self.image))
                self.character = pygame.transform.flip(immagine, True, False) # specchia l'immagine dalle assi x
            
            #print("Sprite WO corrente: "+str(self.current_spriteWO)+" | Sprite WVD corrente: "+str(self.current_spriteWVD)+" | Sprite WVU corrente: "+str(int(self.current_spriteWVU)))

    # Funzione che serve ad aggiornare la velocità attuale del giocatore la velocità da' un'impressione Smooth
    def update(self):
        if (self.getLeftPress() and not self.getRightPress()):
            self.setIsWalking(True)
            self.character_update(3) # richiamo la funzione di aggiorna l'animazione
        
        if (self.getRightPress() and not self.getLeftPress()):
            self.setIsWalking(True)
            self.character_update(2) # richiamo la funzione di aggiorna l'animazione

        if (self.getUpPress() and not self.getDownPress()):
            self.setIsWalking(True)
            self.character_update(1) # richiamo la funzione di aggiorna l'animazione

        if (self.getDownPress() and not self.getUpPress()):
            self.setIsWalking(True)
            self.character_update(0) # richiamo la funzione di aggiorna l'animazione
        
        self.character = pygame.transform.scale(self.character, (self.width, self.height)) # ingrandisco (scalo) l'immagine presa dalle cartelle
        Glob.screen.blit(self.character, (self.x , self.y)) # indica che lo schermo fa nascere il giocatore

    # setta l'animazione della camminata a vera
    def animate(self):
        self.setIsWalking(True)

    # setta l'animazione della camminata a falso e rimette le variabili a default
    def finish(self):
        self.setIsWalking(False)
        self.current_spriteWO = 0
        self.current_spriteWVD = 0
        self.current_spriteWVU = 0

        # imposta un'animazione di default dopo aver eseguito l'ultima
        self.image = self.animationWO[int(self.current_spriteWO)]
        self.character = pygame.image.load(
            os.path.join(self.Name_animationWVD, "Walk0.png"))

def key_pressed(event,IsPressed):

    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        player.setLeftPress(IsPressed)
        
        if IsPressed:
            player.animate()
        else:
            player.finish()
        
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        player.setRightPress(IsPressed)

        if IsPressed:
            player.animate()
        else:
            player.finish()

    if event.key == pygame.K_w or event.key == pygame.K_UP:
        player.setUpPress(IsPressed)

        if IsPressed:
            player.animate()
        else:
            player.finish()

    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
        player.setDownPress(IsPressed)

        if IsPressed:
            player.animate()
        else:
            player.finish()

def main():
    Inizia = True
    inizializza()
    while Inizia:
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()

            if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
                Inizia = False

            if pressed[pygame.K_F3]:
                if Glob.Debug:
                    Glob.Debug = False 
                else:
                    Glob.Debug = True

            if event.type == pygame.KEYDOWN:
                key_pressed(event, True)

            if event.type == pygame.KEYUP:
                key_pressed(event, False)


        # Drawing
        Glob.screen.fill((12,24,36))
        player.update()

        console = Debug()
        console.log(Glob.Debug)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(Glob.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    pygame.init()
    main()