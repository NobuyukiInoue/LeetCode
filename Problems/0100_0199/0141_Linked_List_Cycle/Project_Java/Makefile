JAVAC =javac
JAVAC_FLAGS =

all:	Mylib.class ListNode.class OperateListNode.class Solution.class Main.class

Mylib.class:	Mylib.java
	$(JAVAC) $(JAVAC_FLAGS) $<

ListNode.class:	ListNode.java
	$(JAVAC) $(JAVAC_FLAGS) $<

OperateListNode.class:	OperateListNode.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
