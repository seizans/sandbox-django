FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

VOLUME /etc/nginx/sites-enabled
VOLUME /var/log/nginx

WORKDIR /etc/nginx
EXPOSE 80
ENTRYPOINT ["nginx"]
