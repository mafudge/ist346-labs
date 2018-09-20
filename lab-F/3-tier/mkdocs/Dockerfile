FROM gliderlabs/alpine:3.2

RUN apk add --update python3 py-pip && pip3 install mkdocs mkdocs-material && rm -rf /var/cache/apk/*

WORKDIR /docs

VOLUME /docs
EXPOSE 8000