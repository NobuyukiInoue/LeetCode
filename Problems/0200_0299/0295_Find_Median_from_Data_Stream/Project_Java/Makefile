JAVAC =javac
JAVAC_FLAGS =

all:	MedianFinder.class Solution.class Main.class

MedianFinder.class: MedianFinder.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
