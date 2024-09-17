class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split(" ")
        s2=s2.split(" ")
        count1= Counter(s1)
        count2= Counter(s2)
        # s=[x for x in s1 if x not in s2 ]
        # a=[x for x in s2 if x not in s1]
        # b=s+a
        a = []

       
        for word in count1:
            if count1[word] == 1 and word not in count2:
                a.append(word)

        
        for word in count2:
            if count2[word] == 1 and word not in count1:
                a.append(word)

        return a
            
        