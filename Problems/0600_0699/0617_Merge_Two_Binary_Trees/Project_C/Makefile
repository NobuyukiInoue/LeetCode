CC=gcc
CC_FLAGS_DEBUG=-g -lm -O0 -o
CC_FLAGS_RELEASE=-lm -o

PROJECT_NAME=Merge_Two_Binary_Trees
SOURCE=$(PROJECT_NAME).c

MYLIB_PATH=../../../mylib_C
MYLIB_NAME=mylib.c

ifeq ($(OS),Windows_NT)
	TARGET_FILE=$(PROJECT_NAME).exe
else
UNAME=${shell uname}
ifeq ($(UNAME),Darwin)
	TARGET_FILE=$(PROJECT_NAME)_for_mac
else
ifeq ($(UNAME),Linux)
	TARGET_FILE=$(PROJECT_NAME)_for_linux
else
	TARGET_FILE=$(PROJECT_NAME)
endif
endif
endif

$(TARGET_FILE):	$(SOURCE) $(MYLIB_PATH)/$(MYLIB_NAME)
	$(CC) $(CC_FLAGS_RELEASE)$(TARGET_FILE) $(SOURCE) $(MYLIB_PATH)/$(MYLIB_NAME)

release:	$(SOURCE) $(MYLIB_PATH)/$(MYLIB_NAME)
	$(CC) $(CC_FLAGS_RELEASE)$(TARGET_FILE) $(SOURCE) $(MYLIB_PATH)/$(MYLIB_NAME)

debug:	$(SOURCE) $(MYLIB_PATH)/$(MYLIB_NAME)
	$(CC) $(CC_FLAGS_DEBUG)debug_$(TARGET_FILE) $(SOURCE) $(MYLIB_PATH)/$(MYLIB_NAME)

clean:
	rm $(TARGET_FILE)	# Can not run on Windows

.PHONY:	all clean
