# Ansible playbooks for deploying a DjangoCMS application

The code for this chapter shows how to use Ansible to deploy a
DjangoCMS site into a Vagrant box.

## Before running the playbook

Don't forget to do the following:

    cd playbooks
    cp secrets.yml.example secrets.yml

## Running the playbook

Then you can deploy DjangoCMS by doing:

    vagrant up
    ansible-playbook djangocms-web.yml



Then point your browser to: <http://192.168.33.10.xip.io> or
<https://www.192.168.33.10.xip.io>. You'll get a security warning if you use the
https site since it's a self-signed certificate, this is normal.

