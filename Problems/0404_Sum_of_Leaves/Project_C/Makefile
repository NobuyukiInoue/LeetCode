CC=gcc
CC_FLAGS=-g -O0 -o

PROJECT_NAME=Sum_of_Leaves
SOURCE=$(PROJECT_NAME).c

MYLIB_PATH=../../mylib_C
MYLIB_NAME=mylib.c


ifeq ($(OS),Windows_NT)
	TARGET_FILE=$(PROJECT_NAME).exe
else ifeq ($(OS),macOS)
	TARGET_FILE=$(PROJECT_NAME)_for_mac
else ifeq ($(OS),linux)
	TARGET_FILE=$(PROJECT_NAME)_for_linux
else
	TARGET_FILE=$(PROJECT_NAME)
endif


all:	$(TARGET_FILE)

$(TARGET_FILE):	$(SOURCE) $(MYLIB_PATH)/$(MYLIB_NAME)
	$(CC) $(CC_FLAGS)$(TARGET_FILE) $(SOURCE) $(MYLIB_PATH)/$(MYLIB_NAME)

clean:
	rm $(TARGET_FILE)	# Can not run on Windows

.PHONY:	all clean
