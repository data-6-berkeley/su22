test = {   'name': 'q4',
    'points': 0,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(money_by_quality, Table)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> money_by_quality.num_rows == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> money_by_quality.labels == ('Quality', 'Worldwide Gross (Millions) mean')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(money_by_quality.column(1).item(2), 71.72821428571429)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
