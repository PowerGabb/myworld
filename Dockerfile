FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt* .
RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt; fi

# Copy project
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "kisagold/manage.py", "runserver", "0.0.0.0:8000"] 