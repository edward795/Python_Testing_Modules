import pytest 

def test_using_raises():
    with pytest.raises(TypeError):
        2+'3'==5