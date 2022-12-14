# Python image to use.
FROM python:3.9-slim

# # Set the working directory to /app
WORKDIR /app
ENV PYTHONUNBUFFERED True
# copy the requirements file used for dependencies
COPY requirements.txt .
COPY main.py .
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Run app.py when the container launches
ENTRYPOINT ["python", "main.py"]