names = ["Milly", "Alex", "Kate", "Chris", "Maurice", "Arnold", "Antony"]

my_list = []

for name in names:
    my_list.append(len(name))

print("Without Comprehension:", my_list)

my_list = [len(name) for name in names]

print("With Comprehension:", my_list)