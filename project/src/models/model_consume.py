

from datetime import datetime
from typing import Dict, List, Union
from pydantic import BaseModel, Field, computed_field, constr



class ModelInputSingle(BaseModel):
    number_id : int = Field(...,description='id of seats')

   