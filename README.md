# ansible-docker

Install Docker, Docker Compose and completions with Ansible.

## Requirements

- Python

**Note:** May require additional apt packages on systems older than those tested (Ubuntu bionic/Debian buster).

## Role Variables

`compose_version: 1.24.1` version number of docker-compose to install  
`compose_install_directory: /usr/local/bin/docker-compose` install directory for docker-compose  
`docker_users:` list of users to add to "docker" group (defaults to ansible ssh user)

## Dependencies

None

## Example Playbook

    - hosts: all
      vars:
        compose_version: 1.24.1
        compose_install_directory: /non/standard/path
        docker_users:
          - ubuntu
          - vagrant
      roles:
         - docker

## License

Apache 2.0

## Author Information

James Williams  
https://github.com/jameswilliams1
