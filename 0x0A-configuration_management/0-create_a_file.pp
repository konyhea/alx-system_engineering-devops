# creating a file /temp
file { '/temp/school':
  ensure  => 'present',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
}

