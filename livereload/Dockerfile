FROM node:10-alpine

RUN npm i --global livereload@0.9.1
WORKDIR /livereload

ENTRYPOINT livereload . -w 1000 -d -u true
