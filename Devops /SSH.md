# SSH


```

ssh marcus@yourserver.url -p 2222  

ssh-keygen -t rsa -C EMAIL
ssh-keygen -t rsa -f CUSTOM_FILE_NAME

ssh-keygen -p # Then it wil ask for existing key path, old pass and new pass

Create a file `~/.ssh/authorized_keys` and add public keys to it, one in each line.

You can create `~/.ssh/config` to create shortcuts like `ssh SHORTCUT-NAME`.

Create a file: `~/.ssh/config`

```ssh
Host example
    HostName 0.0.0.0
    port 22
    User name
    IdentityFile ~/.ssh/id_rsa
```


# Resource
- https://futurestud.io/tutorials/simplify-your-ssh-connections-with-ssh-config-file