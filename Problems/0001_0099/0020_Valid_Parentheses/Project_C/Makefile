CC=gcc
CC_FLAGS_DEBUG=-g -lm -O0 -o
CC_FLAGS_RELEASE=-lm -o

PROJECT_NAME=main
SOURCE=$(PROJECT_NAME).c

MYLIB_PATH=lib/mylib.c

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

all:	$(TARGET_FILE)

$(TARGET_FILE):	$(SOURCE) $(MYLIB_PATH)
	$(CC) $(CC_FLAGS_RELEASE)$(TARGET_FILE) $(SOURCE) $(MYLIB_PATH)

debug:	$(SOURCE) $(MYLIB_PATH)
	$(CC) $(CC_FLAGS_DEBUG)$(TARGET_FILE) $(SOURCE) $(MYLIB_PATH)

clean:
	rm $(TARGET_FILE)	# Can not run on Windows

.PHONY:	all clean
