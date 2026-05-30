import numpy as np

from typing import Dict
from sklearn.metrics import (
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
    r2_score
)

def calculate_metrics(y_true, y_pred) -> Dict[str, float]:
    metrics = {
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_true, y_pred)),
        "R2": r2_score(y_true, y_pred),
        "MAPE": mean_absolute_percentage_error(y_true, y_pred),
    }
    
    return metrics

def evaluate_model(model, X_train, X_test, y_train, y_test) -> Dict[str, float]:
    model.fit(X_train, y_train)
    
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    train_metrics = calculate_metrics(y_train, y_train_pred)
    test_metrics = calculate_metrics(y_test, y_test_pred)
    
    metrics = {}
    
    for metric_name, metric_value in train_metrics.items():
        metrics[f"train_{metric_name}"] = metric_value
        
    for metric_name, metric_value in test_metrics.items():
        metrics[f"test_{metric_name}"] = metric_value
        
    return metrics