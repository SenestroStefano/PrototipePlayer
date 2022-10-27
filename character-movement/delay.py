import pygame, sys

# Classe che imposta un delay asincrono ( i metodi devono essere richiamati dentro ad un while )
class Delay():
    def __init__(self, sec, event):
        self.__min = 0
        self.__max = sec * FPS
        self.__increment = 1
        self.__function = event
        self.__flag = True

    # | Avvia il delay -> Poi si interromperà |
    def Start(self):
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) >= self.__max:
                self.__function()
                self.__flag = False

    # | Restarta il delay |
    def ReStart(self):
        if not self.__flag:
            self.__min = 0
            self.__flag = True

    # | Imposta il delay a infinito |
    def Infinite(self):
        self.ReStart()
        self.Start()

    # | Stampa lo stato attuale del delay |
    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/FPS, self.__max/FPS, self.__function))


class Delay_noFunction():
    def __init__(self, sec):
        self.__min = 0
        self.__max = sec * FPS
        self.__increment = 1
        self.__flag = True

    def Start(self):
        if self.__flag:
            self.__min += self.__increment

            if int(self.__min) == self.__max:
                self.__flag = False
                return True

        return False

    def ReStart(self):
        if not self.__flag:
            self.__min = 0
            self.__flag = True

    def Infinite(self):
        self.ReStart()
        self.Start()

    def ActualState(self):
        print("| Current Second: %d | Max Seconds: %d | Function: %s |" %(self.__min/FPS, self.__max/FPS, self.__function))

"""Esempio di funzione"""

def inizializza():
    global FPS, clock, screen, screen_width, screen_height, var

    FPS = 30
    clock = pygame.time.Clock()

    screen_width, screen_height = 800, 800
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Delay")
    var = 0

def miaFunzione():
    global var
    var += 1
    print(var)

def main():
    # Intervallo di tempo - Funzione Richiamante
    delay = Delay(sec = 0.1, event = miaFunzione)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.fill((12,24,36))

        delay.Infinite()
        #delay.ActualState()

        testo = pygame.font.Font("freesansbold.ttf", 102).render(str(var), True, "White")

        screen.blit(testo, (screen_width/2 - testo.get_width()/2, screen_height/2 - testo.get_height()/2))

        #delay.ActualState()

        clock.tick(FPS)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    inizializza()
    main()