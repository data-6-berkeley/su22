---
layout: page
title: Python Reference
description: >-
    Python Reference Guide
---

# Python Reference &#x1F40D;
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Understanding the Python Reference

If you're new to reading documentation

## Built-In Python Functions

| **Function** | **Description** | **Input** | **Output** |
| `str(val)` | Converts `val` to a string | A value of any type (**int**, **float**, **NoneType**, etc.) | The value as a **string** |
| `int(num)` | Converts `num` to an int | A numerical value (represented as a **string** or **float**) | The value as an **int** |
| `float(num)` | Converts `num` to a float | A numerical value (represented as a **string** or **int**) | The value as a **float** |
| `len(arr)` | Returns the length of `arr` | **Array** or **list** | **Int**: the length of the array or list |
| `max(arr)` | Returns the maximum value in `arr` | **Array** or **list** | The maximum value the array (usually an **int**) |
| `min(arr)` | Returns the minimum value in `arr` | **Array** or **list** | The minimum value the array (usually an **int**) |
| `sum(arr)` | Returns the sum of the values in `arr` | **Array** or **list** | **Float** or **Int**: the sum of the values in the array |
| `abs(num)` | Returns the absolute value of `num` | **Int** or **Float** | **Int** or **Float** |

## NumPy Array Functions

| **Function** | **Description** | **Input** | **Output** |
| `np.mean(arr)` or `np.average(arr)` | Calculates the average value of `arr` | An **array** of numbers | **Float**: The average of the array |
| `np.arange(stop)`, `np.arange(start, stop)`, or `np.arange(start, stop, step)` | Creates an array of sequential numbers starting at `start`, going up in increments of `step`, and going up to but excluding `stop`. Default `start` is 0, default `step` is 1 | **Int** or **Float** | **Array** |

## Tables and Table Methods

| **Function** | **Description** | **Input** | **Output** |
| `Table()` | Creates an empty table, usually to extend with data | None | An empty **Table** |
| `tbl.with_column(name, values)` or `tbl.with_columns(n1, v1, n2, v2, ...)` | Adds an extra column onto `tbl` with the label `name` and `values` as the column values | 1. **String**: name of the new column <br> 2. **Array**: values in the column | **Table**: a copy of the original table with the new column(s) |
| `tbl.column(col)` | Returns the values in a column  | **String** or **Int**: the column name or index | **Array**: the values in that column |
| `tbl.num_rows` | Compute the number of rows in `tbl` | None | **Int**: the number of rows in the table |
| `tbl.num_columns` | Compute the number of columns in `tbl` | None | **Int**: the number of columns in the table |
| `tbl.labels` | Returns the labels in `tbl` | None | **Array**: the names of each column as strings |
| `tbl.select(col1, col2, ...)` | Creates a copy of `tbl` only with the selected columns | **String** or **Int**: the column name(s) or index(es) to be included in the table | **Table** with the selected columns |
| `tbl.drop(col1, col2, ...)` | Creates a copy of `tbl` without the selected columns | **String** or **Int**: the column name(s) or index(es) to be dropped from the table | **Table** without the selected columns |
| `tbl.show(n)` | Displays the first `n` rows of `tbl`. If no argument is specified, the function defaults to showing the entire table | (Optional) **Int**: number of rows to be displayed | None (table is displayed) |
| `tbl.sort(column_name)` | Sorts the rows of `tbl` by the values in the `column_name` column. Defaults to ascending order unless the optional argument `descending=True` is included. | 1. **String** or **Int**: name or index of the column to sort <br> 2. (Optional) `descending=True` | **Table**: a copy of the original table with the column sorted |
| `tbl.where(column, predicate)` | Creates a copy of `tbl` containing only the rows where the value of `column` matches the `predicate`. See `Table.where` predicates below. | 1. **String** or **Int**: column name or index <br> 2. `are.(...)` predicate | **Table**: a copy of the originaltable with only the rows that match the predicate |
| `tbl.apply(function)` or `tbl.apply(function, col1, col2, ...)` | Returns an **array** of values resulting from applying a function to each item in a column. | 1. **Function**: function to apply to column <br> 2. (Optional) **String** or **Int**: the column name(s) or index(es) to apply the function to | **Array** containing an element for each value in the original column after applying the function to it |
| `tbl.group(column_or_columns, function)` | Groups rows in `tbl` by unique values or combinations of values in a column(s). Multiple columns must be entered as an array of strings. Values in the other columns are aggregated by count (by default) or the optional argument `function`. You can visualize the `group` function [here](http://data8.org/interactive_table_functions/). | 1. **String** or **Array of Strings**: column(s) on which to group <br> 2. (Optional) **Function**: function to aggregate values in cells (defaults to counting rows) | **Table** a new groupped table |
| `tbl.pivot(col1, col2)` or `tbl.pivot(col1, col2, values, collect)` | Creates a pivot table where each unique value in `col1` has its own column and each unique value in `col2` has its own row. Counts or aggregates values from a third column, collected with some function. If the `values` and `collect` arguments are not included, `pivot` defaults to returning counts in the cells. You can visualize the `pivot` function [here](http://data8.org/interactive_table_functions/). | 1. **String**: name of the column in `tbl` whose unique values will make up the columns of the pivot table <br> 2. **String**: name of column in `tbl` whose unique values will make up the rows of the pivot table <br> 3. (Optional) **String**: name of the column in `tbl` that describes the values of cells in the pivot table <br> 4. (Optional) **Function**: how the values are collected (e.g. `sum` or `np.mean`) | **Table**: a new pivot table |
| `tblA.join(colA, tblB)` | Generate a table with the columns of `tblA` and `tblB`, containing rows for all values in `colA` and `colB` that appear in `tblA` and `tblB`, respectively. By default, `colB` is the same value as `colA`. `colA` and `colB` must be strings specifying column names. | 1. **String**: name of column in `tblA` with values to join on <br> 2. **Table**: the other table <br> 3. (Optional) **String**: the name of the shared column in `tblB`, if column names are different between the tables | **Table**: a new combined table |

## More Documentation

The Data 6 Python reference guide is based on the Data 8 [Python Reference](http://data8.org/sp22/python-reference.html). More detailed Python documentation is available [here](https://docs.python.org/3/).
