# dockerfile for Drupal
FROM drupal:php7.4-apache

RUN apt-get update && apt-get install -y curl nano git unzip

RUN curl "https://getcomposer.org/installer" > composer-setup.php

RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer

RUN mkdir modules && cd modules && git clone https://github.com/auth0/auth0-drupal.git auth0 && cd auth0 && composer install 

RUN sed -i s/80/\${PORT}/g /etc/apache2/ports.conf
RUN sed -i s/80/\${PORT}/g /etc/apache2/sites-enabled/000-default.conf

RUN cat /etc/apache2/ports.conf

RUN echo ': ${PORT:=80}' >> /etc/apache2/envvars
RUN echo "export PORT" >> /etc/apache2/envvars

