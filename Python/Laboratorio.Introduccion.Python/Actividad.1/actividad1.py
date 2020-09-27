# Definition
distinct_type_list = []

# Make some values

# All in indix 0 like a row []
# distinct_type_list.append([0, 1, 0.1, 0.2, "String1", "String2"])

# In diferent indexes
distinct_type_list.insert(0, 0)
distinct_type_list.insert(1, 1)
distinct_type_list.insert(2, 0.1)
distinct_type_list.insert(3, 0.2)
distinct_type_list.insert(4, "String1")
distinct_type_list.insert(5, "String2")

# Values in index 0 || [0], [1]......
print(distinct_type_list[0])

# Values 0 to 3
for i in range(4):
    print(distinct_type_list[i])

print("---------------")

# Append value (in final row)
distinct_type_list.append(1000)

# New value in index 1
distinct_type_list[1] = "Casa"

def visualize_list():
    if(len(distinct_type_list) != 0):
        for i in range(len(distinct_type_list)):
            print(distinct_type_list[i])
        print("----------------")

visualize_list()


if (distinct_type_list[1] != None or distinct_type_list[1] == "Casa"):
    del distinct_type_list[1]

visualize_list()