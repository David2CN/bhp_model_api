from typing import Any, List, Optional

from pressure_model.preprocessing.validation import BHPInputSchema
from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class BHPInputs(BaseModel):
    inputs: List[BHPInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "AVG_ANNULUS_PRESS": 0,
                        "AVG_WHT_P": 37.93925125,
                        "DP_CHOKE_SIZE": 78.93540896,
                        "DAYS_1STPRD": 15,
                    }
                ]
            }
        }
