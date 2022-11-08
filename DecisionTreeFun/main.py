import numpy as np

X_train = [
        ["Senior", "Java", "no", "no"],
        ["Senior", "Java", "no", "yes"],
        ["Mid", "Python", "no", "no"],
        ["Junior", "Python", "no", "no"],
        ["Junior", "R", "yes", "no"],
        ["Junior", "R", "yes", "yes"],
        ["Mid", "R", "yes", "yes"],
        ["Senior", "Python", "no", "no"],
        ["Senior", "R", "yes", "no"],
        ["Junior", "Python", "yes", "no"],
        ["Senior", "Python", "yes", "yes"],
        ["Mid", "Python", "no", "yes"],
        ["Mid", "Java", "yes", "no"],
        ["Junior", "Python", "no", "yes"]
    ]

y_train = ["False", "False", "True", "True", "True", "False", "True", "False", "True", "True", "True", "True", "True", "False"]

# TODO: in fit(), programmatically build header and attribute_domains
# using X_train. perhaps store as attributes of MyDecisionTreeClassifier
header = ["att0", "att1", "att2", "att3"]
attribute_domains = {"att0": ["Junior", "Mid", "Senior"], 
        "att1": ["Java", "Python", "R"],
        "att2": ["no", "yes"], 
        "att3": ["no", "yes"]}

# how to represent trees in Python?
# 1. nested data structures (like dictionaries, lists, etc.)
# 2. OOP (e.g. MyTree class)

# we will use a nested list approach
# at element 0: data type (Attribute, Value, Leaf)
# at element 1: data value (attribute name, 
# value name, class label)
# rest of elements: depends on the type
# example!
# TASK: finish the tree!
interview_tree_solution =   ["Attribute", "att0", 
                                ["Value", "Junior", 
                                    ["Attribute", "att3",
                                        ["Value", "no",
                                            ["Leaf", "True", 3, 5]
                                        ],
                                        ["Value", "yes", 
                                            ["Leaf", "False", 2, 5]
                                        ]
                                    ]
                                ],
                                ["Value", "Mid", 
                                    ["Leaf", "True", 4, 14]
                                ],
                                ["Value", "Senior", 
                                    ["Attribute", "att2", 
                                        ["Value", "no", 
                                            ["Leaf", "False", 3, 5]
                                        ],
                                        ["Value", "yes",
                                            ["Leaf", "True", 2, 5]
                                        ]
                                    ]
                                ]
                            ]

def select_attribute(instances, attributes):
    # TODO: implement the Enew algorithm to select the
    # attribute with the lowest entropy
    # for now, let's use random selection
    rand_index = np.random.randint(0, len(attributes))
    return attributes[rand_index]

def partition_instances(instances, attribute):
    # this is a group by attribute domain
    att_index = header.index(attribute)
    att_domain = attribute_domains["att" + str(att_index)]
    print("attribute domain:", att_domain)
    # lets use dictionaries
    partitions = {}
    for att_value in att_domain:
        partitions[att_value] = []
        for instance in instances:
            if instance[att_index] == att_value:
                partitions[att_value].append(instance)
    return partitions

def same_class_label(instances):
    first_label = instances[0][-1]
    for instance in instances:
        if instance[-1] != first_label:
            return False
    # get here, all the same
    return True

