JAVAC =javac
JAVAC_FLAGS =

all:	Mylib.class Foo.class Solution.class Main.class

Mylib.class:    Mylib.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Foo.class:	Foo.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
