from .matrix import CubicMatrix, Position


class TestCubicMatrix:

    def test_creates(self):
        cm = CubicMatrix(3, 3, 2)
        assert len(cm.matrix) == 18
        assert cm.matrix.get((1, 1, 1)) == 0
        assert cm.matrix.get((3, 3, 2)) == 0