def tdidt(current_instances, available_attributes):
    # basic approach (uses recursion!!):
    print("available attributes:", available_attributes)

    # select an attribute to split on
    split_attribute = select_attribute(current_instances, available_attributes)
    print("splitting on:", split_attribute)
    available_attributes.remove(split_attribute)
    # cannot split on this attribute again in this branch of tree
    tree = ["Attribute", split_attribute]

    # group data by attribute domains (creates pairwise disjoint partitions)
    partitions = partition_instances(current_instances, split_attribute)
    print("partitions:", partitions)

    # for each partition, repeat unless one of the following occurs (base case)
    for att_value, att_partition in partitions.items():
        value_subtree = ["Value", att_value]
        if len(att_partition) > 0 and same_class_label(att_partition):
            print("CASE 1 all same class label")
            #    CASE 1: all class labels of the partition are the same
            # => make a leaf node
        elif len(att_partition) > 0 and len(available_attributes) == 0:
            print("CASE 2 clash")
            #    CASE 2: no more attributes to select (clash)
            # => handle clash w/majority vote leaf node
        elif len(att_partition) == 0:
            print("CASE 3 empty partition")
            #    CASE 3: no more instances to partition (empty partition)
            # => backtrack and replace attribute node with majority vote leaf node
        else: # none of the bases cases were true...recurse!!
            print("Recursing!!!")
            subtree = tdidt(att_partition, available_attributes.copy())
            value_subtree.append(subtree)
        tree.append(value_subtree)

    return tree

def fit_starter_code():
    # note the TODO above
    # here would be a good place to programmatically extract
    # the header and attribute_domains
    # next, I recommend stitching X_train and y_train together
    # so the class label is at instance[-1]
    train = [X_train[i] + [y_train[i]] for i in range(len(X_train))]
    available_attributes = header.copy() # recall tdidt is going
    # to be removing attributes from a list of available attributes
    # python is pass by object reference!!!
    tree = tdidt(train, available_attributes)
    print("tree:", tree)
    # note the unit test will assert tree == interview_tree_solution

fit_starter_code()

# general Enew algorithm pseudocode
# for each available attribute:
#   for each attribute value in the domain:
#       Compute the entropy of that value partition
#           (e.g. proportion and log for each class)
#   Compute Enew by taking weighted sum of the partition entropies
# Choose to split on the attribute with the smallest Enew

# PA7 TODO (do a step a day for 7 days, starting today)
# 1. thurs: all_same_class()
# 2. fri: append subtree to value_subtree and to tree appropriately
# 3. sat: work on CASE 1, then CASE 2, then CASE 3 (write helper functions!!)
# 4. sun: finish the TODOs in fit_starter_code()
# 5. mon: replace random w/entropy (compare tree w/interview_tree_solution... note attribute domain ordering may need to be adjusted)
# 6. tues: Implement unit test for fit() and move starter code over to OOP 
# 7. weds: move on to predict()

def tdidt_predict(tree, instance):
    # are we at a leaf node (base case)
    # or an attribute node (need to recurse)
    info_type = tree[0] # Attribute or Leaf
    if info_type == "Leaf":
        # base case
        return tree[1] # label

    # if we are here, then we are at an Attribute node
    # we need to figure where in instance, this attribute's value is
    att_index = header.index(tree[1])
    # now loop through all of the value lists, looking for a 
    # match to instance[att_index]
    for i in range(2, len(tree)):
        value_list = tree[i]
        if value_list[1] == instance[att_index]:
            # we have a match, recurse on this value's subtree
            return tdidt_predict(value_list[2], instance)


# predict starter code!!
def predict_starter_code():
    # we need some unseen instances
    instance1 = ["Junior", "Java", "yes", "no"] # True
    instance2 = ["Junior",  "Java", "yes", "yes"] # False
    instance3 = ["Intern",  "Java", "yes", "yes"] # None
    # b/c "Intern" is not in the attribute domain for att0 (level)
    prediction = tdidt_predict(interview_tree_solution, instance3)
    print("prediction:", prediction)

predict_starter_code()

# 2 more short tree topics for unit 5 (U5)
# 1. tree visualization (BONUS for PA7)
# we will use the dot language (from graphviz) to represent
# a tree as a graph
# then we will create a PDF using the dot program
# note: you will need to install the docker dependencies for graphviz
# example: interview_tree.dot

# 2. tree pruning (no coding part for PA7)
# decision trees are notorious for overfitting to a training set
# this means that trees don't tend to genrealize well to unseen
# instances
# to combat this, you typically do pruning, such as post-
# pruning with a pruning set