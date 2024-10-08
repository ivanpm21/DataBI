FROM python:latest

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./migrate/migrate_data.py"]