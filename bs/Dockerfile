FROM node:10-alpine

RUN npm i --global browser-sync
WORKDIR /code

ENV CHOKIDAR_USEPOLLING=true
ENTRYPOINT browser-sync start --proxy "app:5000" --files "app.py" --no-open --reload-delay 500
