# A puppet manuscript to replace a line in a file on a server
$fileToEdit = '/var/www/html/wp-settings.php'
# Replace the line in the wp-settings.php file containing "phpp" with "php"
exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' ${fileToEdit}",
  path    => ['/bin','/usr/bin']
}
