from pytest import approx

import hypot

def test_integration():
    '''Test for the example function'''

    # Arrange
    test_opp = 7
    test_adj = 5
    expected_hypot = 8.60233

    # Act
    output = hypot.calc.pythag(test_opp, test_adj)
    print(output)

    # Assert
    assert output == approx(expected_hypot, 0.1)

    # No cleanup needed
    
    