FROM python:3.11-slim AS base

ENV PYTHONDONTWHRITEBYTECODE=1
ENV PYTHONPATH=/app/src
ENV PYTHONBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

FROM base AS dependencies

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

FROM base AS runtime

COPY --from=dependencies /usr/local /usr/local
COPY src ./src
COPY alembic ./alembic
COPY alembic.ini .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]