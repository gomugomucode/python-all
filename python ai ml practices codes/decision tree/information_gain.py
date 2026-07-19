# Information Gain measures how much a feature reduces uncertainty or "impurity" in a dataset in decision tree

# Information gain measures difference in the impurity of the data before and after the split

# It is calculated by finding the difference between the dataset's starting uncertainty and the uncertainty remaining after a split
# formula = IG(D, A) = H(D) - H(D|A)
# where D is the dataset, A is the feature, H(D) is the entropy of the dataset, and H(D|A) is the conditional entropy of the dataset given the feature

# Entropy: The measure of uncertainty or impurity in a set of data. A highly mixed dataset has high entropy; a pure dataset (all belonging to one class) has zero entropy.

# Information Gain Formula: (Information Gain) = (Entropy (Before Split)) - (Weighted Average Entropy (After Split))
