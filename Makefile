CC = gcc
CFLAGS = -Iinclude -Wall
LDFLAGS = 
TARGET = mnist
PYSCRIPT = draw_result.py

# 源代码文件和目标文件
SRC = $(wildcard *.c)
OBJ = $(SRC:.c=.o)

all: $(TARGET) run_py

$(TARGET): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

run_py:
	python $(PYSCRIPT)

clean:
	rm -f $(OBJ) $(TARGET)

.PHONY: clean all run_py


