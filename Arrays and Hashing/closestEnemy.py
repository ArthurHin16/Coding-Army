def findClosestEnemy(array):
    # Step 1: Parse the Input
    grid = [list(row) for row in array]

    # Step 2: Find Player and Enemy Positions
    player_pos = None
    enemy_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                player_pos = (i, j)
            elif grid[i][j] == '2':
                enemy_positions.append((i, j))

    # Step 5: Handle Edge Case
    if len(enemy_positions) == 0:
        return -1

    # Step 3: Find the Closest Enemy
    min_distance = float('inf')
    closest_enemy_pos = None
    for enemy_pos in enemy_positions:
        distance = abs(enemy_pos[0] - player_pos[0]) + \
            abs(enemy_pos[1] - player_pos[1])
        if distance < min_distance:
            min_distance = distance
            closest_enemy_pos = enemy_pos

    # Step 4: Calculate the Minimum Steps
    return min_distance


array = ["00000", "10000", "00002", "00000"]
print(findClosestEnemy(array))
