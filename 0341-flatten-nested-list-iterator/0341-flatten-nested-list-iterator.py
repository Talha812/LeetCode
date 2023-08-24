# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattenList = collections.deque([])
        self.flatten(nestedList)
        
    def next(self) -> int:
        return self.flattenList.popleft()
    
    def hasNext(self) -> bool:
        if not self.flattenList:
            return False
        
        return True
    
    def flatten(self, nestedList):
        for nestedInteger in nestedList:
            if not nestedInteger.isInteger():
                self.flatten(nestedInteger.getList())
            else:
                self.flattenList.append(nestedInteger.getInteger())
        
        
            
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

