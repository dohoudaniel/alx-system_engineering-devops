# A Puppet file that installs flask from pip3
# exec {'apt-get update':
#    command => '/usr/bin/apt-get update',
# }
# exec {'pip3 install Flask==2.1.0':
#     ensure  => 'installed',
#     require => Exec['apt-get update'],
# }
# Install Flask version 2.1.0 using pip3
exec {'apt-get update':
    command => '/usr/bin/apt-get update',
}
package { 'python3-pip':
    ensure => installed,
    before => Exec['apt-get update'],
}
package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
