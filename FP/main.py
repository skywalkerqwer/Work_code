from FP import fp_growth as fp

"""
# 测试
data = fp.load_data()
init_set = fp.create_init_set(data)

my_fp_tree, my_header_tab = fp.create_tree(init_set, 3)
my_fp_tree.disp()
"""

with open('kosarak.dat', 'r') as f:
    data = [line.split() for line in f.readlines()]
init_set = fp.create_init_set(data)

my_fp_tree, my_header_tab = fp.create_tree(init_set, 100000)

freq_items = []
fp.mine_tree(my_fp_tree, my_header_tab, 10000, set([]), freq_items)
for i in freq_items:
    print(i)