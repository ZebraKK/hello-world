
TARGET= helloworld

SRC_DIR= ./
INC_DIR= ./
LIB_DIR= ./

APP_SRC=$(wildcard *.cpp)
APP_INC=
APP_LIB=

CC=g++ -std=c++11

#-shared -fPIC

#CPPFLAGS=-g -Wall -shared -fPIC -Werror -I$(INC_DIR) -L$(LIB_DIR)
CPPFLAGS=-g -Wall -I$(INC_DIR) -L$(LIB_DIR)

.PHONY: all install clean

all: $(TARGET)

$(TARGET):
	$(CC) -o $@ $(CPPFLAGS) $(APP_SRC)

install:

clean:
	-$(RM) $(TARGET)