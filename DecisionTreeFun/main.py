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