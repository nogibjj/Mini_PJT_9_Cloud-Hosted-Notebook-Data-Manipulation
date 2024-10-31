import pandas as pd
from mylib.lib import explore_data, calculate_age_statistics, print_age_statistics
from io import StringIO

# Dummy CSV data for testing
TEST_CSV_DATA = """
Age,Attrition,Department
29,Yes,Sales
34,No,Research & Development
28,Yes,Sales
45,No,Human Resources
38,Yes,Sales
30,No,Research & Development
"""


def test_load_data():
    # Load the test data using StringIO
    test_data = StringIO(TEST_CSV_DATA)
    df = pd.read_csv(test_data)
    assert len(df) > 0, "Data length should be greater than 0"
    assert "Age" in df.columns, "'Age' column should be in the DataFrame"


def test_explore_data():
    test_data = StringIO(TEST_CSV_DATA)
    df = pd.read_csv(test_data)
    description = explore_data(df)
    assert "Age" in description.index, "'Age' should be in the description index"


def test_calculate_age_statistics():
    test_data = StringIO(TEST_CSV_DATA)
    df = pd.read_csv(test_data)
    age_mean, age_median, age_std = calculate_age_statistics(df)
    assert isinstance(age_mean, float), "Mean age should be a float"
    assert isinstance(age_median, float), "Median age should be a float"
    assert isinstance(age_std, float), "Standard deviation should be a float"


def test_print_age_statistics():
    test_data = StringIO(TEST_CSV_DATA)
    df = pd.read_csv(test_data)
    age_mean, age_median, age_std = calculate_age_statistics(df)
    # Simplified verification - just ensuring no errors in printing
    print_age_statistics(age_mean, age_median, age_std)


def run_lib_tests():
    test_load_data()
    test_explore_data()
    test_calculate_age_statistics()
    test_print_age_statistics()
    print("All lib.py tests passed!")


if __name__ == "__main__":
    run_lib_tests()
