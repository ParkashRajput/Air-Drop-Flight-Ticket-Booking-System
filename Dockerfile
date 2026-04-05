FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migrations (optional but useful)
RUN python manage.py migrate

CMD ["gunicorn", "capstone.wsgi:application", "--bind", "0.0.0.0:8000"]