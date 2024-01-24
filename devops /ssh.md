# SSH

- Key generate
    ```bash
    ssh marcus@yourserver.url -p 2222  

    ssh-keygen -t rsa -C EMAIL
    ssh-keygen -t rsa -f CUSTOM_FILE_NAME

    ssh-keygen -p 
    # Then it wil ask for existing key path, old pass and new pass
    ```


- `~/.ssh/authorized_keys` is created to add public file
- `~/.ssh/config` to create shortcuts like `ssh SHORTCUT-NAME`.
    ```yml
    Host example
        HostName 0.0.0.0
        port 22
        User name
        IdentityFile ~/.ssh/id_rsa
    ```

# Resource
- [Simplifying ssh connection](https://futurestud.io/tutorials/simplify-your-ssh-connections-with-ssh-config-file)