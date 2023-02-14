import unittest
from pyspark.sql import DataFrame, Row
from PySparkTest import PySparkTest
from dbdf_hello_world.HelloWorldFeatures import HelloWorldFeatures
from dbdf_hello_world.HelloWorldSchema import HelloWorldSchema


class TestHelloWorldFeatures(PySparkTest):
    """Hello World Feature Extraction Test"""

    def setUp(self):
        self.test_args = {
            'smell': 'stale',
            'weight': 10
        }
        self.test_df = self._make_test_df(self.test_args)

    def _make_test_df(self, args) -> DataFrame:
        """create test dataframe"""
        return self.spark.createDataFrame(Row(rec={**args}), schema=HelloWorldSchema)

    def test_smelly_and_heavy(self):
        rows = self.test_df.withColumn(
            "smelly_and_heavy", HelloWorldFeatures.smelly_and_heavy()
        ).collect()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].smelly_and_heavy, 1)

    def test_add_all_features(self):
        rows = HelloWorldFeatures.add_all_features(self.test_df).collect()

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].smelly_and_heavy, 1)

    def test_add_features(self):
        rows = HelloWorldFeatures.add_features(self.test_df, "smelly_and_heavy").collect()

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].smelly_and_heavy, 1)


if __name__ == "__main__":
    unittest.main()
