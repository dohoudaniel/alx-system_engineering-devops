# A Bash script that kills a process named killmenow
# Requirements:
# Must use the exec Puppet resource
# Must use pkill
exec { 'kill_my_process':
    command => 'pkill -f killmenow',
    path    => '/usr/bin/',
  # onlyif  => 'pgrep -f process_name',
}

