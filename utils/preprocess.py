import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from flask import Response


def preprocess(df=None, training=False):
    if training:
        df = pd.read_csv('/app/model/hotel_bookings.csv')

    to_drop = ['days_in_waiting_list', 'arrival_date_year','assigned_room_type',
               'booking_changes', 'reservation_status', 'country', 'arrival_date_month'
                ]

    df.drop(to_drop, axis=1, inplace=True)

    cat_cols = [col for col in df.columns if df[col].dtype == 'O']
    cat_df = df[cat_cols].copy()

    cat_df['reservation_status_date'] = pd.to_datetime(cat_df['reservation_status_date'])
    cat_df['year'] = cat_df['reservation_status_date'].dt.year
    cat_df['month'] = cat_df['reservation_status_date'].dt.month
    cat_df['day'] = cat_df['reservation_status_date'].dt.day
    cat_df['hotel'] = cat_df['hotel'].map({'Resort Hotel' : 0, 'City Hotel' : 1})
    cat_df['meal'] = cat_df['meal'].map({'BB' : 0, 'FB': 1, 'HB': 2, 'SC': 3, 'Undefined': 4})
    cat_df['market_segment'] = cat_df['market_segment'].map({'Direct': 0, 'Corporate': 1, 'Online TA': 2, 'Offline TA/TO': 3,
                                                            'Complementary': 4, 'Groups': 5, 'Undefined': 6, 'Aviation': 7})
    cat_df['distribution_channel'] = cat_df['distribution_channel'].map({'Direct': 0, 'Corporate': 1, 'TA/TO': 2, 'Undefined': 3,
                                                                        'GDS': 4})
    cat_df['reserved_room_type'] = cat_df['reserved_room_type'].map({'C': 0, 'A': 1, 'D': 2, 'E': 3, 'G': 4, 'F': 5, 'H': 6,
                                                                    'L': 7, 'B': 8})
    cat_df['deposit_type'] = cat_df['deposit_type'].map({'No Deposit': 0, 'Refundable': 1, 'Non Refund': 3})
    cat_df['customer_type'] = cat_df['customer_type'].map({'Transient': 0, 'Contract': 1, 'Transient-Party': 2, 'Group': 3})

    if (((cat_df['year'] < 2014).any()) or ((cat_df['year'] > 2017).any())):
        raise Exception
    cat_df['year'] = cat_df['year'].map({2015: 0, 2014: 1, 2016: 2, 2017: 3})

    cat_df.drop(['reservation_status_date'] , axis = 1, inplace = True)

    num_df = df.drop(columns = cat_cols, axis = 1)

    num_df.drop('is_canceled', axis = 1, inplace = True)

    num_df['lead_time'] = np.log(num_df['lead_time'] + 1)
    num_df['arrival_date_week_number'] = np.log(num_df['arrival_date_week_number'] + 1)
    num_df['arrival_date_day_of_month'] = np.log(num_df['arrival_date_day_of_month'] + 1)
    num_df['agent'] = np.log(num_df['agent'] + 1)
    num_df['company'] = np.log(num_df['company'] + 1)
    num_df['adr'] = np.log(num_df['adr'] + 1)
    num_df['adr'] = num_df['adr'].fillna(value = num_df['adr'].mean())

    X = pd.concat([cat_df, num_df], axis = 1)

    if training:
        y = df['is_canceled']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)
        return (X_train, X_test, y_train, y_test)

    return X