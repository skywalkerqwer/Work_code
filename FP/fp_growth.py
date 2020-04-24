"""
    FP-Growth算法
"""


class TreeNode():
    def __init__(self, name_value, num_occur, parent_node):
        """
        :param name_value: 节点名字
        :param num_occur: 计数
        :param parent_node: 当前节点的父节点
        """
        self.name = name_value
        self.count = num_occur
        self.node_link = None  # 链接相似的元素
        self.parent = parent_node
        self.children = {}  # 存放当前节点的子节点

    def inc(self, num_occur):
        self.count += num_occur

    def disp(self, ind=1):
        print(' ' * ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind + 1)


def update_header(node2test, target_node):
    while (node2test.node_link != None):
        node2test = node2test.node_link
    node2test.node_link = target_node


def update_tree(items, in_tree, header_table, count):
    # 首先测试第一个元素项是否作为子节点存在
    if items[0] in in_tree.children:
        # 若存在，则更新元素项的计数
        in_tree.children[items[0]].inc(count)
    else:
        # 不存在则创建一个新的TreeNode将其作为一个子节点添加到树中
        in_tree.children[items[0]] = TreeNode(items[0], count, in_tree)

        if header_table[items[0]][1] is None:
            # 若没有头指针则指向自己
            header_table[items[0]][1] = in_tree.children[items[0]]
        else:
            # 否则更新头指针指向新的节点
            update_header(header_table[items[0]][1], in_tree.children[items[0]])
    if len(items) > 1:
        # 对剩下的元素项递归迭代
        update_tree(items[1::], in_tree.children[items[0]], header_table, count)


def create_tree(data_set, min_sup=1):
    header_table = {}
    # 第一遍历数据集，统计每个元素项出现的频度
    for trans in data_set:
        for item in trans:
            header_table[item] = header_table.get(item, 0) + data_set[trans]

    # 阈值过滤
    for k in list(header_table.keys()):  # 字典在遍历时不可修改，转成list处理
        if header_table[k] < min_sup:
            del (header_table[k])

    # 满足最小支持度的频繁项集
    freq_item_set = set(header_table.keys())

    # 如果没有元素项满足要求，则退出
    if len(freq_item_set) == 0:
        return None, None

    # 扩展头指针以便保存计数值和每种类型第一个元素项的指针
    for k in header_table:
        header_table[k] = [header_table[k], None]

    # 创建只包含空集合的根节点
    re_tree = TreeNode('Null set', 1, None)

    # 第二次遍历数据集，只考虑频繁项
    for tran_set, count in data_set.items():
        # data_set：[element, count]
        local_d = {}
        for item in tran_set:
            if item in freq_item_set:  # 过滤，只取样本中满足最小支持度的频繁项
                local_d[item] = header_table[item][0]  # element : count
        if len(local_d) > 0:
            # 根据全局频数从大到小对单样本排序
            ordered_items = [v[0] for v in sorted(local_d.items(), key=lambda p: p[1], reverse=True)]
            # 用过滤且排序后的样本更新树
            update_tree(ordered_items, re_tree, header_table, count)
    return re_tree, header_table


def ascend_tree(leaf_node, prefix_path):
    # 迭代上溯整棵树
    if leaf_node.parent is not None:
        prefix_path.append(leaf_node.name)
        ascend_tree(leaf_node.parent, prefix_path)


# 条件模式基
def find_pref_fix_path(base_pat, my_header_tab):
    tree_node = my_header_tab[base_pat][1]  # base_pat在FP树中的第一个结点
    cond_pat = {}
    while tree_node is not None:
        prefix_path = []
        ascend_tree(tree_node, prefix_path)  # prefix_path 是倒过来的，从tree_node开始到根
        if len(prefix_path) > 1:
            cond_pat[frozenset(prefix_path[1:])] = tree_node.count  # 关联tree_node的计数
        tree_node = tree_node.node_link  # 下一个base_pat结点
    return cond_pat


# 递归查找频繁项
def mine_tree(in_tree, header_table, min_sup, pre_fix, freq_item_list):
    # 从头指针表的底端开始
    big_l = [v[0] for v in sorted(header_table.items(), key=lambda p:p[1])]  # 根据频繁项的总频进行排序
    for base_pat in big_l:
        new_freq_set = pre_fix.copy()
        new_freq_set.add(base_pat)
        freq_item_list.append(new_freq_set)
        cond_pat_bases = find_pref_fix_path(base_pat, header_table)  # 当前频繁项集的条件模式基
        my_cond_tree, my_head = create_tree(cond_pat_bases,  min_sup)  # 构造当前频繁项的条件FP树
        if my_head is not None:
            mine_tree(my_cond_tree, my_head, min_sup, new_freq_set, freq_item_list)  # 递归挖掘条件FP树


def load_data():
    # 测试数据集
    data = [
        ['r', 'z', 'h', 'j', 'p'],
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
        ['z'],
        ['r', 'x', 'n', 'o', 's'],
        ['y', 'r', 'x', 'z', 'q', 't', 'p'],
        ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']
    ]

    return data


def create_init_set(data_set):
    re_dict = {}
    for trans in data_set:
        key = frozenset(trans)
        if key in re_dict.keys():
            re_dict[key] += 1
        else:
            re_dict[key] = 1
    return re_dict
