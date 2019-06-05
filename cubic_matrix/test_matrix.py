from .matrix import CubicMatrix, Position


class TestCubicMatrix:

    def test_creates(self):
        cm = CubicMatrix(3, 3, 2)
        assert len([x for x in cm.matrix.values() if x == 0]) == 18
        assert cm.matrix.get((1, 1, 1)) == 0
        assert cm.matrix.get((3, 3, 2)) == 0

    def test_parse_command(self):
        cm = CubicMatrix(3, 3, 2)
        assert cm._parse_command('UPDATE 1 1 1 1') == 0

