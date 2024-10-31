# test_main.py
from mylib.lib import (
    load_data,
    explore_data,
    calculate_age_statistics,
    print_age_statistics,
)


def test_main_execution():
    # Load data
    file_path = "https://raw.githubusercontent.com/nogibjj/Mini_PJT_9_Cloud-Hosted-Notebook-Data-Manipulation/refs/heads/main/file/HR.csv"
    df = load_data(file_path)
    assert df is not None, "Data should be loaded successfully"

    # Explore data
    description = explore_data(df)
    assert "Age" in description.index, "'Age' should be in the description index"

    # Calculate age statistics
    age_mean, age_median, age_std = calculate_age_statistics(df)
    assert age_mean > 0, "Mean age should be a positive number"
    assert age_median > 0, "Median age should be a positive number"
    assert age_std > 0, "Standard deviation should be a positive number"

    # Print age statistics (we won't assert print, but we ensure no errors)
    print_age_statistics(age_mean, age_median, age_std)

    print("All main.py tests passed!")


if __name__ == "__main__":
    test_main_execution()
