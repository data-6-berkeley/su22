test = {   'name': 'q1',
    'points': 0,
    'suites': [   {   'cases': [   {'code': '>>> group_label == "Quality"\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> function in [np.mean, np.average]\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> new_column_label in ["Worldwide Gross (Millions) mean", "Worldwide Gross (Millions) average"]\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> money_by_quality.num_rows == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> money_by_quality.num_columns == 2\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.all(np.round(money_by_quality.column("Worldwide Gross (Millions) average"), 2) == np.array([166.13, 196.95, 69.93]))\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
