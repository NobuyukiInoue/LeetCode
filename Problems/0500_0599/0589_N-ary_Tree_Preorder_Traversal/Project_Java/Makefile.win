JAVAC =javac
JAVAC_FLAGS =-classpath .;..\..\jackson\jackson-core-2.9.8.jar;..\..\jackson\jackson-databind-2.9.8.jar;..\..\jackson\jackson-annotations-2.9.8.jar

all:	JsonUtil.class Node.class Operate_N_arr.class Mylib.class Solution.class Main.class

JsonUtil.class:	JsonUtil.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Node.class:	Node.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Operate_N_arr.class:	Operate_N_arr.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Mylib.class:	Mylib.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Solution.class:	Solution.java
	$(JAVAC) $(JAVAC_FLAGS) $<

Main.class:	Main.java
	$(JAVAC) $(JAVAC_FLAGS) $<

clean:
	rm ./*.class

.PHONY:	all clean
