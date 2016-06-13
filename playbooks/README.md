# Playbooks

This folder contains Ansible playbooks to provision and configure hosts for Hyperledger.

| Playbook  |  Comment  |
|-----------|-----------|
| consulclients.yml     | Playbook to provision Consul clients.  |
| consulservers.yml     | Playbook to provision Consul servers.  |
| dockerhosts.yml       | Playbook to provision hosts to support Docker containers, Docker Swarm, and Docker Compose, as well as as the interface between Ansible and the Docker daemon on the host. |
| fabriclaunchers.yml   | Playbook to provision and launch the Fabric from a host using Docker Compose.  |
| swarmmanagers.yml     | Playbook to provision and configure hosts that are Docker Swarm managers. |
| swarmnodes.yml        | Playbook to provision and configure hosts that are Docker Swarm nodes.  Each swarm node will register with Consul to be discovered by the swarm managers.  They will host peers for the Hyperledger Fabric. |
 



