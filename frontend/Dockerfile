FROM node:18-alpine AS builder

WORKDIR /app

# Asterisk matches related package.json to copy
COPY package*.json ./

# npm clean install (ci) including dev dependencies for build
RUN npm ci

COPY . .

RUN npm run build

FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80