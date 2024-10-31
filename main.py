# main.py
from mylib.lib import (
    load_data,
    explore_data,
    calculate_age_statistics,
    plot_age_histogram,
    print_age_statistics,
    plot_attrition_pie_chart,
    plot_attrition_by_department,
)

if __name__ == "__main__":

    file_path = "https://raw.githubusercontent.com/nogibjj/Mini_PJT_9_Cloud-Hosted-Notebook-Data-Manipulation/refs/heads/main/file/HR.csv"
    ppl = load_data(file_path)

    explore_data(ppl)

    age_mean, age_median, age_std = calculate_age_statistics(ppl)
    print_age_statistics(age_mean, age_median, age_std)

    plot_age_histogram(ppl)

    plot_attrition_pie_chart(ppl)

    plot_attrition_by_department(ppl, "Department")
