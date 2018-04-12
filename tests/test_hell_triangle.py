from ..modules.triangle import HellTriangle

hell_triangle = HellTriangle()


def test_triangle26():
    result = hell_triangle.summed_triangle(
        [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]], test=True)
    assert result == 26
