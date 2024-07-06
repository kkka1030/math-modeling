#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

#include "include/mnist_file.h"
#include "include/neural_network.h"

#include "include/createBMP.h"

#define STEPS 1000
#define BATCH_SIZE 100


const char * train_images_file = "data/train-images-idx3-ubyte";
const char * train_labels_file = "data/train-labels-idx1-ubyte";
const char * test_images_file = "data/t10k-images-idx3-ubyte";
const char * test_labels_file = "data/t10k-labels-idx1-ubyte";

/**
 * Calculate the accuracy of the predictions of a neural network on a dataset.
 */
float calculate_accuracy(mnist_dataset_t * dataset, neural_network_t * network)
{
    float activations[MNIST_LABELS], max_activation;
    int i, j, correct, predict;

    // Loop through the dataset
    for (i = 0, correct = 0; i < dataset->size; i++) {
        // Calculate the activations for each image using the neural network
        neural_network_hypothesis(&dataset->images[i], network, activations);

        // Set predict to the index of the greatest activation
        for (j = 0, predict = 0, max_activation = activations[0]; j < MNIST_LABELS; j++) {
            if (max_activation < activations[j]) {
                max_activation = activations[j];
                predict = j;
            }
        }

        // Increment the correct count if we predicted the right label
        if (predict == dataset->labels[i]) {
            correct++;
        }
    }

    // Return the percentage we predicted correctly as the accuracy
    return ((float) correct) / ((float) dataset->size);
}

void save_weight(neural_network_t * network)
{
    const int width = 28;                          
    const int height = 28;                         
    const int pixel_size = 3;                         

    struct BMPHeader header;

    // 计算填充字节数
    int padding = (4 - (width * pixel_size) % 4) % 4;

    // 创建BMP头
    createBMPHeader(&header, width, height, pixel_size, padding);

    for (int i = 0; i < MNIST_LABELS; i++)
    {
        char filename[16];
        sprintf(filename, "weight%02d.bmp", i);
        FILE *file = fopen(filename, "wb");
        fwrite(&header, sizeof(header), 1, file);

        float average_weight = 0.0;
        float min_weight = 1.0;
        float max_weight = -1.0;
        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                int idx = y * width + x;
                double current_weight = network->W[i][idx];
                average_weight += current_weight;
                if (min_weight > current_weight)
                    min_weight = current_weight;
                if (max_weight < current_weight)
                    max_weight = current_weight;
            }
        }
        average_weight = average_weight / (height * width);
        float weight_width = max_weight - min_weight;
        
        // 逐行写入像素数据
        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                int idx = y * width + x;
                double current_weight = network->W[i][idx];
                float normalized_weight = 0.0;
                unsigned char color[3] = {0, 0, 0};
                if (current_weight > average_weight)
                {
                    normalized_weight = (current_weight - average_weight) / (max_weight - average_weight);
                    int pixel = (int)(normalized_weight * 255);
                    color[2] = pixel;
                    color[1] = color[0] = 0;
                }
                else
                {
                    normalized_weight = (average_weight - current_weight) / (average_weight - min_weight);
                    int pixel = (int)(normalized_weight * 255);
                    color[0] = pixel;
                    color[1] = color[2] = 0;
                }
                fwrite(color, 1, 3, file);
            }
            // 写入填充字节, 每行必须是 4 的倍数
            for (int p = 0; p < padding; p++)
            {
                fputc(0, file);
            }
        }
        fclose(file);  
    }
}
int main() {
    FILE *fp = fopen("result.txt", "w"); // 打开文件用于记录损失和准确率
    FILE *fp_final; // 用于在最后一次迭代后记录预测结果和真实标签
    if (fp == NULL) {
        perror("Unable to open file");
        return 1;
    }

    mnist_dataset_t *train_dataset = mnist_get_dataset(train_images_file, train_labels_file);
    mnist_dataset_t *test_dataset = mnist_get_dataset(test_images_file, test_labels_file);
    if (train_dataset == NULL || test_dataset == NULL) {
        fprintf(stderr, "Failed to load datasets.\n");
        return 1;
    }

    neural_network_t *network = malloc(sizeof(neural_network_t));
    if (network == NULL) {
        fprintf(stderr, "Failed to allocate memory for the neural network.\n");
        return 1;
    }
    neural_network_random_weights(network);

    printf("Training the network...\n");
    for (int step = 0; step < STEPS; step++) {
        float loss = neural_network_training_step(train_dataset, network, 0.01);
        float accuracy = calculate_accuracy(test_dataset, network);
        fprintf(fp, "%d\t%.3f\t%.2f\n", step, loss, accuracy * 100);
        if (step % 100 == 0) {
            printf("Step %d, Loss: %.3f, Accuracy: %.2f%%\n", step, loss, accuracy * 100);
        }

        if (step == STEPS - 1) { // 最后一次迭代
            fp_final = fopen("final_predictions.txt", "w");
            if (fp_final == NULL) {
                perror("Unable to open final predictions file");
                return 1;
            }
            for (int i = 0; i < test_dataset->size; i++) {
                int predicted_label = predict(network, &test_dataset->images[i]);
                fprintf(fp_final, "%d %d\n", predicted_label, test_dataset->labels[i]);
            }
            fclose(fp_final); // 关闭最终预测结果文件
        }
    }

    save_weight(network);
    mnist_free_dataset(train_dataset);
    mnist_free_dataset(test_dataset);
    free(network);
    fclose(fp); // 关闭结果文件

    return 0;
}
