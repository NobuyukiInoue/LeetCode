JAVAC =javac
JAVAC_FLAGS =

all:	Mylib.class Node.class OperateNode.class Solution.class Main.class

Mylib.class:	Mylib.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Node.class:	Node.java
	$(JAVAC) $(JAVAC_FLAGS) $<

OperateNode.class:	OperateNode.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
