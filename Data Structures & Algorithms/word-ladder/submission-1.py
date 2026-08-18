class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:]
                nei[pattern].append(word)

        visited=set([beginWord])
        queue=deque([beginWord])
        res=1
        while queue:
            for _ in range(len(queue)):
                word=queue.popleft()
                if word==endWord:
                    return res
                for i in range(len(word)):
                    pattern=word[:i]+"*"+word[i+1:]
                    for next_word in nei[pattern]:
                        if next_word not in visited:
                            visited.add(next_word)
                            queue.append(next_word)            
            res+=1
        return 0
                    