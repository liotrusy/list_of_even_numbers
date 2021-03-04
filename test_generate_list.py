import pytest
import generate_list

def test_generate_list_version_1():
    assert generate_list.generate_list_version_1() == [2, 4, 6, 8, 10]
