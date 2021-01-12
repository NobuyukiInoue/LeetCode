JAVAC =javac
JAVAC_FLAGS =

all:	Mylib.class TreeNode.class Codec2.class OperateTreeNode.class Solution.class Main.class

Mylib.class:	Mylib.java
	$(JAVAC) $(JAVAC_FLAGS) $<

TreeNode.class:	TreeNode.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Codec2.class:	Codec2.java
	$(JAVAC) $(JAVAC_FLAGS) $<

OperateTreeNode.class:	OperateTreeNode.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
