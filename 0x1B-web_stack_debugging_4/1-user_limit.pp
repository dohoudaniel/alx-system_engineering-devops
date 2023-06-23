# edit /etc/security/limits.conf to increase user limit

exec {'hard_limit':
  command => "sed -i 's/holberton hard.*/holberton hard nofile 10000/' /etc/security/limits.conf",
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
}
exec {'soft_limit':
  command => "sed -i 's/holberton soft.*/holberton soft nofile 10000/' /etc/security/limits.conf",
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
  require => Exec['hard_limit']
}
