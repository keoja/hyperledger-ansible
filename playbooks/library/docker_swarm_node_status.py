#!/usr/bin/python
DOCUMENTATION = '''
---
module: docker_swarm_node_status
short_description:
    - Get the status of a docker swarm node.
description:
    - A module for extracting the current status of a host with respect to its status as a node in a docker swarm.
author: Keoja LLC
'''

EXAMPLES = '''
- name: Query the host for its status as a docker swarm node
  docker_swarm_node_status:
  register: swarm_status
'''

import json
import docker

docker_py_installed = False

# Check to see if docker-py is installed
# See: https://docker-py.readthedocs.io/en/stable/client.html
try:
    from docker import Client
    docker_py_installed=True
except:
    try:
        from docker import APIClient as Client
        docker_py_installed=True
    except:
        docker_py_installed=False

def makeFacts(info):
    return {'is_active': info['Swarm']['LocalNodeState'] == "active" }
    #return info
    
def main():

    module = AnsibleModule(
     argument_spec = dict(
        ),
        add_file_common_args=True,
        supports_check_mode=True
    )

    # Are we good to go?
    if docker_py_installed:
       try: 
         info = Client().info()
         module.exit_json(changed=True, node=makeFacts(info))  
       except Exception as e:
         module.fail_json(msg=e.message)
    else:
       # No
       module.fail_json(msg='docker-py not installed')
        
# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
