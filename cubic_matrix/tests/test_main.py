from cubic_matrix.matrix import CubicMatrix


class TestMain:

    # SUCCESS
    def test_execute_update_action(self):
        cm = CubicMatrix(3, 3, 4)
        assert cm.execute('UPDATE 1 1 1 10') == 'SUCCESS'
        assert cm.execute('UPDATE 2 2 2 10') == 'SUCCESS'
        assert cm.execute('UPDATE 3 3 4 10') == 'SUCCESS'
        assert cm.matrix.get((1, 1, 1)) == 10
        assert cm.matrix.get((2, 2, 2)) == 10
        assert cm.matrix.get((3, 3, 4)) == 10
        assert sum(pos[1] for pos in cm.matrix.items() if pos[0] not in ((1, 1, 1), (2, 2, 2), (3, 3, 4))) == 0

    def test_execute_query_action(self):
        cm = CubicMatrix(3, 3, 4)
        assert cm.execute('QUERY 1 1 1 3 3 1') == 'SUCCESS 0'
        cm.execute('UPDATE 1 1 1 10')
        assert cm.execute('QUERY 1 1 1 3 3 1') == 'SUCCESS 10'
        cm.execute('UPDATE 3 3 3 10')
        assert cm.execute('QUERY 1 1 1 3 3 3') == 'SUCCESS 20'
        cm.execute('UPDATE 1 2 1 1')
        assert cm.execute('QUERY 1 1 1 1 2 1') == 'SUCCESS 11'
        assert cm.execute('QUERY 1 1 1 3 3 3') == 'SUCCESS 21'
        cm.execute('UPDATE 1 2 1 -1')
        assert cm.execute('QUERY 1 1 1 3 3 3') == 'SUCCESS 19'

    # ERROR
    def test_non_integer_arguments_error(self):
        cm = CubicMatrix(3, 3, 4)
        assert cm.execute('UPDATE 1 1 X 10') == 'ERROR Argument "X" is not valid, must be an integer.'
        assert cm.execute('UPDATE 1 1 1 X') == 'ERROR Argument "X" is not valid, must be an integer.'
        assert cm.execute('QUERY 1 1 1 2 2 2 0.1') == 'ERROR Argument "0.1" is not valid, must be an integer.'

    def test_invalid_action_error(self):
        cm = CubicMatrix(3, 3, 4)
        assert cm.execute('UPDAT 1 1 1 10') == 'ERROR Action "UPDAT" is not valid. Options are UPDATE and QUERY.'
        assert cm.execute('Q 1 1 1 1 2 2') == 'ERROR Action "Q" is not valid. Options are UPDATE and QUERY.'
        assert cm.execute('1 1 1 1 2 2') == 'ERROR Action "1" is not valid. Options are UPDATE and QUERY.'

    def test_coordinate_out_of_range(self):
        cm = CubicMatrix(3, 3, 4)
        assert cm.execute('UPDATE 4 4 4 10') == 'ERROR Coordinates are out of matrix range.'
        assert cm.execute('QUERY 1 1 1 3 3 5') == 'ERROR Coordinates are out of matrix range.'
        assert cm.execute('QUERY -1 1 1 3 3 4') == 'ERROR Coordinates are out of matrix range.'
