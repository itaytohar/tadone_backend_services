# # Python image to use.
# FROM python:3.9-slim

# # Set the working directory to /app
# WORKDIR /app

# # copy the requirements file used for dependencies
# COPY requirements.txt .
# COPY main.py .
# # Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# # Copy the rest of the working directory contents into the container at /app
# COPY . .

# # Run app.py when the container launches
# ENTRYPOINT ["python", "main.py"]

#===========================================================================================

FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True


# Copy local code to the container image.
COPY . /src
WORKDIR /src

# Install Python Requirements
RUN pip install -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
