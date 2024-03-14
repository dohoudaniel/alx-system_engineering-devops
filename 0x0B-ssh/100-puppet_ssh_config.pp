# A Puppet manifest file that sets up your client SSH configuration file
# so that you can connect to a server without typing a password.
file_line { 'Turn off password auth':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    PasswordAuthentication no',
}

file_line { 'Declaring identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/school',
}
