# src/fe_application.py
import pandas as pd

def FE_application_data(data: pd.DataFrame) -> pd.DataFrame:
    df = data.copy()

    df['CREDIT_INCOME_PERCENT'] = df['AMT_CREDIT'] / df['AMT_INCOME_TOTAL']
    df['ANNUITY_INCOME_PERCENT'] = df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL']
    df['CREDIT_ANNUITY_PERCENT'] = df['AMT_CREDIT'] / df['AMT_ANNUITY']
    df['FAMILY_CNT_INCOME_PERCENT'] = df['AMT_INCOME_TOTAL'] / df['CNT_FAM_MEMBERS']
    df['CREDIT_TERM'] = df['AMT_ANNUITY'] / df['AMT_CREDIT']
    df['BIRTH_EMPLOYED_PERCENT'] = df['DAYS_EMPLOYED'] / df['DAYS_BIRTH']
    df['CHILDREN_CNT_INCOME_PERCENT'] = df['AMT_INCOME_TOTAL'] / df['CNT_CHILDREN'].replace(0, 1)
    df['CREDIT_GOODS_DIFF'] = df['AMT_CREDIT'] - df['AMT_GOODS_PRICE']
    df['EMPLOYED_REGISTRATION_PERCENT'] = df['DAYS_EMPLOYED'] / df['DAYS_REGISTRATION']

    return df