from jinja2 import Template

TEMPLATE_DATA = """
---
version: "2.1"
services:
  code-server:
    image: {{ image }}
    container_name: code-server
    volumes:
      - {{ volume }}:/config
    ports:
    # Bind to arbitrary port but only LOCALHOST
      - 127.0.0.1:{{ port }}:8443
    restart: unless-stopped
"""

DATA = {
    "image": "lscr.io/linuxserver/code-server:latest",
    "volume": "/volumes/code-server",
    "port": 5000
}

print(Template(TEMPLATE_DATA).render(DATA))