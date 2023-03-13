from jinja2 import Template

TEMPLATE_DATA = """
[Unit]
Description=Vs Code with docker compose
PartOf=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=true
WorkingDirectory={{ compose_directory }}
ExecStart=/usr/local/bin/docker-compose up -d --remove-orphans
ExecStop=/usr/local/bin/docker-compose down
User=conglobo

[Install]
WantedBy=multi-user.target
"""

DATA = {
    "compose_directory": "/compose/code-server/"
}

print(Template(TEMPLATE_DATA).render(DATA))