import pytest



def test_equal_or_not_equal():
    list = [1,2,3,4,5]
    any_list = [False,False]

    assert 1 in list
    assert 7 not in list
    assert all(list)
    assert not any (any_list)


