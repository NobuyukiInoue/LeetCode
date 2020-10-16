JAVAC =javac
JAVAC_FLAGS =

all:	ParkingSystem.class Solution.class Main.class

ParkingSystem.class:	ParkingSystem.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
