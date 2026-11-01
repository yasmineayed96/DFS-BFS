from collections import deque
from maze_view import backward_forward

def algo_recherche(maze, start, goal):
    """
    BFS qui enregistre les étapes pour animation.
    Chaque étape = (action, cell, cur_path)
      action : "visit" ou "backtrack"
      cur_path : chemin actuel du robot
    """
    rows, cols = len(maze), len(maze[0])
    parent = {start: None}
    visited = {start}
    steps = []

    q = deque([start])
    cur_path = [start]

    while q:
        cell = q.popleft()

        # (+) Animation pour retourner et avancer pas à pas
        backward_forward(cell, parent, cur_path, steps)
        
        # ajouter voisins
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = cell[0]+di, cell[1]+dj
            nxt = (ni, nj)
            if 0 <= ni < rows and 0 <= nj < cols and maze[ni][nj]==0 and nxt not in visited:
                visited.add(nxt)
                parent[nxt] = cell
                q.append(nxt)

        if cell == goal:
            return list(cur_path), steps

    return [], steps
