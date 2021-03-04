import pytest
import generate_list as gl

class TestGenerateList:
    
    def test_generate_list(self):
        assert gl.generate_list(2, 10) == [2, 4, 6, 8]
        assert gl.generate_list(1, 2) == []
        assert gl.generate_list(2, 3) == [2]

    def test_generate_list_negative_start(self):
        assert gl.generate_list(-2, 8) == [-2, 0, 2, 4, 6]

    def test_generate_list_odd_start(self):
        assert gl.generate_list(1, 8) == [2, 4, 6]

    def test_generate_list_exceptions(self):
        with pytest.raises(ValueError):
            gl.generate_list(7,7)

        with pytest.raises(ValueError):
            gl.generate_list(7, 5)

