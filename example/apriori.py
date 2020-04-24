"""
    实现Apriori算法
"""


def create_c1(dataset):
    c1 = set()
    for transaction in dataset:
        for item in transaction:
            c1.add(item)
    c1 = list(c1)
    c1.sort()
    return map(lambda x: frozenset([x]), c1)  # 将c1中每个元素放入固定集合,作key使


def scanD(D, Ck, min_support):
    """
    计算所有项的支持度
    :param D: 数据集
    :param Ck: 候选项集列表 Ck的每个元素大小为k
    :param min_support: 最小支持度
    :return: re_list: 满足最小支持度的元素
             support_data: 最频繁项集的支持度
    """
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):  # 判断can集合是否包含tid集合
                if not "can" in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1  # 增加计数值
    re_list = []
    support_data = {}  # 支持度(出现比例)
    for key in ssCnt:
        support = ssCnt[key] / float(len(D))  # 计算支持度
        if support >= min_support:
            re_list.insert(0, key)  # 阈值过滤 在列表首部插入满足最小支持度的元素
        support_data[key] = support
    return re_list, support_data


def aprioriGen(lk, k):
    re_list = []
    len_lk = len(lk)
    for i in range(len_lk):
        for j in range(i + 1, len_lk):
            L1 = list(lk[i])[:k - 2]
            L2 = list(lk[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:  # 如果它们前k-2项相同
                re_list.append(lk[i] | lk[j])  # 合并
    return re_list


def apriori(dataSet, minSupport=0.5):
    c1 = create_c1(dataSet)
    D = map(set, dataSet)
    l1, support_data = scanD(D, c1, minSupport)
    L = [l1]
    k = 2
    while len(L[k - 2]) > 0:
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minSupport)  # 扫描并过滤
        support_data.update(supK)
        L.append(Lk)
        k += 1
    return L, support_data
