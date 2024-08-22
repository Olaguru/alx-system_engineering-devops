# increase the limit hard and soft of the /etc/security/limits.conf

#increase limit
exec { 'increase-hard-limit-of-holberton-user':
    command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
    path    => '/usr/bin/:/bin/',
}

#increase soft limit
exec { 'increase-soft-limit-of-holberton-user':
    command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
    path    => '/usr/bin/:/bin/',
}
