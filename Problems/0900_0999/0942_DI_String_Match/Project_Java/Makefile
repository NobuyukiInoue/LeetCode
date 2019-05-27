JAVAC =javac
JAVAC_FLAGS =

all:	Solution.class Mylib.class Main.class

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Mylib.class:	Mylib.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
