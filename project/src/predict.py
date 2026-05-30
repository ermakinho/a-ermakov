import pandas as pd

from typing import Dict
from src.preprocessing import preprocess_dataset, FEATURE_COLUMNS

def predict_rentals(model, input_data: Dict) -> int:
    input_df = pd.DataFrame([input_data])
    
    processed_df = preprocess_dataset(input_df)
    
    X = processed_df[FEATURE_COLUMNS]
    
    prediction = model.predict(X)[0]
    prediction = max(prediction, 0)
    prediction = round(prediction)
    
    return int(prediction)
    