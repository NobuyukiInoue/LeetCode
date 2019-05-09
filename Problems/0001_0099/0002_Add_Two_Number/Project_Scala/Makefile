SCALAC = scalac
SCALAC_FLAGS = 

all:	ListNode.class Operate_ListNode.class Solution.class Main.class

ListNode.class:	ListNode.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

Operate_ListNode.class:	Operate_ListNode.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

Solution.class:	Solution.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

Main.class:	Main.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
