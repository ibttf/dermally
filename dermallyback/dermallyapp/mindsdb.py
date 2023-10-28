import pandas as pd
from mindsdb import Predictor
from django.db import connections

def train_mindsdb():
    # Fetch data directly from CockroachDB into a DataFrame
    with connections['default'].cursor() as cursor:
        cursor.execute('SELECT image, condition FROM skincare_app_skincareimage')
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=['image', 'condition'])
    
    # Train the MindsDB model
    Predictor(name='skincare_predictor').learn(from_data=df, to_predict='condition')


train_mindsdb()