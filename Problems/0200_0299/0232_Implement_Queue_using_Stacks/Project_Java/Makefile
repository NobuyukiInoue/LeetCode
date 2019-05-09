JAVAC =javac
JAVAC_FLAGS =

all:	MyQueue.class Solution.class Main.class

MyQueue.class:	MyQueue.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
