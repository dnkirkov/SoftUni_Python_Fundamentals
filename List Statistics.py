# On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create
# and print two lists:
# • One with all the positives (including 0) numbers
# • One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}"
# "Sum of negatives: {sum_of_negatives}"

count = int(input())
positive_list = list()
negative_list = list()
for i in range(count):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
