import pytest
import generate_list_hardcoded as hard_coded

class TestGenerateListHardCoded:

    def test_generate_list_version_1(self):
        assert hard_coded.generate_list_version_1() == [2, 4, 6, 8, 10]

    def test_generate_list_version_2(self):
        assert hard_coded.generate_list_version_2() == [2, 4, 6, 8, 10]

    def test_generate_list_version_3(self):
        assert hard_coded.generate_list_version_3() == [2, 4, 6, 8, 10]

    def test_generate_list_version_4(self):
        assert hard_coded.generate_list_version_4() == [2, 4, 6, 8, 10]

    def test_generate_list_harcode_end(self):
        assert hard_coded.generate_list_hardcode_end(2) == [2, 4, 6, 8, 10]
        assert hard_coded.generate_list_hardcode_end(-2) == [-2, 0, 2, 4, 6]
