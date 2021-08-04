FROM python:3.9

COPY . /app

WORKDIR /app

# Install packages
RUN pip install -r requirements.txt

# Run flask app
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0"]