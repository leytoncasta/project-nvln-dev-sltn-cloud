FROM python:3.9-slim

WORKDIR /Frontend

COPY dependencies.txt .

RUN pip install --no-cache-dir -r dependencies.txt

COPY pages/ pages/
COPY utils/ utils/
COPY router.py .
COPY app.py .

CMD ["python", "app.py"]
