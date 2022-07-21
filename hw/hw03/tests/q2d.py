test = {   'name': 'q2d',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(top_5_acc, np.ndarray)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> isinstance(bottom_5_acc, np.ndarray)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(sorted(top_5_acc) == sorted(np.array(['ROSELAND COLLEGIATE PREP', 'GRANGE SCHOOL THE', 'FELICITAS GONZALO MENDEZ HS', 'ALLIANCE M&E STERN "
                                               "MATH SCI SCH', 'SOUTH HIGH SCHOOL'])))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(sorted(bottom_5_acc) == sorted(np.array(['NANJING FOREIGN LANGUAGE SCH', 'BEIJING NATIONAL DAY SCHOOL', 'HIGH SCH @RENMIN UNIV OF CHINA', "
                                               "'SKYLINE HIGH SCHOOL', 'SHANGHAI FOREIGN LANGUAGE SCHL'])))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
