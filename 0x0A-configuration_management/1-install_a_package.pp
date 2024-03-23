# 1-install_a_package.pp

# First part of the code to install Flask package
package { 'flask':
  ensure => '2.1.0',
}

# Second part of the code to install Werkzeug package
package { 'werkzeug':
  ensure => '2.1.1',
}

