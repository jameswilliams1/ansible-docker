import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hosts_file(host):
    f = host.file("/etc/hosts")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


@pytest.mark.parametrize(
    "pkg", ["docker", "docker-engine", "docker.io", "containerd", "runc"]
)
def test_old_docker_packages_not_installed(host, pkg):
    package = host.package(pkg)
    assert not package.is_installed


@pytest.mark.parametrize("pkg", ["docker-ce"])
def test_docker_packages_installed(host, pkg):
    package = host.package(pkg)
    assert package.is_installed


def test_docker_compose_installed(host):
    compose_path = host.file("/usr/local/bin/docker-compose")
    assert compose_path.exists
    assert compose_path.is_file


def test_docker_compose_symlink(host):
    compose_symlink = host.file("/usr/bin/docker-compose")
    assert compose_symlink.exists
    assert compose_symlink.is_symlink


@pytest.mark.parametrize("cmd", ["docker", "docker-compose"])
def test_docker_cli_commands(host, cmd):
    assert host.command(cmd)


def test_user_in_docker_group(host):
    user = host.user("vagrant")
    docker_group = host.group("docker")
    assert docker_group.exists
    assert "docker" in user.groups
