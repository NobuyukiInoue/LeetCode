SCALAC = scalac
SCALAC_FLAGS = 

all:	TreeNode.class OperateTreeNode.class Solution.class Main.class

TreeNode.class:	TreeNode.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

OperateTreeNode.class:	OperateTreeNode.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

Solution.class:	Solution.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

Main.class:	Main.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
