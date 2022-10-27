import pygame
TITLE = "Smooth Animation"
# https://github.com/nas-programmer/youtube-tutorials/blob/main/Smooth_movement.py

# Valori di proporzione

Delta_Time = 2 # Delta_Time (Congliabile 1/2)
Player_proportion = 1 # Divisore della grandezza del giocatore

#FPS
FPS = 60 * Delta_Time

# rapporto di proporzione allo schermo NON INFERIORE AD 1
MULT = 3

# rapporto offset telecamera dello schermo MAX 40
Moff = 30

# rapporto audio del gioco
AU = 5

# rapporto musica del gioco
MU = 5

Cam_visible = True

Debug = True

Player_speed = 4 * MULT / Delta_Time

Player_default_speed = Player_speed

Background_Color = (12, 24, 36)

# Dimensione Schermo
DF_width = 480
DF_height = 270

screen_width = DF_width * MULT
screen_height = DF_height * MULT

# Configurazione Schermo
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(TITLE)