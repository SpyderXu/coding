def get_topk_in_two_nums(numsA, numsB, K):
    if len(numsA) > len(numsB):
        return get_topk_in_two_nums(numsB, numsA, K)
    elif len(numsA) == 0:
        return numsB[K-1]
    elif K == 1:
        return min(numsA[0], numsB[0])
    else:
        ia = min(len(numsA), K//2)
        ib = K - ia
        if numsA[ia-1] < numsB[ib-1]:
            return get_topk_in_two_nums(numsA[ia:], numsB, K-ia)
        elif numsA[ia-1] > numsB[ib-1]:
            return get_topk_in_two_nums(numsA, numsB[ib:], K-ib)
        else:
            return numsA[ia-1]