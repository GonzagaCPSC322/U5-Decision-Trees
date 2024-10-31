

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
interview_tree_solution =   ["Attribute", "att0", 
                                ["Value", "Junior", 
                                    ["Attribute", "att3",
                                        ["Value", "no",
                                            ["Leaf", "True", 3, 5]
                                        ]# TASK: finish the tree!
                                    ]
                                ]
                            ]
def tdidt(current_instances, available_attributes):
    # basic approach (uses recursion!!):
    # select an attribute to split on
    # group data by attribute domains (creates pairwise disjoint partitions)
    # for each partition, repeat unless one of the following occurs (base case)
    #    CASE 1: all class labels of the partition are the same => make a leaf node
    #    CASE 2: no more attributes to select (clash) => handle clash w/majority vote leaf node
    #    CASE 3: no more instances to partition (empty partition) => backtrack and replace attribute node with majority vote leaf node
    return None

def fit_starter_code():
    # note the TODO above
    # here would be a good place to programmatically extract
    # the header and attribute_domains
    pass

fit_starter_code()