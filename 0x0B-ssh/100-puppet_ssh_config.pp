# Setting up my client SSH configuration
include 'stdlib'  # Use single quotes for string literals

# Disable password authentication
file_line { 'Turn off password auth':  # Provide a descriptive name
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => /^\s*PasswordAuthentication\s+/  # Match existing line before replacing
  replace => true,
}

# Set identity file
file_line { 'Declare identity file': # Provide a descriptive name
  ensure  => present,  # Remove indentation here
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}
