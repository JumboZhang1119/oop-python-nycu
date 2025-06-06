import add_path
import mit_ocw_exercises.lec11_complexity_part2 as lec11
import pytest

def test_bisect_search2():
    testList = [10, 20, 30, 40, 50, 60]
    assert lec11.bisect_search2(testList, 30) == True     
    assert lec11.bisect_search2(testList, 10) == True     
    assert lec11.bisect_search2(testList, 60) == True     
    assert lec11.bisect_search2(testList, 25) == False    
    assert lec11.bisect_search2(testList, 100) == False   
    assert lec11.bisect_search2([], 30) == False      

def test_genSubsets():
    testSet = [10, 20]
    subsets = lec11.genSubsets(testSet)
    assert subsets == [[], [10], [20], [10, 20]]