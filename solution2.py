# function to return the number of moves to be taken
def moves(empty_index):
    row_index = empty_index // 3  # calculating row index of empty space
    col_index = empty_index % 3   # calculating column index of empty space

    move = [] #empty list to store moves to take

    # Check left move
    if col_index > 0:
         move.append(empty_index - 1)

    # Check right move
    if col_index < 2:
        move.append(empty_index + 1)

    # Check up move
    if row_index > 0:
        move.append(empty_index - 3)

    # Check down move
    if row_index < 2:
        move.append(empty_index + 3)

    return move

# function to perform iterative deepening
def iterativeDeepening(initial_puzzle):
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Correct order of the puzzle

# function to perform depth first search
    def dfs(initial_state, depth, path):
        if depth == 0:
            return None  # Reached depth limit
        if initial_state == goal:
            return path  # puzzle is in goal state
        empty_index = initial_state.index(8) # store index of empty space
        possible_moves = moves(empty_index) # store number of moves to be taken
        # iterate through the moves and swap the number to reach goal state
        for move_pos in possible_moves:
            new_puzzle = initial_state[:]
            new_puzzle[empty_index], new_puzzle[move_pos] = new_puzzle[move_pos], new_puzzle[empty_index]
            # recursive function to iterate until goal state is reached
            result = dfs(new_puzzle, depth - 1, path + [move_pos])
            if result is not None:
                return result  # Return the path if a solution is found

    # Iterative Deepening
    for depth in range(1, 100):  # Adjust the maximum depth as needed
        result = dfs(initial_puzzle, depth, [])
        if result is not None:
            return result

    return []  # Return an empty list if no solution is found within the depth limit

# function to calculate heuristic
def calculate_heuristic(initial_puzzle, goal_state):
    counter = 0
    for i in range(len(initial_puzzle)):
        x, y = initial_puzzle[i], goal_state[i]
        if x != y and x != 8:
            counter += 1  # store the number of mismatched tiles/numbers
    return counter

# function to perform astar search
def astar(puzzle):
    goal_state=[0,1,2,3,4,5,6,7,8]
    open_list = [(0, puzzle, [])]  # (cost, state, path)
    closed_set = set()

# while loop continues until open_list is not empty
    while open_list:
        cost, current_state, path = open_list.pop(0)  # pops first element of open_list
        empty_space = current_state.index(8) # index of empty space in puzzle

        if current_state == goal_state:
            return path  # Found a solution
        # checking whether the current state is closed set and has been visited before or not
        if tuple(current_state) not in closed_set:
            closed_set.add(tuple(current_state))
            possible_steps = moves(empty_space)

            for moved in possible_steps:
                new_state = current_state[:]
                new_state[empty_space], new_state[moved] = new_state[moved], new_state[empty_space]
                new_cost = len(path) + 1 + calculate_heuristic(new_state, goal_state) # calculating f(n) = g(n) + h(n)
                open_list.append((new_cost, new_state, path + [moved]))

            open_list.sort(key=lambda x: x[0])  # Sort based on cost

    return []

