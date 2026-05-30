import numpy as np
import pandas as pd

TARGET = "count"

LEAKAGE_COLUMNS = ["casual", "registered"]

CATEGORICAL_COLUMNS = [
    "season",
    "holiday",
    "workingday",
    "weather"
]

NUMERICAL_COLUMNS = [
    "hour_sin",
    "hour_cos",
    "weekday_sin",
    "weekday_cos",
    "month",
    "year",
    "temp",
    "atemp",
    "windspeed",
    "humidity"
]

FEATURE_COLUMNS = CATEGORICAL_COLUMNS + NUMERICAL_COLUMNS

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    df["hour"] = df["datetime"].dt.hour
    df["weekday"] = df["datetime"].dt.weekday
    df["month"] = df["datetime"].dt.month
    df["year"] = df["datetime"].dt.year
    
    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)
    
    df["weekday_sin"] = np.sin(2 * np.pi * df["weekday"] / 7)
    df["weekday_cos"] = np.cos(2 * np.pi * df["weekday"] / 7)
    
    if TARGET in df:
        df[TARGET] = df.pop(TARGET)
    
    return df

def time_based_sort(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values(by="datetime")
    
    return df

def preprocess_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    df = create_features(df)
    df = time_based_sort(df)
    
    columns_to_drop = LEAKAGE_COLUMNS + ["datetime", "hour", "weekday"]
    columns_to_drop = [col for col in columns_to_drop if col in df]
    
    df  = df.drop(columns=columns_to_drop)
    
    return df