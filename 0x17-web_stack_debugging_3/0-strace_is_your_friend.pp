# fix 500 Internal Server Error in Wordpress cused by a typo phpp

exec{'replace phpp with php using sed':
  command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
