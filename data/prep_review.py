lines = []
count = 0

with open("./yelp_academic_dataset_review.json", "r", encoding="utf-8") as reader:
    while count <= 1000000:
        lines.append(reader.readline())
        count += 1

with open("./yelp_academic_dataset_review.json", "r", encoding="utf-8") as reader:
    for i, l in enumerate(reader):
            pass
    print("{} number of rows in reviews.json".format(i+1))

with open("./reviews_1000000.json", "w", encoding="utf-8") as writer:
    writer.writelines(lines)
