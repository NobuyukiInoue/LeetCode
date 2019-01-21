SCALAC = scalac
SCALAC_FLAGS = 

all:	Main.class Solution.class TreeNode.class

Main.class:	OutputTreeNode.class Solution.class Main.scala
	$(SCALAC) $(SCALAC_FLAGS) Main.scala

Solution.class:	TreeNode.class Solution.scala
	$(SCALAC) $(SCALAC_FLAGS) Solution.scala

TreeNode.class:	TreeNode.scala
	$(SCALAC) $(SCALAC_FLAGS) TreeNode.scala

OutputTreeNode.class:	OutputTreeNode.scala
	$(SCALAC) $(SCALAC_FLAGS) OutputTreeNode.scala

clean:
	rm ./*.class

.PHONY:	all clean
