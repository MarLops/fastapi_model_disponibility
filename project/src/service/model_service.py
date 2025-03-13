

from typing import List
import pandas as pd

from src.exceptions.model_exception import MultipleInputMissColumn
from src.models.model_consume import ModelInputSingle


def model_consume_service(input:ModelInputSingle) -> str:
    return ""


def validate_input_file(df:pd.DataFrame) -> bool:
    if [''] not in df.columns:
        raise MultipleInputMissColumn()

def model_consume_service_multiple(df:pd.DataFrame) -> List[str]:
    return [""]