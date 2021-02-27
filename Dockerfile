FROM python:3.6 as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --prefix=/install --no-warn-script-location -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
WORKDIR /app
RUN mkdir -p logs
COPY src .
EXPOSE 8084
CMD gunicorn --bind 0.0.0.0:8084 --log-config /app/logconfig.conf app:app