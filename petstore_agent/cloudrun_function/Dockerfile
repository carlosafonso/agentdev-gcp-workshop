# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Cloud Run sets the PORT environment variable
ENV PORT 8080

# Expose the port
EXPOSE 8080

# Run the application using Gunicorn, a production-ready server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]