import calculation

def test_add_num_and_double():
    cal = calculation.Cal()
    assert cal.add_num_and_double(1, 1) != 4

# pytest section14/166.py で実行
