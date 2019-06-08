from cubic_matrix.matrix import CubicMatrix
from cubic_matrix.actions import UpdateAction


class TestUpdateAction:

    def test_creates(self):
        cm = CubicMatrix(3, 3, 2)
        update = UpdateAction([1, 1, 1], cm.matrix)
        assert update._position == (1, 1, 1)
        assert update._update_value == 1
        assert update._matrix is cm.matrix

    def test_execute(self):
        cm = CubicMatrix(3, 3, 2)
        update = UpdateAction([1, 1, 1], cm.matrix)
        update.execute()
        assert cm.matrix.get((1, 1, 1)) == 1
