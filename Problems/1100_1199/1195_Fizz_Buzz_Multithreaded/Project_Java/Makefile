JAVAC =javac
JAVAC_FLAGS =

all:	FizzBuzz.class Solution.class Main.class

FizzBuzz.class:	FizzBuzz.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
