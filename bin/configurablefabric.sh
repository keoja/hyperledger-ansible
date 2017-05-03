#!/bin/bash
export ANSIBLE_NOCOWS=1; ansible-playbook --ask-become-pass -e fabric=configurable -i fabrichosts playbooks/fabriclaunchers.yml
