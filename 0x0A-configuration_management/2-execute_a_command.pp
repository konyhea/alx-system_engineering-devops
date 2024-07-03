# kill me now process
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'pgrep killmenow',
}

