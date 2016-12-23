CUR_DIR=
TOP_DIR=
INC_PATH=
SRCS_DIR=

TARGET=


OBJS=
SRCS=$(foreach src,$(SRCS_DIR),$(wildcard *.c))



CC=
LD=
AR=

CFLAG=
LDFLAG=

all:

$(SRCS_DIR/%.o):$(SRCS_DIR)/%.c
	$(CC) -c -o $@ $(CFLAG) $<

#ar
$(TARGET_AR):$(OBJS)
	$(AR) crus $(TARGET_AR) $(OBJS)
#so
$(TARGET_SO):$(OBJS)
	$(LD) $(OBJS) -o $(TARGET_SO) $(LDFLAG)
	

install:

clean:



#include
#export


