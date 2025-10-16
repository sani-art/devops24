# Examination 1 - Understanding SSH and public key authentication

Connect to one of the virtual lab machines through SSH, i.e.

    $ ssh -i deploy_key -l deploy webserver

Study the `.ssh` folder in the home directory of the `deploy` user:

    $ ls -ld ~/.ssh

Look at the contents of the `~/.ssh` directory:

    $ ls -la ~/.ssh/

## QUESTION A

What are the permissions of the `~/.ssh` directory?

- The permissions are rwx (read, write and execute). Only the owner has the permissions. 

Why are the permissions set in such a way?

- In order to protect private SSH keys and prevent other users from having the access. 


## QUESTION B

What does the file `~/.ssh/authorized_keys` contain?

- It contains public SSH keys from users who are allowed to log in without a password. 


## QUESTION C

When logged into one of the VMs, how can you connect to the
other VM without a password?

- I generate a SSH key pair by using ssh-keygen on the first VM and copy the public key to the file ~/.ssh/authorized_keys on the other VM. Then, SSH uses the private key for authentication, so I can log in without a password. 

### Hints:

* man ssh-keygen(1)
* ssh-copy-id(1) or use a text editor

## BONUS QUESTION

Can you run a command on a remote host via SSH? How?

- Yes, I can run a command by writing it after the SSH command. 

For example: 

ssh deploy@192.168.121.154 ls -l

This will run the command on the remote machine I choose and shows the output in my local terminal.