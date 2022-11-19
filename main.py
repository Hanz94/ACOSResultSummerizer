def count_sentiments(line, pos_list, neg_list):
    cat_and_sentiment = line.split("#")
    if len(cat_and_sentiment) > 1 and cat_and_sentiment[0] in pos_list:
        category = cat_and_sentiment[0]
        sentiment = int(cat_and_sentiment[1].strip())
        if sentiment == 0:
            neg_list[category] = neg_list.get(category) + 1
        elif sentiment == 2:
            pos_list[category] = pos_list.get(category) + 1


def calculate_ratings(pos_list, neg_list):
    print("----------------ASPECT BASED RATINGS---------------")
    for cat in pos_list:
        rating = (pos_list[cat] / (pos_list[cat] + neg_list[cat])*4) + 1
        print(cat)
        print(rating)

def read_file_line_by_line(pos_list, neg_list):
    file1 = open('result.txt', 'r')
    lines = file1.readlines()
    item_list = []
    for line in lines:
        line = line.strip()
        if not is_empty(line):
            count_sentiments(line, pos_list, neg_list)
    file1.close()
    return item_list


def is_empty(str):
    return str == ""


if __name__ == '__main__':
    positive_sentiments = {"MISCELLANEOUS": 0, "EXPERIENCE": 0, "PRICE": 0, "SERVICE": 0, "FOOD": 0, "ATTRACTIONS": 0, "RIDES": 0}
    negative_sentiments = {"MISCELLANEOUS": 0, "EXPERIENCE": 0, "PRICE": 0, "SERVICE": 0, "FOOD": 0, "ATTRACTIONS": 0, "RIDES": 0}
    read_file_line_by_line(positive_sentiments, negative_sentiments)
    print("Positive Sentiments by Category:")
    print(positive_sentiments)
    print("Negative Sentiments by Category:")
    print(negative_sentiments)
    calculate_ratings(positive_sentiments, negative_sentiments)
