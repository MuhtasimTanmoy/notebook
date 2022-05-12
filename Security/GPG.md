# GPG

```sh
Generate keys:
-------------
gpg --full-generate-key
gpg --gen-key

List keys:
----------
# Only keys with private key
gpg --list-secret-keys
gpg --list-keys

# Signed File 
gpg --sign filename

# Signature
gpg --detach-sign filename

# Verify
gpg --verify filename.sig

# Export/Import keys:
# -------------------
gpg --export -a "Name" > public.key
gpg --export --armor --output public.key email
gpg --export-secret-keys Melvin > melvin-private-key.key

# Import others public key
gpg --import melvin_public.key
gpg --import melvin-private-key.key

# Encrypt & Decrypt
# -----------------
gpg -e -r "Name" users.csv
gpg --always-trust -e -r "Name" users.csv

# -----------------
gpg -d fileName.gpg
gpg --batch --passphrase "pass" users.csv.gpg

# Keybase export import
keybase pgp export | gpg --import
keybase pgp export -q keyID --secret | gpg --import --allow-secret-key-import
```