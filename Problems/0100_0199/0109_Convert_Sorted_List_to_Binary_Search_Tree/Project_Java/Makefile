JAVAC =javac
JAVAC_FLAGS =

all:	Mylib.class TreeNode.class Operate_TreeNode.class ListNode.class Operate_ListNode.class Solution.class Main.class

Mylib.class:	Mylib.java
	$(JAVAC) $(JAVAC_FLAGS) $<

TreeNode.class:	TreeNode.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Operate_TreeNode.class:	Operate_TreeNode.java
	$(JAVAC) $(JAVAC_FLAGS) $<

ListNode.class:	ListNode.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Operate_ListNode.class:	Operate_ListNode.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
