# Create a manifest that kills a process named killmenow

exec { 'kill_killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  onlyif  => '/bin/pgrep -f killmenow',
}
