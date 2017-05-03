#!/bin/bash
export ANSIBLE_NOCOWS=1; ansible -i fabrichosts allmachines -m ping
