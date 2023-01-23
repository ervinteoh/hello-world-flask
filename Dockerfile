FROM node:latest as tailwindcss

WORKDIR /usr/src/app
COPY package.json ./
COPY postcss.config.js ./
COPY tailwind.config.js ./
COPY webpack.config.js ./

RUN npm install
COPY ./src ./src
RUN npm run build

FROM python:3.9-alpine

WORKDIR /usr/src/app
ARG DATABASE_URL
ENV DATABASE_URL=${DATABASE_URL}
ENV FLASK_APP=src:create_app()

COPY requirements.txt requirements.txt
RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r requirements.txt
COPY ./migrations ./migrations
COPY ./src ./src
COPY --from=tailwindcss /usr/src/app/src/static/dist ./src/static/dist

RUN flask db upgrade
CMD ["gunicorn", "-b", "0.0.0.0:80", "-w", "4", "src:create_app()"]
