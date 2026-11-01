# maze_core.py
from maze_view import backward_forward

def algo_recherche(maze, start, goal):
    """
    DFS qui enregistre les étapes pour animation.
    Chaque étape = (action, cell, cur_path)
      action : "visit" ou "backtrack"
      cur_path : chemin actuel du robot
    """
    rows, cols = len(maze), len(maze[0])
    parent = {start: None}
    visited = {start}
    steps = []

	# pile (stack)
    stack = [start]
    cur_path = [start]

    while stack:
		# explore le dernier ajouté
        cell = stack.pop()

        # (+) Animation pour retourner et avancer pas à pas
        backward_forward(cell, parent, cur_path, steps)

        # ajouter voisins (ordre = haut, bas, gauche, droite)
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = cell[0]+di, cell[1]+dj
            nxt = (ni, nj)
            if 0 <= ni < rows and 0 <= nj < cols and maze[ni][nj] == 0 and nxt not in visited:
                visited.add(nxt)
                parent[nxt] = cell
                stack.append(nxt)

        if cell == goal:
            return list(cur_path), steps

    return [], steps
