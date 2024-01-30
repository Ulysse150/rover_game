
import traceback
from game import*
from variables import*

rover_game = Game(largeur_ecran, hauteur_ecran, title, path_first_background)
try:
    while rover_game.running:
        rover_game.main()
except:
    print(traceback.format_exc())