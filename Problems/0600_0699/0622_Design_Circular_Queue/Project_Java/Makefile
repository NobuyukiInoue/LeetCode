JAVAC =javac
JAVAC_FLAGS =

all:	MyCircularQueue.class Solution.class Main.class

MyCircularQueue.class:	MyCircularQueue.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
