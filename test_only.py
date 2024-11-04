from getFileFromPresentation import only_one_word


def test_only_one_word():
    assert only_one_word('123fdsa') == False
    assert only_one_word(':') == False
    assert only_one_word(' ') == False # assert подразумевается
    assert only_one_word('Firtt Second') == False
    assert only_one_word('True') == True
    assert only_one_word('Vasiliy') == True

if __name__=='__main__':
    test_only_one_word()