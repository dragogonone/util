import csv

###########################################
# csvファイルを読み込んでリストにして返す #
###########################################
def read_csv_in_list(filename, delimiter=','):
    lst = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            lst.append(row)
    return lst

###########################################
# 一列のファイルを読み込んでリストにして返す #
###########################################

def read_in_list(filename):
    lst = []
    with open(filename, 'r') as f:
        for row in f:
            row = row.replace('\n', '')
            row = row.replace('\r', '')
            lst.append(row)
    return lst

if __name__ == "__main__":
    lst = read_csv_in_list('evaluate.csv')
    print(lst)

