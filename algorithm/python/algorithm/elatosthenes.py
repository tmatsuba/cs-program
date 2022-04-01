def elatosthenes(limit: int):
    # 0, 1 は素数ではない
    if limit < 2:
        return []

    # 2と奇数のリストを作る
    ret = [2] + [i for i in range (3, limit + 1,  2)]
    for number in range (3, limit + 1,  2):
        for sieve in range (number**2, limit + 1, number):
            ret = list(filter(lambda x: (x % sieve != 0), ret))
    return ret

if __name__ == "__main__":
    print(elatosthenes(53))
