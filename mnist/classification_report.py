from sklearn.metrics import classification_report
import numpy as np

def read_data(file_path):
    """ 从文件中读取预测和真实标签 """
    y_pred = []
    y_true = []
    with open(file_path, 'r') as file:
        for line in file:
            pred, true = map(int, line.split())
            y_pred.append(pred)
            y_true.append(true)
    return np.array(y_pred), np.array(y_true)

def generate_classification_report(y_true, y_pred):
    """ 生成并打印分类报告 """
    report = classification_report(y_true, y_pred)
    print(report)

if __name__ == '__main__':
    predictions_path = 'final_predictions.txt'
    y_pred, y_true = read_data(predictions_path)
    generate_classification_report(y_true, y_pred)
