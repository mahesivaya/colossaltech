FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# RUN apt-get update \
# 	&& apt-get install -y --no-install-recommends \
# 		postgresql-client \
# 	&& rm -rf /var/lib/apt/lists/*

# WORKDIR /usr/src/app
# COPY requirements.txt ./
# RUN pip install -r requirements.txt
# COPY . .

# EXPOSE 7000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:7000"]
