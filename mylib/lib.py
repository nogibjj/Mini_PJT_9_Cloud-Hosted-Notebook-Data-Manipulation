import pandas as pd
import matplotlib.pyplot as plt

# Load dataset using Pandas
def load_data(file_path, encoding="utf-8"):
    return pd.read_csv(file_path, encoding=encoding)

# Explore data
def explore_data(df):
    full_desc = df.describe().T
    print(full_desc)
    return full_desc

# Calculate statistics for Age
def calculate_age_statistics(df):
    age_mean = df["Age"].mean()
    age_median = df["Age"].median()
    age_std = df["Age"].std()
    return age_mean, age_median, age_std

# Plot histogram for Age
def plot_age_histogram(df):
    plt.figure(figsize=(8, 6))
    plt.hist(df["Age"], bins=10, edgecolor="black")
    plt.title("Average age of employees")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

# Print age statistics
def print_age_statistics(age_mean, age_median, age_std):
    print(f"Average age of employees is {round(age_mean, 1)}")
    print(f"Median age of employees is {age_median}")
    print(f"Standard Deviation age of employees is {age_std}")

# Employee Attrition rate
def plot_attrition_pie_chart(df):
    attrition_counts = df["Attrition"].value_counts()
    plt.pie(
        attrition_counts,
        labels=attrition_counts.index,
        autopct="%1.1f%%",
        startangle=90,
    )
    plt.title("Employee Attrition")
    plt.show()

# Employee Attrition by department or other categories
def plot_attrition_by_department(df, col_name):
    temp_grp = df.groupby([col_name, "Attrition"]).size().unstack(fill_value=0)
    temp_grp.columns = ["Attrition_No", "Attrition_Yes"]
    temp_grp["Percentage Attrition"] = (
        temp_grp["Attrition_Yes"]
        / (temp_grp["Attrition_Yes"] + temp_grp["Attrition_No"])
    ) * 100
    print(temp_grp)

    temp_grp[["Attrition_No", "Attrition_Yes"]].plot(
        kind="bar",
        stacked=False,
    )
    plt.xlabel(col_name)
    plt.ylabel("Count")
    plt.title(f"Attrition by {col_name}")
    plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt


# # Load dataset using Pandas
# def load_data(file_path, encoding="utf-8"):
#     return pd.read_csv(file_path, encoding=encoding)


# # Explore data
# def explore_data(df):
#     full_desc = df.describe().T
#     print(full_desc)
#     return full_desc


# # Calculate statistics for Age
# def calculate_age_statistics(df):
#     age_mean = df["Age"].mean()
#     age_median = df["Age"].median()
#     age_std = df["Age"].std()
#     return age_mean, age_median, age_std


# # Plot histogram for Age
# def plot_age_histogram(df):
#     plt.figure(figsize=(8, 6))
#     plt.hist(df["Age"], bins=10, edgecolor="black")
#     plt.title("Average age of employees")
#     plt.xlabel("Age")
#     plt.ylabel("Frequency")
#     plt.show()


# # Print age statistics
# def print_age_statistics(age_mean, age_median, age_std):
#     print(f"Average age of employees is {round(age_mean, 1)}")
#     print(f"Median age of employees is {age_median}")
#     print(f"Standard Deviation age of employees is {age_std}")


# # Employee Attrition rate
# def plot_attrition_pie_chart(df):
#     attrition_counts = df["Attrition"].value_counts()
#     plt.pie(
#         attrition_counts,
#         labels=attrition_counts.index,
#         autopct="%1.1f%%",
#         startangle=90,
#     )
#     plt.title("Employee Attrition")
#     plt.show()


# # Employee Attrition by department or other categories
# def generate_frequency_graph(df, col_name):
#     temp_grp = df.groupby([col_name, "Attrition"]).size().unstack(fill_value=0)
#     temp_grp.columns = ["Attrition_No", "Attrition_Yes"]
#     temp_grp["Percentage Attrition"] = (
#         temp_grp["Attrition_Yes"]
#         / (temp_grp["Attrition_Yes"] + temp_grp["Attrition_No"])
#     ) * 100
#     print(temp_grp)

#     temp_grp[["Attrition_No", "Attrition_Yes"]].plot(
#         kind="bar",
#         stacked=False,
#     )
#     plt.xlabel(col_name)
#     plt.ylabel("Count")
#     plt.title(f"Attrition by {col_name}")
#     plt.show()


# # Main execution
# if __name__ == "__main__":
#     ppl = load_data("HR.csv")

#     # Explore the data
#     explore_data(ppl)

#     # Calculate and print statistics for Age
#     age_mean, age_median, age_std = calculate_age_statistics(ppl)
#     print_age_statistics(age_mean, age_median, age_std)

#     # Plot histogram for Age
#     plot_age_histogram(ppl)

#     # Plot Employee Attrition rate
#     plot_attrition_pie_chart(ppl)

#     # Plot Attrition by department
#     generate_frequency_graph(ppl, "Department")
