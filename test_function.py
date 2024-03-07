
import pytest
import function


class TestApp:
    def test_my_function(self):
        res = function.my_function(4)
        assert res == 6
