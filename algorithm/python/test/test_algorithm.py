from algorithm.elatosthenes import elatosthenes

def test_elatoshthenes():
    assert elatosthenes(-1) == []
    assert elatosthenes(2) == [2]
    assert elatosthenes(3) == [2, 3]
    assert elatosthenes(112) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]

