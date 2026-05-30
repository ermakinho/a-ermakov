from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    datetime: str = Field(
        description="Дата и время прогноза",
        examples=["2012-12-31 17:00:00"]
        )
    
    season: int = Field(ge=1, le=4, description="Сезон: 1-весна, 2-лето, 3-осень, 4-зима")
    holiday: int = Field(ge=0, le=1, description="Праздничный день: 0-нет, 1-да")
    workingday: int = Field(ge=0, le=1, description="Рабочий день: 0-нет, 1-да")
    weather: int = Field(
        ge=1, 
        le=4, 
        description="Погода: 1-ясно, 2-туман/облачно, 3-лёгкие осадки, 4-сильные осадки"
        )
    
    temp: float = Field(description="Фактическая температура, °С")
    atemp: float = Field(description="Ощущаемая температура, °С")
    humidity: int = Field(ge=0, le=100, description="Влажность, %")
    windspeed: float = Field(ge=0, description="Скорость ветра, мили/час")
    
class PredictResponse(BaseModel):
    predicted_demand: int
    
class HealthResponse(BaseModel):
    status: str = "OK"
    model_loaded: bool