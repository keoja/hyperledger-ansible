# README.md
# Ansible Role: dockerhost

An Ansible role that provisions Docker and [Docker Compose](https://docs.docker.com/compose/) on a host to support the hosting of [Hyperledger Fabric](https://github.com/hyperledger/fabric) peers in Docker containers.

## Requirements

TBD

## Role Variables

Available variables are listed below, along with default values:

TBD

## Dependencies

TBD

## Example Playbook

    - hosts: webservers
      roles:
         - {role: dockerhost,
              user: "{{ lookup('env', 'USER') }}",
         }

## License

Apache