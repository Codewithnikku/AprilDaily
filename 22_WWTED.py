class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        
        def is_valid(query, word):
            count = 0
            for i in range(len(query)):
                if query[i] != word[i]:
                    count += 1
                    if count > 2:
                        return False
            return True
        
        res = []
        for query in queries:
            for word in dictionary:
                if is_valid(query, word):
                    res.append(query)
                    break
        
        return res