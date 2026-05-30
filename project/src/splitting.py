import pandas as pd

from src.preprocessing import FEATURE_COLUMNS, TARGET

def split_dataset(df: pd.DataFrame, test_size: float = 0.2):
    
    split_index = int(len(df) * (1 - test_size))
    
    train_df = df.iloc[:split_index]
    test_df = df.iloc[split_index:]
    
    X_train, X_test = train_df[FEATURE_COLUMNS], test_df[FEATURE_COLUMNS]
    y_train, y_test = train_df[TARGET], test_df[TARGET]
    
    return X_train, X_test, y_train, y_test