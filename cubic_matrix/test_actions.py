from cubic_matrix.matrix import CubicMatrix
from cubic_matrix.actions import UpdateAction, QueryAction


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


class TestQueryAction:

    def test_creates(self):
        cm = CubicMatrix(3, 3, 2)
        query = QueryAction([1, 1, 1, 3, 1, 2], cm.matrix)
        assert query._start_position == (1, 1, 1)
        assert query._end_position == (3, 1, 2)
        assert query._matrix is cm.matrix
