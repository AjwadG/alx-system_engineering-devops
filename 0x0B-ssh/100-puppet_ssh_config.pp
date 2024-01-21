# adding PasswordAuthentication no to servers config 
exec { 'Turn off passwd auth':
  command => '/usr/bin/echo "PasswordAuthentication no" >> /etc/ssh/sshd_config'
}

# adding the public key to servers auth keys
exec { 'Declare identity file':
  command => '/usr/bin/cat ~/.ssh/school >> /root/.ssh/authorized_keys'
}
