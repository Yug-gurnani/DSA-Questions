 """
 Given two words beginWord and endWord, and a dictionary wordList,
return the length of the shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.
Return 0 if there is no such transformation sequence.
 """
 def ladderLength(begin: str, end: str, word: List[str]) -> int:
        def isadjacent(a,b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
                    if count > 1:
                        return False
            return True
        dic = {}
        for i in word:
            dic[i] = 1
        queue = []
        item = [begin,1]
        queue.append(item)
        while queue:
            curr = queue.pop(0)
            for i in dic:
                if dic[i] == 1:
                    if isadjacent(curr[0],i):
                        queue.append([i,curr[1]+1])
                        if i == end:
                            return curr[1]+1
                        dic[i] = 0
        return 0