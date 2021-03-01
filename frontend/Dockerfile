FROM node:14
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
RUN npm install bootstrap@4.6.0 reactstrap@8.9.0 --legacy-peer-deps
RUN npm install axios@0.21.1
COPY . .
EXPOSE 8080
CMD [ "node", "server.js" ]