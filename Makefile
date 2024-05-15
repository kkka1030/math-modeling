CC = gcc
CFLAGS = -lm

# 目标文件
TARGET = mnist

# 源文件
SRCS = mnist.c mnist_file.c neural_network.c createBMP.c

# 生成的目标
all: $(TARGET)

$(TARGET): $(SRCS)
	$(CC) $(SRCS) $(CFLAGS) -o $(TARGET)

# 清理目标
clean:
	rm -f $(TARGET)

