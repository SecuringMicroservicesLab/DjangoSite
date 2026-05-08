# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install your requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# (Crucial) Install gunicorn to run the server
RUN pip install gunicorn

# Copy the rest of your Django project
COPY . .

# Start the server (Replace 'myproject' with the actual name of your main Django folder!)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]
