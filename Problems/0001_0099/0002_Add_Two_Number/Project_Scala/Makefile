SCALAC = scalac
SCALAC_FLAGS = 

all:	Mylib.class ListNode.class OperateListNode.class Solution.class Main.class


Mylib.class:	Mylib.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

ListNode.class:	ListNode.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

OperateListNode.class:	OperateListNode.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

Solution.class:	Solution.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

Main.class:	Main.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
