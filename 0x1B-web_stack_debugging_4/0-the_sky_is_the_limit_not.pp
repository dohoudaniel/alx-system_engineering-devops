# Puppet File to fix the Nginx Bug

exec { 'increase limit':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
}
exec {'restart nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
  require => Exec['increase limit']
}
