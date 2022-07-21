test = {   'name': 'q4b',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(varied_menu_only, Table)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> varied_menu_only.num_rows == 22\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.all(varied_menu_only.column(\'Restaurant\').take(np.arange(5)) == np.array(["O\'Charley\'s", "Cooper\'s Hawk Winery & Restaurants",\n'
                                               "...        'Ninety Nine Restaurants', 'Bar Louie', 'Seasons 52']))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
