JAVAC =javac
JAVAC_FLAGS =

all:	Mylib.class ZeroEvenOdd.class Solution.class Main.class

Mylib.class:    Mylib.java
	$(JAVAC) $(JAVAC_FLAGS) $<

ZeroEvenOdd.class:	ZeroEvenOdd.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
