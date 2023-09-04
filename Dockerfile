# Use an official Python runtime as a parent image
FROM python:3.10.6

# Set the working directory to /app
WORKDIR /app

COPY . .

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org Flask
RUN pip install requests
RUN pip install waitress

# Run server.py when the container launches
CMD ["waitress-serve", "--listen=*:7575", "server:app"]
