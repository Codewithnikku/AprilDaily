class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        direction = 0
        x, y = 0, 0
        max_distance = 0
        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:  
                direction = (direction - 1) % 4
            elif command == -1:  
                direction = (direction + 1) % 4
            else:  
                for _ in range(command):
                    if direction == 0:  
                        next_pos = (x, y + 1)
                    elif direction == 1:  
                        next_pos = (x + 1, y)
                    elif direction == 2:  
                        next_pos = (x, y - 1)
                    else:  
                        next_pos = (x - 1, y)

                    if next_pos in obstacle_set:
                        break

                    x, y = next_pos
                    max_distance = max(max_distance, x**2 + y**2)

        return max_distance