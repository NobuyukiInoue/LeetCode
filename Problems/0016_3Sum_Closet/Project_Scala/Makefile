SCALAC = scalac
SCALAC_FLAGS = 

all:	Main.class Solution.class

ALL:	Main.class Solution.class

Main.class:	Solution.class Main.scala
	$(SCALAC) $(SCALAC_FLAGS) Main.scala

Solution.class:	Solution.scala
	$(SCALAC) $(SCALAC_FLAGS) Solution.scala

clean:
	rm ./*.class

.PHONY:	all clean
