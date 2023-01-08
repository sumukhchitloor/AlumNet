FROM php:7.4-apache

# Install dependencies
RUN apt-get update && apt-get install -y \
    libicu-dev \
    libpq-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libzip-dev

# Enable Apache mod_rewrite
RUN a2enmod rewrite

#install php-mysql
RUN apt-get update && apt-get install -y git curl libmcrypt-dev default-mysql-client
#RUN docker-php-ext-enable default-mysqli-clent


# Install PHP extensions
RUN docker-php-ext-configure gd --with-freetype --with-jpeg
RUN docker-php-ext-install -j$(nproc) \
    intl \
    pdo_mysql \
    pdo_pgsql \
    gd \
    zip

# Copy the website code to the container
COPY . /var/www/html

# Set the working directory to the website root
WORKDIR /var/www/html

# Set the Apache document root to the website root
ENV APACHE_DOCUMENT_ROOT /var/www/html
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

# Set the ownership and permissions of the website files
RUN chown -R www-data:www-data /var/www/html
RUN chmod -R 755 /var/www/html

# Expose the Apache port
EXPOSE 8080

# Run Apache in the foreground
CMD ["apache2-foreground"]
