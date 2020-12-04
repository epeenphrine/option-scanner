FROM node:10
WORKDIR /app
COPY ./calendar_spread_api_frontend /app

RUN npm install

CMD npm start