import unittest
import main
import pandas as pd


class TestMain(unittest.TestCase):

    def test_change_time(self):
        self.assertEqual(main.change_time("2019-01-09T11:00:00Z"), 1547024400)
        self.assertEqual(main.change_time("2019-01-09T11:30:00Z"), 1547026200)

    def test_get_median(self):
        result = main.get_median(12, 1547026200, 1547028000)
        self.assertEqual(result, 25)

    # Change the name of index everytime test so that it can pass
    def test_add_data(self):
        main.add_data("test-add-data-new-test-1", 27)
        hdf = pd.HDFStore("hdf5_data.h5", mode="r")
        data = hdf.get("/request")
        added_data = data.loc["test-add-data-new-test-1", 'result']
        hdf.close()
        self.assertEqual(int(added_data), 27)

    def test_get_data(self):
        self.assertEqual(main.get_data("12-1547024400-1547028000"), 27)
        self.assertEqual(main.get_data("12-1547024400-1547029000"), None)


if __name__ == '__main__':
    unittest.main()