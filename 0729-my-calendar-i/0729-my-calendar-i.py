class TreeNode:
    def __init__(self,lo,hi):
        self.left = None
        self.right = None
        self.lo = lo
        self.hi = hi
        self.mid = int((self.lo + self.hi) / 2)

class MyCalendar:

    def __init__(self):
        self.root = None

    def update(self,node,start,end):        
        mid = int((start + end) /2)
        if not node:
            node = TreeNode(start,end)
            if not self.root:
                # this is the first interval and we take it as root
                self.root = node
        elif node.mid > mid:
            node.left = self.update(node.left,start,end)
        else:
            node.right = self.update(node.right,start,end)
        return node

    def canInsert(self,node,start,end):
        mid = int((start + end) /2)
        if not node: 
            return True
        if not (start >= node.hi or end <= node.lo):
            #Overlap detected. Finding disjoints are easier than overlaps so we just check if they are not disjoint
            return False
        if node.mid > mid:
            return self.canInsert(node.left,start,end)
        else:
            return self.canInsert(node.right,start,end)

    def book(self, start: int, end: int) -> bool:
        ans = self.canInsert(self.root,start,end)
        if ans:
            self.update(self.root,start,end)
        return ans

        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)