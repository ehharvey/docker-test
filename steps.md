# Notes
* Use jinja2 for templating
* All services will be accessible via localhostonly

# Steps
## Enable
1. Find an unused port on the host OS. Note this port
2. Find a path for the volume mount(s) (code-server has a single volume, so maybe we can just stick to 1) 
3. Template a Docker Compose file to a specific location
4. Template a SystemD service to /etc/systemd/ directory. E.g., `/etc/systemd/docker-code-server.service`
5. Run `systemctl start docker-code-server`
6. Run `systemctl enable docker-coder-server`
7. (Bonus: Update nginx to reverse proxy to it)

## Enable
1. (Bonus: Update nginx to not route to it anymore)
2. Run `systemctl stop docker-code-server`
3. Run `systemctl disable docker-coder-server`
4. (Bonus: Remove its Docker Compose and SystemD Service files)