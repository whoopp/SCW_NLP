import numpy as np

name_list = [
    # name
]

hist_dict = {
    # name: uses
}

hist_list = [
    # [name, occurance]
]

with open('PLACEHOLDER') as f: #textfile with a flair every line
    name_list = f.readlines()

for i in range(len(name_list)):
    if not name_list[i] in hist_dict.keys():
        hist_dict.__setitem__(
            name_list[i],
            name_list.count(name_list[i]),
        )
else:
    pass

for iter in hist_dict.keys():
    hist_list.append([iter, hist_dict[iter]])

# replace print with whatever function you want.
hl_sorted = np.sort(hist_list[::-1])
print(hl_sorted)