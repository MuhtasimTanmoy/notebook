# NGINX

- A lightweight reverse proxy.
- Suppose you have a server and you are running two web apps on it. 
- One on port 8000 and one on `8001`. 
- Now suppose we have a domain name "example.com". 
- We want `abc.example.com` to get routed to port 8000 of the machine and `xyz.example.com` to get routed to the 8001 port of the machine.
- For that, we create 1 file for each web app we want to configure at `/etc/nginx/sites-enabled`. 
- The file names could be anything. Let's just name them the same as the sub-domain they represent.


I mostly code in nodejs. So I usually have a web app running on localhost. So the configuration looks like this:

```bash
server {
    listen 80; listen [::]:80;
    server_name abc.example.com;  # <-- change this

    location / {
        proxy_pass http://localhost:8000; # <-- And this
 }
}
```

### How to add a site

```bash
cd /etc/nginx/sites-enabled
touch site.conf
vim site.conf

# Paste the following inside the site.conf
server {
    listen 80; listen [::]:80;
    server_name a.domain.com;  # <-- change this

    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 }
}
```

### How to enforce HTTPS?

```bash
if ($scheme != "https") {
    return 301 https://$host$request_uri;
} # managed by Certbot
```

### Mixed content error

We once got mixed content errors after upgrading to SSL. To fix the issue, we simply had to add some headers to the location block.

```bash
location / {
  proxy_pass http://localhost:8000;
  proxy_set_header Host $http_host;
  proxy_http_version 1.1;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Forwarded-Proto https;
}
```