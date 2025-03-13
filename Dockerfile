FROM python:3.12

COPY ./requirements.txt /requirements.txt
RUN apt-get update
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
COPY ./project .
EXPOSE 8086
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8086"]