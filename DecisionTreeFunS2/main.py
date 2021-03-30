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

# how do we represent trees in Python? a few ways...
# 1. nested data structures (e.g. nested lists, nested dictionaries)
# 2. OOP (e.g. MyTree class...)

# we will do approach #1 (nested lists)
# each list can be one of three types ("Attribute", "Attribute Value", "Leaf")

# example... nested list tree representation for the interview tree
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
    # for now, we are going to select an attribute randomly
    # TODO: come back after you can build a tree with 
    # random attribute selection and replace with entropy
    rand_index = random.randrange(0, len(available_attributes))
    return available_attributes[rand_index]

def partition_instances(instances, split_attribute):
    # this is a group by split_attribute's domain, not by
    # the values of this attribute in instances
    # example: if split_attribute is "level"
    attribute_domain = attribute_domains[split_attribute] # ["Senior", "Mid", "Junior"]
    attribute_index = header.index(split_attribute) # 0
    # lets build a dictionary
    partitions = {} # key (attribute value): value (list of instances with this attribute value)
    # task: try this!
    for attribute_value in attribute_domain:
        partitions[attribute_value] = []
        for instance in instances:
            if instance[attribute_index] == attribute_value:
                partitions[attribute_value].append(instance)
    return partitions

def all_same_class(instances):
    # assumption: instances is not empty and class label is at index -1
    first_label = instances[0][-1]
    for instance in instances:
        if instance[-1] != first_label:
            return False 
    return True # if we get here, all instance labels matched the first label

def tdidt(current_instances, available_attributes):
    # basic approach (uses recursion!!):

    # select an attribute to split on
    split_attribute = select_attribute(current_instances, available_attributes)
    print("splitting on:", split_attribute)
    available_attributes.remove(split_attribute)
    # cannot split on the same attribute twice in a branch
    # recall: python is pass by object reference!!
    tree = ["Attribute", split_attribute]

    # group data by attribute domains (creates pairwise disjoint partitions)
    partitions = partition_instances(current_instances, split_attribute)
    print("partitions:", partitions)

    # for each partition, repeat unless one of the following occurs (base case)
    for attribute_value, partition in partitions.items():
        print("working with partition for:", attribute_value)
        value_subtree = ["Value", attribute_value]
        # TODO: appending leaf nodes and subtrees appropriately to value_subtree
        #    CASE 1: all class labels of the partition are the same => make a leaf node
        if len(partition) > 0 and all_same_class(partition):
            print("CASE 1")
        #    CASE 2: no more attributes to select (clash) => handle clash w/majority vote leaf node
        elif len(partition) > 0 and len(available_attributes) == 0:
            print("CASE 2")
        #    CASE 3: no more instances to partition (empty partition) => backtrack and replace attribute node with majority vote leaf node
        elif len(partition) == 0:
            print("CASE 3")
        else: # all base cases are false... recurse!!
            subtree = tdidt(partition, available_attributes.copy())
            # need to append subtree to value_subtree and appropriately append value subtre
            # to tree
    
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
    # TODO: compute the attribute domains dictionary
    # TODO: compute a "header" ["att0", "att1", ...]
    # my advice is to stitch together X_train and y_train
    train = [X_train[i] + [y_train[i]] for i in range(len(X_train))]
    # initial call to tdidt current instances is the whole table (train)
    available_attributes = header.copy() # python is pass object reference
    tree = tdidt(train, available_attributes)
    print("tree:", tree)

# 2 more topics in U5 Decision Trees
# 1. tree visualization w/graphviz (BONUS PA6)
# a tree is really a graph with some restrictions
# we will make a .dot file to represent our tree as a graph using the DOT language
# we will create a .pdf file from the .dot file
# 2. pruning
# bias vs variance tradeoff (read about this...)
# https://towardsdatascience.com/understanding-the-bias-variance-tradeoff-165e6942b229
# post pruning is more common
# need a "pruning set" to compute "static error rates"
# compute "estimated error rates" for each split
# if static error rate < estimated error rate for a subtree
# with height/depth = 1, then prune 
# prune -> replace with majority vote leaf node


fit_starter_code()