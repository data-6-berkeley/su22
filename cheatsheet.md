---
layout: page
title: Exam Cheat Sheet
tagline: Cheat sheet for quizzes and exams
nav_exclude: true
---

# Data 6 Python Cheat Sheet (Quiz 1)
_This cheat sheet has been modified from the Data 6 Python Reference and includes all of the functions and table methods that you will need for Quiz 1._

## Built-In Python Functions
<div class="small_table">
| **Function** | **Description** | **Input** | **Output** |
| `str(val)` | Converts `val` to a string | A value of any type (**int**, **float**, **NoneType**, etc.) | The value as a **string** |
| `int(num)` | Converts `num` to an int | A numerical value (represented as a **string** or **float**) | The value as an **int** |
| `float(num)` | Converts `num` to a float | A numerical value (represented as a **string** or **int**) | The value as a **float** |
| `len(arr)` | Returns the length of `arr` | **array** or **list** | **int**: the length of the array or list |
| `max(arr)` | Returns the maximum value in `arr` | **array** or **list** | The maximum value the array (usually an **int**) |
| `min(arr)` | Returns the minimum value in `arr` | **array** or **list** | The minimum value the array (usually an **int**) |
| `sum(arr)` | Returns the sum of the values in `arr` | **array** or **list** | **int** or **float**: the sum of the values in the array |
| `abs(num)` | Returns the absolute value of `num` | **int** or **float** | **int** or **float** |
</div>

## NumPy Array Functions

| **Function** | **Description** | **Input** | **Output** |
| `make_array(val1, val2, ...)` | Makes a NumPy array with the inputted values | A sequence of values | An **array** with those values |
| `np.mean(arr)` or `np.average(arr)` | Calculates the average value of `arr` | An **array** of numbers | **float**: The average of the array |
| `np.sum(arr)` | Returns the sum of the values in `arr` | **array** | **int** or **float**: the sum of the values in the array |
| `np.arange(stop)`, `np.arange(start, stop)`, or `np.arange(start, stop, step)` | Creates an array of sequential numbers starting at `start`, going up in increments of `step`, and going up to but excluding `stop`. Default `start` is 0, default `step` is 1 | **int** or **float** | **array** |

## Tables and Table Methods

| **Function** | **Description** | **Input** | **Output** |
| `Table()` | Creates an empty table, usually to extend with data | None | An empty **Table** |
| `tbl.with_column(name, values)` or `tbl.with_columns(n1, v1, n2, v2, ...)` | Adds an extra column onto `tbl` with the label `name` and `values` as the column values | 1. **string**: name of the new column <br> 2. **array**: values in the column | **Table**: a copy of the original table with the new column(s) |
| `tbl.column(col)` | Returns the values in a column  | **string** or **int**: the column name or index | **array**: the values in that column |
| `tbl.num_rows` | Compute the number of rows in `tbl` | None | **int**: the number of rows in the table |
| `tbl.num_columns` | Compute the number of columns in `tbl` | None | **int**: the number of columns in the table |
| `tbl.labels` | Returns the labels in `tbl` | None | **array**: the names of each column as strings |
| `tbl.select(col1, col2, ...)` | Creates a copy of `tbl` only with the selected columns | **string** or **int**: the column name(s) or index(es) to be included in the table | **Table** with the selected columns |
| `tbl.drop(col1, col2, ...)` | Creates a copy of `tbl` without the selected columns | **string** or **int**: the column name(s) or index(es) to be dropped from the table | **Table** without the selected columns |
| `tbl.relabeled(old_label, new_label)` | Creates a new table, changing the column name specified by `old_label` to `new_label`, and leaves the original table unchanged. | 1. **string**: the old column name <br> 2. **string** the new column name | **Table**: a copy of the original table with the changed column name |
| `tbl.show(n)` | Displays the first `n` rows of `tbl`. If no argument is specified, the function defaults to showing the entire table | (Optional) **int**: number of rows to be displayed | None (table is displayed) |
| `tbl.sort(column_name)` | Sorts the rows of `tbl` by the values in the `column_name` column. Defaults to ascending order unless the optional argument `descending=True` is included. | 1. **string** or **int**: name or index of the column to sort <br> 2. (Optional) `descending=True` | **Table**: a copy of the original table with the column sorted |
| `tbl.where(column, predicate)` | Creates a copy of `tbl` containing only the rows where the value of `column` matches the `predicate`. See `Table.where` predicates below. | 1. **string** or **int**: column name or index <br> 2. `are.(...)` predicate | **Table**: a copy of the original table with only the rows that match the predicate |
| `tbl.take(row_indices)` | Creates a table with only the rows at the given indices. `row_indices` is either an array of indices or an integer corresponding to one index. | **int** or **array**: indices of rows to be included in the table | **Table**: a copy of the original table with only the rows at the given indices |


## Visualization Functions

| **Function** | **Description** | **Input** | **Output** |
| `tbl.barh(categories)` or `tbl.barh(categories, values)` | Displays a horizontal bar chart with bars for each category in the column `categories`. `values` specifies the column corresponding to the size of each bar, but is unnecessary if the table only has two columns | 1. **string**: name of the column with categories <br> 2. (Optional) **string**: name of the column with values corresponding to the categories | None: draws a bar chart |
| `tbl.hist(column)` | Generates a histogram of the numerical values in `column`. | **string**: name of the column | None: draws a histogram |
| `tbl.plot(x_column, y_column)` or `tbl.plot(x_column)` | Draws a line plot consisting of one point for each row in `tbl`. If only `x_column` is specified, `plot` will plot the rest of the columns on the y-axis with different colored lines. | 1. **string**: name of the column on the x-axis <br> 2. **string**: name of the column on the y-axis | None: draws a line graph |
| `tbl.scatter(x_column, y_column)` | Draws a scatter plot consisting of one point for each row in `tbl`. The optional argument `fit_line=True` can be included to draw a line of best fit through the scatter plot. | 1. **string**: name of the column on the x-axis <br> 2. **string**: name of the column on the y-axis <br> 3. (Optional) `fit_line=True` | None: draws a scatter plot |
