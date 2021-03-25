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
    return partitions

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
    #    CASE 1: all class labels of the partition are the same => make a leaf node
    #    CASE 2: no more attributes to select (clash) => handle clash w/majority vote leaf node
    #    CASE 3: no more instances to partition (empty partition) => backtrack and replace attribute node with majority vote leaf node
    return None

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


fit_starter_code()