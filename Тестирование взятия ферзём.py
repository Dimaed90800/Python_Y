import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(42)
    with pytest.raises(TypeError):
        is_under_queen_attack(['e2', 'b1'])


def test_wrong_value():
    with pytest.raises(ValueError):
        is_under_queen_attack('j5') in ['a1', 'a2', 'a3', 'a4', 'a5',
                                        'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 
                                        'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 
                                        'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 
                                        'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 
                                        'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 
                                        'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 
                                        'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 
                                        'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 
                                        'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 
                                        'h4', 'h5', 'h6', 'h7', 'h8']

            
def position():
    assert is_under_queen_attack('b5') == 'b5'
    assert is_under_queen_attack('b5') == 'b1'
    assert is_under_queen_attack('b5') == 'b2'
    assert is_under_queen_attack('b5') == 'b3'
    assert is_under_queen_attack('b5') == 'b4'
    assert is_under_queen_attack('b5') == 'b6'
    assert is_under_queen_attack('b5') == 'b7'
    assert is_under_queen_attack('b5') == 'b8'
    assert is_under_queen_attack('b5') == 'a5'
    assert is_under_queen_attack('b5') == 'c5'
    assert is_under_queen_attack('b5') == 'a5'
    assert is_under_queen_attack('b5') == 'a4'
    assert is_under_queen_attack('b5') == 'a6'
    assert is_under_queen_attack('b5') == 'c6'
    assert is_under_queen_attack('b5') == 'c4'
    