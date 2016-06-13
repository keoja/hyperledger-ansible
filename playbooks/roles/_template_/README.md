# README.md
# Ansible Role: Acme 2.x

An Ansible role that installs Acme 2.x on Centos 7.x

## Requirements

If you are using SSL/TLS, you will need to provide your own certificate and key files. You can generate a self-signed certificate with a command like `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout example.key -out example.crt`.

## Role Variables

Available variables are listed below, along with default values:

    acme_listen_port: 80
    acme_listen_port_ssl: 443

## Dependencies

- username.iptables - configure the firewall and block all ports except those needed for the web server and ssh access.
- username.common - perform common server configuration

## Example Playbook

    - hosts: webservers
      roles:
        - { role: username.acme }

## License

Apache