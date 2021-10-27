from os import system
system('add-apt-repository ppa:gnome3-team/gnome3')
system('apt-get update')
system('apt-get install gnome-session&&apt-get install gnome-shell')
print('gnome successfully installed !')
print('To use gnome run (gnome-shell --replace)')