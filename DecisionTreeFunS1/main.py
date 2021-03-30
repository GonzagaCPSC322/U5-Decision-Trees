import random 


header = ["level", "lang", "tweets", "phd"]
attribute_domains = {"level": ["Senior", "Mid", "Junior"], 
        "lang": ["R", "Python", "Java"],
        "tweets": ["yes", "no"], 
        "phd": ["yes", "no"]}
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

# how to represent trees in python?? a few ways
# 1. OOP (e.g. a Node class (or struct) or a Tree class (or struct))
# 2. nested data structures (e.g. nested lists)

# we are going to do approach #2
# there are three types of lists (Attribute, Attribute Value, Leaf)
# example!! build the solution decision tree for the interview data
# using nested lists
# index 0 types
# index 1 value of the type
interview_tree = \
["Attribute", "level", 
    ["Value", "Senior", 
        ["Attribute", "tweets", 
            ["Value", "yes", 
                ["Leaf", "True", 2, 5]
            ],
            ["Value", "no", 
                ["Leaf", "False", 3, 5]
            ]
        ]
    ],
    ["Value", "Mid", 
        ["Leaf", "True", 4, 14]
    ],
    ["Value", "Junior", 
        ["Attribute", "phd", 
            ["Value", "yes", 
                ["Leaf", "False", 2, 5]
            ],
            ["Value", "no", 
                ["Leaf", "True", 3, 5]
            ]
        ]
    ]
]

def select_attribute(instances, available_attributes):
    # for now, lets choose an attribute randomly
    # TODO: later... after you can succcessfully build a tree
    # replace random w/entropy
    rand_index = random.randrange(0, len(available_attributes))
    return available_attributes[rand_index]

def partition_instances(instances, split_attribute):
    # comments refer to split_attribute "level"
    attribute_domain = attribute_domains[split_attribute] # ["Senior", "Mid", "Junior"]
    attribute_index = header.index(split_attribute) # 0

    partitions = {} # key (attribute value): value (partition)
    # task: try to finish this
    for attribute_value in attribute_domain:
        partitions[attribute_value] = []
        for instance in instances:
            if instance[attribute_index] == attribute_value:
                partitions[attribute_value].append(instance)

    return partitions 


def tdidt(current_instances, available_attributes):
    # basic approach (uses recursion!!):

    # select an attribute to split on
    split_attribute = select_attribute(current_instances, available_attributes)
    print("splitting on:", split_attribute)
    # remove split attribute from available attributes
    # because, we can't split on the same attribute twice in a branch
    available_attributes.remove(split_attribute) # Python is pass by object reference!!
    tree = ["Attribute", split_attribute]

    # group data by attribute domains (creates pairwise disjoint partitions)
    partitions = partition_instances(current_instances, split_attribute)
    print("partitions:", partitions)
    # for each partition, repeat unless one of the following occurs (base case)
    for attribute_value, partition in partitions.items():
        values_subtree = ["Value", attribute_value]
        # TODO: append your leaf nodes to this list appropriately
        #    CASE 1: all class labels of the partition are the same => make a leaf node
        if len(partition) > 0 and all_same_class(partition):
            print("CASE 1")
        #    CASE 2: no more attributes to select (clash) => handle clash w/majority vote leaf node
        elif len(partition) > 0 and len(available_attributes) == 0:
            print("CASE 2")
        #    CASE 3: no more instances to partition (empty partition) => backtrack and replace attribute node with majority vote leaf node
        elif len(partition) == 0:
            print("CASE 3")
        else: # all base cases are false, recurse!!
            subtree = tdidt(partition, available_attributes.copy())
    return tree

# PA6 TODO (do a step a day for 7 days)
# 1. all_same_class()
# 2. append subtree to values_subtree and to tree appropriately
# 3. work on CASE 1, then CASE 2, then CASE 3 (write helper functions!!)
# e.g. compute_partition_stats()
# 4. finish the TODOs in fit_starter_code()
# 5. replace random w/entropy (compare tree w/interview_tree)
# 6. move over starter code to PA6 OOP w/unit test fit()
# 7. move on to predict()...

def fit_starter_code():
    # fit() accepts X_train and y_train
    # TODO: calculate the attribute domains dictionary
    # TODO: calculate a header (e.g. ["att0", "att1", ...])
    # my advice: stitch together X_train and y_train
    train = [X_train[i] + [y_train[i]] for i in range(len(X_train))]
    available_attributes = header.copy() # recall: Python is pass
    # by object reference
    # initial tdidt() call
    tree = tdidt(train, available_attributes)
    print("tree:", tree)



fit_starter_code()

# 2 more U5 Decision Trees topics
# 1. tree visualization (BONUS PA6)
# need to install graphviz in your docker container
# a tree is a graph with some restrictions
# specify our tree using the DOT graph language
# create a .pdf file from a .dot (represents our tree in DOT language)
# 2. pruning
# bias vs variance trade-off (read about it...)
# https://towardsdatascience.com/understanding-the-bias-variance-tradeoff-165e6942b229
# post pruning is more common
# for post pruning, you typically hold out "pruning set"
# static error rates from running your tree over the pruning set
# if the static error rate at a subtree with height/depth == 1 is <
# the estimated error rate (at that that subtree), then prune
# (replace this subtree with majority vote leaf node)