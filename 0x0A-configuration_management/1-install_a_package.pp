# Ensure python3-pip is installed

package { 'python3-pip':
  ensure => installed,
}


# Ensure Flask version 2.1.0 is installed using pip3

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
}
