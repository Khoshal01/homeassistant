# Use a suitable base image
FROM python:3.9

# Set environment variables
ENV LANG C.UTF-8
ENV TZ=UTC

# Create a working directory
WORKDIR /usr/src/app/

# Copy files
COPY test_inverter.py /usr/src/app/
COPY start.sh /usr/src/app/

# Ensure the script has execute permissions
RUN chmod +x /usr/src/app/start.sh

# Install required dependencies (update if needed)
RUN pip3 install requests


# Set the startup command
CMD ["/bin/bash", "/usr/src/app/start.sh"]
