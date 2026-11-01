import pygame, time, os

CELL = 48
PATH_COLOR = (0,200,0)
BACK_COLOR = (220,0,0)
LINE_WIDTH = 4
MODE_GAME = True

# Specialement pour BFS (animation de retour pas à pas)
def backward_forward(cell, parent, cur_path, steps):
    # reconstruire chemin vers cell
    path_to_cell = []
    p = cell
    while p:
        path_to_cell.append(p)
        p = parent.get(p)
    path_to_cell.reverse()

    # trouver dernier ancêtre commun
    i = 0
    while i < len(cur_path) and i < len(path_to_cell) and cur_path[i] == path_to_cell[i]:
        i += 1

    # backtracking pas à pas
    for k in range(len(cur_path)-1, i-1, -1):
        removed = cur_path.pop()
        steps.append(("backtrack", removed, list(cur_path)))

    # avancer pas à pas
    for k in range(i, len(path_to_cell)):
        cur_path.append(path_to_cell[k])
        steps.append(("visit", path_to_cell[k], list(cur_path)))

def load_icon(name):
    img = pygame.image.load(os.path.join("icons", name)).convert_alpha()
    return pygame.transform.scale(img, (CELL, CELL))

def cell_center(i,j):
    return (j*CELL + CELL//2, i*CELL + CELL//2)

def run_animation(maze, start, goal, steps, delay=0.1, game_mode=False):
    rows, cols = len(maze), len(maze[0])
    pygame.init()
    screen = pygame.display.set_mode((cols*CELL, rows*CELL))
    pygame.display.set_caption("Algorithme de recherche")

    wall    = load_icon("wall.jpg")
    floor   = load_icon("floor.jpg")
    start_i = load_icon("start.jpg")
    goal_i  = load_icon("goal.jpg")
    agent_i = load_icon("agent.jpg")

    path_points = []
    back_segments = []
    current = None

    def draw():
        # fond
        
        for i in range(rows):
            for j in range(cols):
                screen.blit(floor if maze[i][j]==0 else wall, (j*CELL, i*CELL))

        # tracer segments annulés rouges
        for a,b in back_segments:
            pygame.draw.line(screen, BACK_COLOR, cell_center(*a), cell_center(*b), LINE_WIDTH)

        # tracer chemin vert
        if len(path_points) > 1:
            pygame.draw.lines(screen, PATH_COLOR, False,
                              [cell_center(*c) for c in path_points], LINE_WIDTH)

        # départ et objectif
        screen.blit(start_i, (start[1]*CELL, start[0]*CELL))
        screen.blit(goal_i,  (goal[1]*CELL, goal[0]*CELL))

        # icône du robot
        if current:
            screen.blit(agent_i, (current[1]*CELL, current[0]*CELL))

        pygame.display.flip()

    if not game_mode:
        ''' AI Mode '''
        for action, cell, cur_path in steps:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); return

            if action == "visit":
                if cur_path:
                    path_points = list(cur_path)
                    current = cell
            else:  # backtrack
                if len(cur_path) >= 1:
                    back_segments.append((path_points[-1], cur_path[-1]))
                    path_points = list(cur_path)
                    current = path_points[-1] if path_points else None

            draw()
            # accélérer retour : delay plus court pour backtrack
            time.sleep(delay if action=="visit" else delay*0.2)    

        draw()
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); return
    else:
        ''' Game Mode '''
        clock = pygame.time.Clock()
        current = start
        while True:
            draw()
            # clock.tick(0.1)  # vitesse du jeu
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); return
                elif e.type == pygame.KEYDOWN:
                    di, dj = 0, 0
                    if e.key == pygame.K_UP: di = -1
                    elif e.key == pygame.K_DOWN: di = 1
                    elif e.key == pygame.K_LEFT: dj = -1
                    elif e.key == pygame.K_RIGHT: dj = 1

                    ni, nj = current[0]+di, current[1]+dj
                    if 0 <= ni < rows and 0 <= nj < cols and maze[ni][nj]==0:
                        current = (ni,nj)
                        path_points.append(current)

                        if current == goal:
                            print("Goal reached!")
