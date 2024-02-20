# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV FLASK_APP=src
ENV FLASK_DEBUG=1
ENV APP_NAME="User Authentication App"

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host", "0.0.0.0"]
