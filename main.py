def read_file_line_by_line():
    file1 = open('result.txt', 'r')
    lines = file1.readlines()
    item_list = []
    for line in lines:
        line = line.strip()
        # if not is_empty(line)

    file1.close()
    return item_list


def is_empty(str):
    return str == ""


if __name__ == '__main__':
    positive_sentiments = {"MISCELLANEOUS": 0, "EXPERIENCE": 0, "PRICE":0, "SERVICE":0 , "FOOD":0 , "ATTRACTIONS":0, "RIDES": 0 }
    negative_sentiments = {"MISCELLANEOUS": 0, "EXPERIENCE": 0, "PRICE":0, "SERVICE":0 , "FOOD":0 , "ATTRACTIONS":0, "RIDES": 0 }
    read_file_line_by_line(positive_sentiments, negative_sentiments)
