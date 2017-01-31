import argparse
from readfile import read_in_list

# 1の個数（正解の個数）を調べる
def count_one(lst):
    cnt = 0
    for num in lst:
        if num == str(1):
            cnt+=1
    return cnt


def calculate_prf(predict_list, true_list):
    tp = 0
    fp = 0
    fn = 0
    tn = 0

    if(len(predict_list) != len(true_list)):
        print('長さ違ってますよ')
        return

    for (predict, true) in zip(predict_list, true_list):
        if predict == str(1):
            if true ==str(1):
                tp += 1
            else:
                fp += 1
        else:
            if true ==str(1):
                fn += 1
            else:
                tn += 1
    
    print(tp, fp, fn, tn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f_measure = 2 * recall * precision / (recall + precision)
    return [precision, recall, f_measure]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'predict', type=str)
    parser.add_argument(
        'true', type=str, default='./test_sparce_feature')
    args = parser.parse_args()

    predict_list = read_in_list(args.predict)
    true_list = read_in_list(args.true)

    print(calculate_prf(predict_list, true_list))
