import pandas as pd

from pathlib import Path
from src.preprocessing import (
    preprocess_dataset,
    FEATURE_COLUMNS,
    TARGET
)


def make_sample_df():
    
    return pd.DataFrame(
        {
            "datetime": ["2011-01-01 00:00:00", "2011-01-01 01:00:00"],
            "season": [4, 4],
            "holiday": [0, 0],
            "workingday": [0, 0],
            "weather": [1, 2],
            "temp": [9.84, 9.02],
            "atemp": [14.395, 13.635],
            "humidity": [81, 80],
            "windspeed": [0.0, 0.0],
            "casual": [3, 8],
            "registered": [13, 32],
            "count": [16, 40],
        }
    )
    
    
def test_preprocess_creates_features():
    sample_df = make_sample_df()
    
    df = preprocess_dataset(sample_df)
    
    for col in FEATURE_COLUMNS:
        assert col in df
        
    
def test_preprocess_removes_unused_columns():
    sample_df = make_sample_df()
    
    df = preprocess_dataset(sample_df)
    
    unused_columns = [
        "datetime",
        "hour",
        "weekday",
        "casual",
        "registered",
    ]
    
    for col in unused_columns:
        assert col not in df
        
