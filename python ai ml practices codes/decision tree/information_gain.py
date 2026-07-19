# Information Gain measures how much a feature reduces uncertainty or "impurity" in a dataset in decision tree

# Information gain measures difference in the impurity of the data before and after the split

# It is calculated by finding the difference between the dataset's starting uncertainty and the uncertainty remaining after a split
# formula = IG(D, A) = H(D) - H(D|A)
# where D is the dataset, A is the feature, H(D) is the entropy of the dataset, and H(D|A) is the conditional entropy of the dataset given the feature

# Entropy: The measure of uncertainty or impurity in a set of data. A highly mixed dataset has high entropy; a pure dataset (all belonging to one class) has zero entropy.

# Information Gain Formula: (Information Gain) = (Entropy (Before Split)) - (Weighted Average Entropy (After Split))


from collections import Counter


# unstructured or mixed data set for the splitting
unsplit_labels = [
    "unacc",
    "unacc",
    "unacc",
    "unacc",
    "unacc",
    "unacc",
    "good",
    "good",
    "good",
    "good",
    "vgood",
    "vgood",
    "vgood",
]

# two split data sets for comparison purpose
split_labels_1 = [
    ["unacc", "unacc", "unacc", "unacc", "unacc", "unacc", "good", "good", "vgood"],
    ["good", "good"],
    ["vgood", "vgood"],
]

split_labels_2 = [
    [
        "unacc",
        "unacc",
        "unacc",
        "unacc",
        "unacc",
        "unacc",
        "good",
        "good",
        "good",
        "good",
    ],
    ["vgood", "vgood", "vgood"],
]


# calculation of the gini
# gini impurity formula = 1 - sum of prob of each class squared


def gini(dataset):
    impurity = 1
    label_counts = Counter(dataset)

    for label in label_counts:
        prob_of_label = label_counts[label] / len(dataset)
        impurity -= prob_of_label**2

    return impurity


# calculating the information gain of the unstructured data set
# info gain = entropy of unsplit data - entropy of split data

info_gain = gini(unsplit_labels)
print(info_gain)


# calculating the information gain of the split data sets

# for subset in split_labels_1:
#   info_gain -= gini(subset)
#   print(info_gain)


# printing the gini impurity of the split data sets for comparison purpose one by one of  split_labels_1
for subset in split_labels_1:
    print(subset)
    print("Gini =", gini(subset))

# info_gain -= gini(split_labels_1[0])
# info_gain -= gini(split_labels_1[1])
# info_gain -= gini(split_labels_1[2])
