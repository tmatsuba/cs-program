from stringsearch.kmp import kmp, create_pattern_table

def test_kmp():
    w = 'tested'
    assert kmp('testehogehogtestedh', w, create_pattern_table(w)) == 12

