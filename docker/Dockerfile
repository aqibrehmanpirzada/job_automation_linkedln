FROM python:3.12-slim

RUN apt-get update && apt-get install -y wget unzip chromium && \
    wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/local/bin/ && \
    rm -f chromedriver_linux64.zip && \
    apt-get clean && rm -rf /var/lib/apt/lists/* 
    
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Run the bot script by default
CMD ["python", "runAiBot.py"]