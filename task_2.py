your_list = input().split()
print(your_list)
your_list_set = set(your_list)
if len(your_list_set) == len(your_list):
    print('There are NO repeated items!')
else:
    print('There are duplicates.')