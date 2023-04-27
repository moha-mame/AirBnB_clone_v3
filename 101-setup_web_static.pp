# puppet manifest file to setup web static server

# update package list
package { 'update':
  ensure => 'latest',
}

# install nginx
package { 'nginx':
  ensure => 'installed',
}

# create necessary directories
file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0775',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0775',
}

# create index.html file
file { '/data/web_static/releases/test/index.html':
  content => "<html>
                <head>
                </head>
                <body>
                  Holberton School
                </body>
              </html>",
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# create symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test/',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0775',
}

# configure nginx
file { '/etc/nginx/sites-available/default':
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;
                root /var/www/html;

                index index.html index.htm index.nginx-debian.html;

                server_name _;

                location / {
                        try_files $uri $uri/ =404;
                }

                location /hbnb_static/ {
                        alias /data/web_static/current/;
                }
            }",
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# restart nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => [
    File['/etc/nginx/sites-available/default'],
    File['/data/web_static/current'],
    File['/data/web_static/releases/test/index.html'],
  ],
}
