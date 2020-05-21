import os

def get_new_file(lis):
    l = []
    for name in lis:
        index = name.split('-')[1]
        l.append(index)
    min_index = max(l)
    for name in lis:
        if min_index in name:
            return name

def get_file_name():
    sale_file = []
    member_file = []
    for root, dirs, files in os.walk(r'C:\Users\Healthlink\Desktop\新建文件夹\\'):
        for file in files:
            if '营销员' in file:
                sale_file.append(file)
            if '会员' in file:
                member_file.append(file)
    if len(sale_file) == 1:
        s = sale_file[0]
    elif len(sale_file) > 1:
        s = get_new_file(sale_file)
    if len(member_file) == 1:
        m = member_file[0]
    elif len(member_file) > 1:
        m = get_new_file(member_file)
    return s, m
if __name__ == '__main__':
    s,m = get_file_name()
    print(s)
    print(m)