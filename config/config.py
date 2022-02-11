import os

class Config(object):

    # Common Configuration Elements

    RETRY_LIMIT=5
    APP_DB='postgres'
    APP_PASSWORD='teset'
    LIST_VALS = [
                ['NO1',1,'Line1'],
                ['NO2',2,'Line2'],
                ['NO3',3,'Line3']
                ],
    TABLE_COLUMNS=['No','Name','Address','City']


app_config=Config
