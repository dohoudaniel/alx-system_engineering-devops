# A Puppet manifest file that installs flask from pip
# This manifest file installs it, if it does not exists,
# and it updates it to the specified version if it does.
package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
