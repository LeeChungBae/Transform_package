# transform.py

import requests
import os
import pandas as pd

# 행 추출
def col_drop(load_dt, path):
    df = pd.read_parquet(f"{path}/load_dt={load_dt}")
    print(type(df))
    # drop columns -> implement
    cols = ['rnum','rankOldAndNew','movieCd']
    print(type(df))
    df = df.drop(axis=1,columns=cols)   
    return df

# 문자열 > 숫자
def str_to_num(df, path):
    # columns to sum
    print(type(df))
    num_cols = ['rank',                     # 순위
                'salesAmt', 'salesAcc',     # 일일 & 누적 매출액
                'salesShare',               # 전체 영화 매출액 중 파이 비율
                'audiCnt', 'audiAcc',       # 일일 & 누적 관객수
                'scrnCnt', 'showCnt',       # 일일 & 누적 상영수
                'audiInten', 'audiChange',  # 관객수 변화 절대값 & 비율
     ]
    for col in num_cols:
        print(df[col], type(df[col]))
        df[col] = pd.to_numeric(df[col])

    df.to_parquet(path, partition_cols=['load_dt'])
    return df
