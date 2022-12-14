Ansible Developer Guide for This Role
======

.. contents::
    :depth: 1
    :local:

This folder comes with a test ``playbook.yml`` using this role. ``run-playbook.sh`` allows you to execute this role (install, configure and link nessus agent) on the localhost. You should use this on your dev AWS EC2 box.

There are serveral variables considered as sensitive information. For development, you can create a ``vars-secrets.json`` (full path ``ise-ansible-nessus-agent/tests/vars-secrets.json``) and fill in secrets values. The python scripts ``prepare_vars.py`` is a pre-hook scripts runs before ``ansible-playbook`` command, which generated the desired ``vars.json`` file to be consumed.

NOTE:

    there is a task to download installation files from S3 bucket. **You need to attach an instance profile that grant you read access to the S3 artifacts bucket** (see ``defaults/main.yml`` file) to your Dev EC2 Box.

How to Test this Role on an AWS EC2 Instance
------

.. code-block:: bash

    # start from a fresh EC2 box

    # switch to root user
    $ sudo su root

    # install ansible
    $ sudo amazon-linux-extras install epel
    $ sudo yum install ansible

    # clone source code
    $ git clone https://github.com/GSA/ise-ansible-nessus-agent.git
    $ cd ise-ansible-nessus-agent

    # update your ansible code, commit and push to remote, then do:
    $ git pull && bash ./tests/run-playbook.sh

How to verify Nessus Agent are Running as a service
------

Reference: https://docs.tenable.com/nessus/Content/StartOrStopNessusAgent.htm

**RedHat, CentOS, and Oracle Linux**:

.. codeblock:: bash

    # check status
    /opt/nessus_agent/sbin/nessuscli agent status
    
    # start service
    /sbin/service nessusagent start

    # stop service	
    /sbin/service nessusagent stop
