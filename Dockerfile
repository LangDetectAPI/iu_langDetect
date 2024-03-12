FROM python:3.10-slim
LABEL authors="amina"

# work directory
WORKDIR /app

# copy the requirements file
COPY requirements.txt .

# install the requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy the content of the local api directory to the working directory
COPY . .

EXPOSE 5000

#Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# command to run on container start
CMD ["flask", "run", "--host=0.0.0.0"]



