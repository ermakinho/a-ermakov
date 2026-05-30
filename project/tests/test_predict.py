from src.predict import predict_rentals

class DummyModel:
    def predict(self, x):
        return [42.42]


class NegativeDummyModel:
    def predict(self, x):
        return [-42.42]


def make_sample_input():
    return {
        "datetime": "2012-12-31 17:00:00",
        "season": 4,
        "holiday": 0,
        "workingday": 1,
        "weather": 2,
        "temp": 15.5,
        "atemp": 17.0,
        "humidity": 65,
        "windspeed": 12.5,
    }
    
    
def test_predict_returns_integer():
    model = DummyModel()
    sample_input = make_sample_input()
    
    prediction = predict_rentals(model, sample_input)
    
    assert isinstance(prediction, int)
    
    
def test_predict_returns_non_negative():
    model = NegativeDummyModel()
    sample_input = make_sample_input()
    
    prediction = predict_rentals(model, sample_input)
    
    assert prediction >= 0
    
    
def test_predict_rounds_prediction():
    model = DummyModel()
    sample_input = make_sample_input()
    
    prediction = predict_rentals(model, sample_input)
    
    assert prediction == 42