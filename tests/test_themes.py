from great_tables import GT, exibble

from GTextras.themes import gt_theme_538


def test_gt_theme_538_no_error():

    tbl = gt_theme_538(GT(exibble, id="test"))
    assert isinstance(tbl, GT)
