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
| `np.arange(stop)`, `np.arange(start, stop)`, `np.arange(start, stop, step)` | Creates an array of sequential numbers starting at `start`, going up in increments of `step`, and going up to but excluding `stop`. Default `start` is 0, default `step` is 1 | **Int** or **Float** | **Array** |

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

## More Documentation

The Data 6 Python reference guide is based on the Data 8 [Python Reference](http://data8.org/sp22/python-reference.html). 
