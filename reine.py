import time
import sys
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
print("Toutes les librairies ont été chargées avec succès !")

def is_valid(state):
    k=len(state)-1

    for i in range (k):
        if state[k]==state[i]:
            return False
        
        if abs(state[i]-state[k])==abs(i-k):
            return False

    return True
#print(is_valid([1, 3, 0, 2]))  # True
#print(is_valid([0, 1, 2, 3]))  # False


from collections import deque
import time

def is_valid(state):
    k = len(state) - 1

    for i in range(k):
        if state[k] == state[i]:
            return False

        if abs(state[i] - state[k]) == abs(i - k):
            return False

    return True


def successors(state, n):
    successors_list = []

    for col in range(n):
        new_state = state + [col]

        if is_valid(new_state):
            successors_list.append(new_state)

    return successors_list


def bfs_n_queens(n):
    queue = deque([[]])
    explored_count = 0
    max_queue_size = 1
    start_time = time.time()

    while queue:
        max_queue_size = max(max_queue_size, len(queue))

        state = queue.popleft()
        explored_count += 1

        if len(state) == n:
            return (
                state,
                explored_count,
                max_queue_size,
                time.time() - start_time
            )

        for successor in successors(state, n):
            queue.append(successor)

    return None, explored_count, max_queue_size, time.time() - start_time


solution, nodes, max_q, exec_t = bfs_n_queens(4)

#print("Solution :", solution)
#print("Nœuds explorés :", nodes)
#print("Taille maximale de la file :", max_q)
#print("Temps d'exécution :", exec_t)




# Afficher le plateau des N reines
def plot_board(state):
    n = len(state)

    board = np.zeros((n, n))

    for r in range(n):
        for c in range(n):
            if (r + c) % 2 == 1:
                board[r, c] = 1

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(board, cmap="copper", alpha=0.6)

    # Afficher les reines
    for row, col in enumerate(state):
        ax.text(
            col, row, "♛",
            fontsize=32 - (n * 2),
            ha="center",
            va="center",
            color="white"
        )

    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))

    ax.set_xticklabels([f"C{i}" for i in range(n)])
    ax.set_yticklabels([f"L{i}" for i in range(n)])

    ax.set_title(
        f"Solution des {n}-Reines",
        fontsize=14,
        fontweight="bold"
    )

    ax.grid(False)
    plt.tight_layout()
    plt.show(block=True)


# Afficher une solution pour N = 4
solution, nodes, max_q, exec_t = bfs_n_queens(4)

if solution:
    plot_board(solution)


# Tester BFS pour N de 4 à 9
n_values = list(range(4, 10))

results_nodes = []
results_queue = []
results_time = []

print(
    f"{'N':<5} | {'Explorés':<10} | "
    f"{'Taille Max Queue':<18} | {'Temps (s)':<12}"
)
print("-" * 60)

for n in n_values:

    # Mesurer le temps d'exécution de BFS
    start = time.perf_counter()
    solution, nodes, max_q, exec_t = bfs_n_queens(n)
    elapsed = time.perf_counter() - start

    # Stocker les résultats
    results_nodes.append(nodes)
    results_queue.append(max_q)
    results_time.append(elapsed)

    # Afficher les résultats
    print(
        f"{n:<5} | {nodes:<10} | {max_q:<18} | "
        f"{elapsed:<12.5f}"
    )


# Créer les deux graphiques
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(14, 5)
)

# Graphique 1 : exploration et taille de la file
ax1.plot(
    n_values, results_nodes,
    marker="o", color="blue",
    label="Nœuds explorés"
)

ax1.plot(
    n_values, results_queue,
    marker="s", color="red",
    linestyle="--",
    label="Taille max file"
)

ax1.set_xlabel("N")
ax1.set_ylabel("Nombre d'états")
ax1.set_yscale("log")
ax1.set_title("Croissance spatiale (log)")
ax1.grid(True)
ax1.legend()


# Graphique 2 : temps d'exécution
ax2.plot(
    n_values, results_time,
    marker="^", color="green"
)

ax2.set_xlabel("N")
ax2.set_ylabel("Temps (s)")
ax2.set_title("Temps d'exécution du BFS")
ax2.grid(True)


plt.tight_layout()
plt.show()

def dfs_n_queens(n):
    stack = [[]]
    explored_count = 0
    max_stack_size = 1
    start_time = time.time()

    while stack:
        max_stack_size = max(max_stack_size, len(stack))

        # 1. Extraire le dernier état de la pile
        state = stack.pop()
        explored_count += 1

        # 2. Tester si une solution est trouvée
        if len(state) == n:
            return state, explored_count, max_stack_size, time.time() - start_time

        # 3. Générer et empiler les successeurs
        row = len(state)

        for col in reversed(range(n)):
            # Vérifier si la reine peut être placée dans cette colonne
            valid = True

            for r, c in enumerate(state):
                # Même colonne
                if c == col:
                    valid = False
                    break

                # Même diagonale
                if abs(r - row) == abs(c - col):
                    valid = False
                    break

            if valid:
                stack.append(state + [col])

    return None, explored_count, max_stack_size, time.time() - start_time
N_TEST = 9
sol_b, nodes_b, max_q_b, time_b = bfs_n_queens(N_TEST)
sol_d, nodes_d, max_s_d, time_d = dfs_n_queens(N_TEST)
print("BFS :", sol_b, nodes_b, max_q_b, f"{time_b:.5f}s")
print("DFS :", sol_d, nodes_d, max_s_d, f"{time_d:.5f}s")
