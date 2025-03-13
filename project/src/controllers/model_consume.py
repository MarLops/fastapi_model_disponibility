from io import StringIO

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import pandas as pd

from src.exceptions.model_exception import MultipleInputMissColumn
from src.service.model_service import model_consume_service, model_consume_service_multiple, validate_input_file
from src.controllers.auth import get_current_username
from src.models.model_consume import ModelInputSingle


app_model_consume=  APIRouter(tags=['barconfig'])


@app_model_consume.post('/consume/single')
async def model_consume(model:ModelInputSingle, user:str =  Depends(get_current_username)):
    """
        Consume Model to only one record
    
    """
    try:
        response = model_consume_service(model)
        return response
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    

@app_model_consume.post('/consume/multi')
async def model_consume(file: UploadFile = File(...), user:str =  Depends(get_current_username)):
    """
        Consume Model by csv file
    """
    try:
        if not file.filename.endswith(".csv"):
            raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")
        content = await file.read()
        df = pd.read_csv(StringIO(content.decode("utf-8")))
        validate_input_file(df)
        response = model_consume_service_multiple(df)
        return response
    except MultipleInputMissColumn as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail="Miss column"
        )
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    