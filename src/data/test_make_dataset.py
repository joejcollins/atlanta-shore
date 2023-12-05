
""" Tests for windows_servers_by_pod.py """
import datetime

import make_dataset


def test_date_from_file():
    """ Confirm correct date is returned """
    returned_date = make_dataset.date_from_file("./data/raw/2019-06/data-plant-2019-06-20-MEC.csv")
    expected_date = datetime.date(2019, 6, 20)
    assert returned_date == expected_date
