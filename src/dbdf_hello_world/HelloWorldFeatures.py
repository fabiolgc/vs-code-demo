"""Central App Service Feature Extraction"""

from pyspark.sql.functions import expr
from pyspark.sql import Column


class HelloWorldFeatures:
    """Hello World Feature Extractor"""

    @staticmethod
    def smelly_and_heavy() -> Column:
        return expr("IF(smell = 'stale' AND weight >= 10, true, false)")

    @staticmethod
    def add_all_features(df):
        return (
            df.withColumn("smelly_and_heavy", HelloWorldFeatures.smelly_and_heavy())
        )

    @staticmethod
    def add_features(df, *features):
        for feature in features:
            df = df.withColumn(feature, getattr(HelloWorldFeatures, feature)())
        return df
