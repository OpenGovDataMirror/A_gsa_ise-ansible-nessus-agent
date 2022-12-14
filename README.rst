ise-ansible-nessus-agent
======

This is an Ansible Role that install, configure and link nessus agent to GSA sec helix nessus server.

How to Use This Role
------

1. add ``- src: https://github.com/GSA/ise-ansible-nessus-agent`` to your ``requirements.yml`` file.
2. Find secrets variable values for ``nessus_agent_key`` and ``nessus_server_url``, ise team should be able to give you this information.

How to Dev This Role
------

There are some helper scripts allows you to test this Role on AWS EC2. Please read `Ansible Developer Guide for This Role <./tests/README.rst>`_ for more info.
