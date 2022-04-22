from sort.bubblesort import bubble_sort
from sort.selectionsort import selection_sort
from sort.insertsort import insert_sort
from sort.quicksort import quick_sort
from sort.mergesort import merge_sort

def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([1, 3, 2, 4, 7, 6, 8, 5]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_selection_sort():
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([1, 3, 2, 4, 7, 6, 8, 5]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_insert_sort():
    assert insert_sort([]) == []
    assert insert_sort([1]) == [1]
    assert insert_sort([1, 3, 2, 4, 7, 6, 8, 5]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_quick_sort():
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([1, 3, 2, 4, 7, 6, 8, 5]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_merge_sort():
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([1, 3, 2, 4, 7, 6, 8, 5]) == [1, 2, 3, 4, 5, 6, 7, 8]
