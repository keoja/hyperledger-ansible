# README.md
# Ansible Role: swarmhost

An Ansible role that installs Docker Swarm.

## Requirements

-TBW

## Role Variables

Available variables are listed below, along with default values:

TBW

## Dependencies

-TBW

## Example Playbooks

    - hosts: swarmmanagers
      become: true
      roles:
        - {role: swarmhost,
                  is_swarm_manager: true
          }


    - hosts: swarmnodes
      become: true
      roles:
        - {role: swarmhost}


## License

Apache