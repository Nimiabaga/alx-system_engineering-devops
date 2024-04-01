# Install,Config with a custom header and Start Nginx

# Update package lists
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-update'],
}

# Add a custom HTTP header
file_line {'Adding_Header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => '    add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
