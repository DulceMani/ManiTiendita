# syntax=docker/dockerfile:1
FROM node:alpine
WORKDIR /app

COPY frontend/ManiTiendita/package*.json /app/
COPY frontend/ManiTiendita/vite.congif.js /app/
# RUN npm ci --only=productions
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD [ "npm","run", "dev" ]

FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /api
COPY backend/requirements.txt /api/
COPY backend/manage.py /api/
RUN pip install -r requirements.txt
COPY . /api/
