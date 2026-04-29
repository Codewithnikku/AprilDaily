class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        # Combine all robot info and sort by position
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        
        stack = []  # will store indices of robots moving right
        alive = [True] * len(robots)
        
        for i in range(len(robots)):
            pos, health, direction, idx = robots[i]
            
            if direction == 'R':
                stack.append(i)
            else:  # direction == 'L'
                while stack and robots[i][1] > 0:
                    j = stack[-1]
                    
                    if robots[j][1] < robots[i][1]:
                        # right robot dies
                        alive[j] = False
                        stack.pop()
                        robots[i] = (robots[i][0], robots[i][1] - 1, robots[i][2], robots[i][3])
                    
                    elif robots[j][1] > robots[i][1]:
                        # left robot dies
                        alive[i] = False
                        robots[j] = (robots[j][0], robots[j][1] - 1, robots[j][2], robots[j][3])
                        break
                    
                    else:
                        # both die
                        alive[j] = False
                        alive[i] = False
                        stack.pop()
                        break
        
        # Collect surviving robots and return in original order
        result = []
        for i in range(len(robots)):
            if alive[i]:
                result.append((robots[i][3], robots[i][1]))
        
        result.sort()  # sort by original index
        return [h for _, h in result]