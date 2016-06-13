# Group variables

This folder contains files that define variables for different groups of machines.

all.yml - Contains a number of different variable definitions that are common to all groups.  The ones in the table below might require customization for your particular configuration.  The values of the other variables in the file can be changed, but are not likely to require any initial adjustment.


| Variable | Default Value | Comment|
| ---------- |--------|
| hl\_num\_validating_peers   |  8   | The number of Hyperledger validating peers to run in the Fabric. |
| hl\_vpeer\_docker_image     | "yeasy/hyperledger-peer" | The Docker image to use for the validating peer. | 
| hl\_msvc\_docker_image      | "yeasy/hyperledger-membersrvc" | The Docker image to use for the member service.  |
| hl\_identifier               | hyperledger | The identifier used for network domains, etc. |
| hl\_network\_subnet           | "10.12.34"  | This is the subnet of the network supporting the Docker Swarm.  This needs to be customized to the particular network in used. |
| hl\_main\_server\_ip           | "{{hl_network_subnet}}.92"  |  This is the ip address of the host that will be the Consul server and the Docker Swarm manager. |
 
