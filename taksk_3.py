def make_file_list(file_name):
    list = []
    list.append(file_name)
    with open (file_name) as f:
        list.append(str(len(f.readlines())))
    with open (file_name) as f:
        list.append(f.read())
    return list
    
def right_sequence():
    list = []
    list.append(make_file_list('1.txt'))
    list.append(make_file_list('2.txt'))
    list.append(make_file_list('3.txt'))
    list.sort(key=lambda x:x[1])
    return list

with open ('final.txt', 'w') as f:
    for el in right_sequence():
        f.write(f'{str(el[0])}\n')
        f.write(f'{str(el[1])}\n')
        f.write(f'{str(el[2])}\n')