FROM python:3.12-slim

# Set the initial working directory
WORKDIR /app

# Install requirements first to leverage Docker's layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# (Crucial) Install gunicorn to run the server
RUN pip install gunicorn

# Copy the rest of your project into /app
COPY . .

# Move into the directory containing manage.py and the inner mysite module
WORKDIR /app/mysite

# Run Gunicorn binding to port 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "mysite.wsgi:application"]
