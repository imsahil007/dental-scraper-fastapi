FROM python:3.8
FROM mongo:latest as mongodb
FROM redis:latest as redis

# Set environment variables
ENV SMTP_USERNAME="deployprojects@gmail.com" \
    SMTP_PASSWORD="" \
    DENTAL_BASE_URL="https://dentalstall.com/shop/" \
    SMTP_SERVER="smtp.gmail.com" \
    SMTP_PORT=587
    
WORKDIR /app
RUN apt-get update && apt-get install -y mongodb-clients redis-tools
# Copy MongoDB data from the MongoDB image
COPY --from=mongodb /data/db /data/db

# Copy Redis data from the Redis image
COPY --from=redis /data /data

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "settings.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Expose MongoDB and Redis ports
EXPOSE 27017 6379 8000