#!/bin/bash
export ANSIBLE_NOCOWS=1; ansible-playbook -i fabrichosts --tags swarmmanager playbooks/swarmmanagers.yml