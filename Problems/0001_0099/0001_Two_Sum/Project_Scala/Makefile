SCALAC = scalac
SCALAC_FLAGS = 

all:	Solution.class Main.class

Solution.class:	Solution.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

Main.class:	Main.scala
	$(SCALAC) $(SCALAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
