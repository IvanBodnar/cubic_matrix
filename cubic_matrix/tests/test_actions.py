from cubic_matrix.matrix import CubicMatrix
from cubic_matrix.actions import UpdateAction, QueryAction


class TestUpdateAction:

    def test_creates(self):
        cm = CubicMatrix(3, 3, 2)
        update = UpdateAction([1, 1, 1, 1], cm.matrix)
        assert update._position == (1, 1, 1)
        assert update._update_value == 1
        assert update._matrix is cm.matrix

    def test_execute(self):
        cm = CubicMatrix(3, 3, 2)
        update = UpdateAction([1, 1, 1, 1], cm.matrix)
        update.execute()
        assert cm.matrix.get((1, 1, 1)) == 1


class TestQueryAction:

    def test_creates(self):
        cm = CubicMatrix(3, 3, 2)
        query = QueryAction([1, 1, 1, 3, 1, 2], cm.matrix)
        assert query._start_position == (1, 1, 1)
        assert query._end_position == (3, 1, 2)
        assert query._matrix is cm.matrix

    def test_get_enumerated_items(self):
        cm = CubicMatrix(3, 3, 3)
        query = QueryAction([1, 1, 1, 3, 1, 2], cm.matrix)
        ei = query._get_enumerated_items()
        assert list(item[0] for item in ei) == list(range(1, 28))
        assert ei[-1][1][0] == (3, 3, 3)

    def test_get_index(self):
        cm = CubicMatrix(3, 3, 3)
        query = QueryAction([1, 1, 1, 3, 1, 2], cm.matrix)
        assert query._get_index((1, 1, 1)) == 1
        assert query._get_index((3, 3, 3)) == 27

    def test_execute(self):
        cm = CubicMatrix(3, 3, 3)
        update = UpdateAction([1, 1, 1, 1], cm.matrix)
        update.execute()
        update = UpdateAction([3, 3, 3, 1], cm.matrix)
        update.execute()
        query = QueryAction([1, 1, 1, 3, 3, 3], cm.matrix)
        assert query.execute() == 2
