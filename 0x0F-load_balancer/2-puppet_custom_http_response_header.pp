
# Installing Nginx web server and configuring the header using puppet

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/Ddilibe permanent;/" /etc/nginx/sites-available/default ; sudo sed -i "s/location \/{/location \/ {\n\t\tadd_header X-Served-By \"$HOSTNAME\";\n/" /etc/nginx/sites-enabled/default; sudo service nginx start',
}
