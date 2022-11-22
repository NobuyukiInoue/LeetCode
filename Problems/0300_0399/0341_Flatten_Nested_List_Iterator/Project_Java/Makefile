JAVAC =javac
JAVAC_FLAGS =

all:	Mylib.class OperateNestedInteger.class NestedInteger.class NestedIterator.class Solution.class Main.class

Mylib.class:	Mylib.java
	$(JAVAC) $(JAVAC_FLAGS) $<

OperateNestedInteger.class:	OperateNestedInteger.java
	$(JAVAC) $(JAVAC_FLAGS) $<

NestedInteger.class:	NestedInteger.java
	$(JAVAC) $(JAVAC_FLAGS) $<

NestedIterator.class:	NestedIterator.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
