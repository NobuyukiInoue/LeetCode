JAVAC =javac
JAVAC_FLAGS =

all:	Main.class mylib.class Solution.class 

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) Main.java

mylib.class:	mylib.java
	$(JAVAC) $(JAVAC_FLAGS) mylib.java

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) Solution.java

clean:
	rm ./*.class

.PHONY:	all clean
