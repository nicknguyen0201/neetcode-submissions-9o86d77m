from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        #wordList.append(beginWord)

        #build a mp[patten]->word

        pattern_to_words=defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                #construct willcard on word
                pattern=word[:i]+"*"+word[i+1:]
                pattern_to_words[pattern].append(word)
        
        #do bfs
        q=deque([beginWord])
        seen=set([beginWord])
        steps=1
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return steps
                
                #generate all wildcards
                for i in range(len(word)):
                    pattern=word[:i]+"*"+word[i+1:]
                    #check if this is a valid pattern to see who connected to this word
                    
                    for neighbor in pattern_to_words[pattern]:
                        if neighbor not in seen:
                            q.append(neighbor)
                            seen.add(neighbor)
            steps+=1
        return 0
        

