# README.md
# Ansible Role: fabriclauncher

An Ansible role that provisions and configures a host so it can create instances of [Hyperledger](https://www.hyperledger.org/) networks by deploying the [Hyperledger Fabric](https://github.com/hyperledger/fabric), in Docker containers, using [Docker Compose](https://docs.docker.com/compose/).

The Docker image used for the Hyperledger peer and member service, is pulled from [Docker Hub](https://hub.docker.com/), or from an alternative Docker Registry (not implemented).

## Requirements

Ansible 2.1 (Needed for the [docker_service](https://docs.ansible.com/ansible/docker_service_module.html) module that manages Docker Compose).

## Role Variables

Available variables are listed below, along with default values:

| Variable | Default Value | Comment |  
|----------|:---------------|---------| 
|fabriclauncher_user | none | The user account to store the Docker Compose files. |
|fabriclauncher_group | none | The user group to store the Docker Compose files. | 
|fabriclauncher_default_fabric | behave_4_noops | The default fabric to launch. |    
|fabric | behave_4_noops | The fabric to launch. |
|fabriclauncher_config_dir |  ~{{user}}/Fabric | The top-level directory to store the Docker Compose files on the host. |  
|fabriclauncher_behave_4_noops_dir |  behave_4_noops | The directory where the compose files for the behave_4_noops fabric are stored on the host. |
|fabriclauncher_docker_compose_version |  1.7.1 | The default version of [Docker Compose](https://docs.docker.com/compose/) to install. |
|fabriclauncher_vpeer_image |  "yeasy/hyperledger-peer" | The default Docker Image for the Hyperledger peer container to use. See [https://github.com/yeasy/docker-hyperledger-peer](https://github.com/yeasy/docker-hyperledger-peer) |
|fabriclauncher_msvc_image |  "yeasy/hyperledger-membersrvc"  | The default Docker Image for the Hyperledger member service container to use. See: [https://github.com/yeasy/docker-hyperledger-membersrvc](https://github.com/yeasy/docker-hyperledger-membersrvc) |

Variables for configurable fabric instance

| Variable | Default Value | Comment |  
|----------|:---------------|---------| 
|fabriclauncher_num_validating_peers| 6 | comment here |
|fabriclauncher_msvc_image | as above | as above |
|fabriclauncher_core_security_enabled | false | comment here |
|fabriclauncher_configurable_dir| "configurable" | comment here |
|fabriclauncher_membersrvc_container_name_root| "membersrvc" | comment here |
|fabriclauncher_vpeer_container_name_root | "vpeer" | comment here |



## Dependencies

- TBW

## Example Playbook

    - hosts: fabriclaunchers
      roles:
        -{ role: fabriclauncher,
                 user: "{{ lookup('env', 'USER') }}",
                 group: "{{'staff' if is_macosx else ansible_user}}",
         }

## License

Apache