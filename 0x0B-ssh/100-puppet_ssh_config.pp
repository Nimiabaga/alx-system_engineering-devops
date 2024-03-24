# connect to a server

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "\
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
    PubkeyAuthentication yes
",
}
