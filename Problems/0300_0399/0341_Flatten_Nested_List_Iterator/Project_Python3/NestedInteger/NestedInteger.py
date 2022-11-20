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

# from NestedInteger import NestedInteger

from typing import List, Dict, Tuple

class NestedInteger:
    def __init__(self, flds) -> None:
        if isinstance(flds, int):
            self.val = flds
            return
        self.val = []
        for fld in flds:
            self.val.append(NestedInteger(fld))
        return

    def isInteger(self) -> bool:
        if isinstance(self.val, int):
            return True
        return False

    def getInteger(self) -> int:
        return self.val

    def getList(self) -> List[int]:
        return self.val
