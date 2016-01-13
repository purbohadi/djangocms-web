# Ansible playbooks for deploying a DjangoCMS application

The code is to shows how to use Ansible to deploy a
DjangoCMS site into a Vagrant box.

The Stack is: Django+Mysql+Nginx

## Before running the playbook

Don't forget to do the following:

    set the VagrantFile to fit your Vagrant configuration : private ip, box image os, etc.
    The ssh key to clone from github is in the files folder, you need to copy it to vagrant machine to allow git clone.
    You may also provide your own github setting and database config.    		

## Running the playbook

Then you can deploy DjangoCMS by doing:

    vagrant up
    ansible-playbook djangocms-web.yml


Then point your browser to: <http://192.168.33.11.xip.io> 

To backup your sql data and site config, you can do this:
    
    ansible-playbook backup-rotation.yml

The script will automate the process of backup config and db file if there are less than 7 successfull backup, if not it will delete the oldest backup files first.

If you have any issue or feedback please dont hesitate to contact me @purboh.
   

Cheers
