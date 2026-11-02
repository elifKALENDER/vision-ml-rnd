from numpy.ma.core import append

from exercises import (temperature_comparison)

def test_temperature_comparison():
    test_list=[69,70,71,84,85,86]
    result = []
    for t in test_list:
        result.append(temperature_comparison(t))

    assert result== ["Normal","Warning","Warning","Warning","Warning","Critical"]
