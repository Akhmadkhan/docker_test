PASSWORD=$(pwgen -n 16 -1 -s)
echo root:$PASSWORD | chpasswd 
echo "SSH Password: $PASSWORD"
/usr/sbin/sshd
