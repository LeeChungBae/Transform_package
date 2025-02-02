# transform.py

import requests
import os
import pandas as pd

# 행 추출
def col_drop(load_dt, path):
    df = pd.read_parquet(f"{path}/load_dt={load_dt}")

    # drop columns -> implement
    cols = ['rnum','rankOldAndNew','movieCd'] 
    df = df.drop(columns = cols, axis = 1)
    return df

# 문자열 > 숫자
def str_to_num(df, path, load_dt):
    print("df at flag:", df.head(5))
    num_cols = ['rank',                     # 순위
                'salesAmt', 'salesAcc',     # 일일 & 누적 매출액
                'salesShare',               # 전체 영화 매출액 중 파이 비율
                'audiCnt', 'audiAcc',       # 일일 & 누적 관객수
                'scrnCnt', 'showCnt',       # 일일 & 누적 상영수
                'audiInten', 'audiChange',  # 관객수 변화 절대값 & 비율
     ]

    for col in num_cols:
#        print("col:", col)
        df[col] = pd.to_numeric(df[col])
        
#    print("path:", path)
#    print("df at flag2:", df.head(5))
 
    df['load_dt'] = load_dt   
    df.to_parquet(path, partition_cols=['load_dt'])
    return df
