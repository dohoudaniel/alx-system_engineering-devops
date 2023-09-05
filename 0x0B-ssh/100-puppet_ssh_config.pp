# A Puppet manifest file that sets up your client SSH configuration file
# so that you can connect to a server without typing a password.
file_line { 'Turn off password authentication':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    PasswordAuthentication no',
}

file_line { 'Declaringt the identity file':
    ensure => 'present',
    path   => '/etc/ssh/sshd_config',
    line   => '    IdentityFile /root/.ssh/school',
}
