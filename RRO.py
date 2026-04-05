class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        #  Optimal code
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')