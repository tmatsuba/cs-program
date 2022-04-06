from algorithm.bubblesort import bubble_sort
from algorithm.selectionsort import selection_sort

def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([1, 3, 2, 4, 7, 6, 8, 5]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_selection_sort():
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([1, 3, 2, 4, 7, 6, 8, 5]) == [1, 2, 3, 4, 5, 6, 7, 8]


