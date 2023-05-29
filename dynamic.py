from os import walk, getcwd

mypath = "data/"
txt_name_list = []
for (dirpath, dirnames, filenames) in walk(mypath):
    if filenames != '.DS_Store':       ##Ugh mac junk
        txt_name_list.extend(filenames)
        break

print(txt_name_list)