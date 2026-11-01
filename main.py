# *** TODO: Changer entre maze_core1 (BFS) et maze_core2 (DFS)
from maze_core2 import algo_recherche
from maze_view import run_animation

# --- parameters ---

# *** TODO: Changer entre mode jeu (manuel) actif ou non
GAME_MODE = False

# --- labyrinthe (0 = libre, 1 = mur) ---
MAZE = [
 [0,0,1,0,0,0,1,0,0,0,1,0],
 [0,1,1,0,1,0,1,0,1,0,1,0],
 [0,0,0,0,1,0,0,0,1,0,1,0],
 [1,1,0,1,1,0,1,1,1,0,1,0],
 [0,0,0,0,0,0,1,0,0,0,1,0],
 [0,1,1,1,0,1,1,1,0,1,1,0],
 [0,0,0,0,0,1,0,1,0,1,1,0],
 [1,1,0,1,0,0,0,1,0,0,0,0],
 [0,0,0,1,1,1,0,1,1,1,1,0],
 [0,1,0,0,0,1,0,1,1,0,0,0],
 [0,1,1,1,0,1,0,1,0,0,1,0],
 [0,0,0,0,0,0,0,1,0,1,1,0],
]
START = (0,0)
GOAL  = (6,6)

# --- exécution de l'algo ---
if not GAME_MODE:
	# Mode AI
	path, steps = algo_recherche(MAZE, START, GOAL)
	print("Chemin final :", path)
else:
	# (+) pour mode Game
	steps = []

# --- visualisation ---
run_animation(MAZE, START, GOAL, steps, delay=0.1, game_mode=GAME_MODE)
