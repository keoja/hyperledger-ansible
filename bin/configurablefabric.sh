#!/bin/bash
export ANSIBLE_NOCOWS=1; ansible-playbook -e fabric=configurable -i fabrichosts playbooks/fabriclaunchers.yml
