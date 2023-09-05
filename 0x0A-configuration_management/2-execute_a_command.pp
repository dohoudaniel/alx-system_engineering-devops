# A Puppet manifest file that kills a process named killmenow
# This manifest file:
#    Uses the 'exec' Puppet resource 
#    Uses 'pkill'
exec { 'kill':
    command => ''pkill -f killmenow,
    # onlyif  => 'pgrep -f killmenow',
    path    => ['usr/bin', '/usr/sbin'],
}
