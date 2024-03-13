# A Puppet file that installs flask from pip3
exec {'apt-get update':
    command => '/usr/bin/apt-get update',
}
exec {'pip3 install Flask==2.1.0':
    ensure  => 'installed',
    require => Exec['apt-get update'],
}
