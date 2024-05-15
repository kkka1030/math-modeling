#include <stdio.h>
#include "createBMP.h"
#include "mnist_file.h"

int main() {  

    const int width = 28;                          
    const int height = 28;                         
    const int pixel_size = 3;                         

    struct BMPHeader header;
    int padding = createBMPHeader(&header, width, height, pixel_size);
    FILE *file = fopen("test.bmp", "wb");
    fwrite(&header, sizeof(header), 1, file);

    mnist_dataset_t * dataset = mnist_get_dataset("data/train-images-idx3-ubyte", "data/train-labels-idx1-ubyte");  
    if (dataset == NULL) {  
        printf("Could not open MNIST dataset\n");  
        return 1;  
    }  

    mnist_image_t* image = &dataset->images[0];

    // 逐行写入像素数据
    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            int idx = y * width + x;
            int pixel = 255 - image->pixels[idx];
            unsigned char color[3] = {pixel, pixel, pixel};
            fwrite(color, 1, 3, file);
        }
        // 写入填充字节, 每行必须是 4 的倍数
        for (int p = 0; p < padding; p++)
        {
            fputc(0, file);
        }
    }
    fclose(file);  
  
    mnist_free_dataset(dataset);  
  
    return 0;  
}  