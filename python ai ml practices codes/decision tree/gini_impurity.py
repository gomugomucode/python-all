from collections import Counter

# counter is the dictonary subclass that automatically maps data points (as keys) to their total occurrence counts (as values) without requiring manual loops

# we have labels here
labels = ["unacc", "unacc", "acc", "acc", "good", "good"]
# labels = ["unacc","unacc","unacc", "good", "vgood", "vgood"]
# labels = ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc"]

# impurity mean measureness of randomness , mixedness of dataset
# formula for gini impurity = 1 - sum (probability of each label ^ 2)

# 1 - (2/6)^2 - (2/6)^2 - (2/6)^2 = 1 - 4/36 - 4/36 - 4/36 = 1 - 12/36 = 1 - 1/3 = 2/3 = 0.666

# we have impurity initialised to 1 so that we can subtract from it
impurity = 1


# we count the number of each label
# the labels are unacc, unacc, acc, acc, good, good
# total number of labels is 6
# number of unacc labels is 2
# number of acc labels is 2
# number of good labels is 2
# probability of unacc labels = 2/6 = 1/3
# probability of acc labels = 2/6 = 1/3
# probability of good labels = 2/6 = 1/3
label_counts = Counter(labels)

# loop through each label and calculate the probability of each label
for label in label_counts:
    # calculate the probability of each label
    probability_of_label = label_counts[label] / (len(labels))
    # subtract the square of the probability from impurity
    impurity -= probability_of_label**2

print(impurity)
