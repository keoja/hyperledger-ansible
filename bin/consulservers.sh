#!/bin/bash
export ANSIBLE_NOCOWS=1; ansible-playbook --ask-become-pass -i fabrichosts playbooks/consulservers.yml
