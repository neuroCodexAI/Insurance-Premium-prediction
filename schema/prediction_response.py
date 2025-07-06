
from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    prediction: str = Field(..., description="Predicted class")
    confidence: float = Field(..., description="Model's confidence", example=0.8432)
    class_probabilities: Dict[str, float] = Field(
        ..., description="Probability for each class",
        example={"High": 0.84, "Medium": 0.15, "Low": 0.01}
    )
