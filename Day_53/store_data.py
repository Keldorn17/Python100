import pandas


class StoreData:

    def __init__(self, data: list[dict]):
        """
        Parameters:
        - Data list has to have dictionaries the has all these key-value pairs:
        {'Address': ..., 'Price': ..., 'Link': ...}
        """
        self.__data: list[dict] = data
        data_frame: pandas.DataFrame = pandas.DataFrame(self.__data)
        data_frame.to_csv("data.csv", index=False)  # header=False to remove header
