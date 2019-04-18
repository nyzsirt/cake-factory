FROM python:latest

# Set the working directory to /app
WORKDIR /opt
# Copy the current directory contents into the container at /app
ADD . app
RUN pip install -U pip setuptools

WORKDIR app
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Run app.py when the container launches
CMD ["mrq-worker", "-c", "config/config.py"]
