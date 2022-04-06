def create_pattern_table(w):
    """ 照合テーブルを作成する
        与えられた文字の先頭部分の文字列と何文字合致しているかを配列で返す
    """
    t = [-1]

    for j in range(1, len(w)):
        k = j - 1
        while w[0:k ] != w[j-k:j] and k > 0:
            k = k -1
        t.append(k)
    return t

def kmp(s, w, t):
    """ 文字列を先頭から照合して行き、
        合致しなかった場合は照合テーブルに指定された数だけずらして照合を継続する。
    """
    print(t)
    i, j = 0, 0
    while i + j < len(s):
        if w[j] == s[i + j]:
            j = j + 1
            if j == len(w):
                return i
        else:
            i = i + j - t[j]
            if j > 0:
                j = t[j]

if __name__ == "__main__":
    w = 'tested'
    s = 'testehogehogtestedh'
    print(kmp(s, w, create_pattern_table(w)))
