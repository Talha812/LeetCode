class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        list1 = []
        list2 = []
        
        for i in s:
            if i == "#" and len(list1) > 0:
                list1.pop()
            elif(i != "#"):
                list1.append(i)
        
        for i in t:
            if i == "#" and len(list2) > 0:
                list2.pop()
            elif(i != "#"):
                list2.append(i)
        #print(list1, list2)
        return list1 == list2