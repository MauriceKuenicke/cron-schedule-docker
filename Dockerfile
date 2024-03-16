# Use python:3 as the base image
FROM python:3

# Set Python buffer to make Docker logs continuous
ENV PYTHONUNBUFFERED=1

# Set container timezone
ENV TZ="Europe/Berlin"

# Set the working directory
WORKDIR /app

# Install cron and your dependencies
RUN apt-get update && apt-get -y install cron
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt install python3-dotenv

# Copy everything into the container
COPY . .

# Give execution rights on the cron job and apply it
RUN chmod 0644 /app/cronjob
RUN crontab /app/cronjob

# Log files need to exist before running the tail command
RUN mkdir /app/log
RUN touch /app/log/is_alive.log
RUN touch /app/log/hello_world_1.log
RUN touch /app/log/hello_world_2.log

# We need to save all environment variables to /etc/environment since cron doesn't load
# any Docker environment variables by default
CMD /bin/bash -c "printenv >> /etc/environment && cron && tail -f /app/log/*.log"