# Tasks

The swarmhost Ansible role contains tasks for both a Docker Swarm manager, and a Docker Swarm node.  They are selected by the value of a boolean variable is\_swarm\_manager, which, if true, will start a Docker Swarm manager to begin execution in a Docker container, and then create an "overlay network" for the manager and nodes to communicate.  The creation of the overlay network can "fail" if it already exists, this should be ignored.  If the is\_swarm\_manager variable is false, then the playbook will start a Docker Swarm node to begin execution in a Docker container on the host.

