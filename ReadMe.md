# Initial Setup of HIL and QUADS:

## HIL:

	1. cd to directory you're using for development
	2. git clone https://github.com/BUEC528-HIL-QUADS/hil
	3. cd hil
	4. yum install epel-release bridge-utils  gcc  httpd  ipmitool libvirt libxml2-devel  libxslt-devel  mod_wsgi net-tools python-pip python-psycopg2 python-virtinst python-virtualenv qemu-kvm telnet vconfig virt-install -y (just copy-pasting this command is easiest)
	5. virtualenv .venv
	6. source .venv/bin/activate
	7. pip install -e .
	8. cp examples/haas.cfg.dev-no-hardware haas.cfg
	9. haas-admin db create
	10. haas serve 5000
	Leave the haas server running, you can see changes happen in this window as commands are executed
	11. 

	From separate teminal window:
	12. cd ~/hil/
	13. virtualenv .venv
	14. source .venv/bin/activate
	15. pip install -e .
	
	You are now free to use HIL from the second terminal window
	haas list_nodes all should return an empty list



## QUADS:

	1. Open a new terminal window
	2. cd to the same directory as hil	
	3. git clone https://github.com/BUEC528-HIL-QUADS/quads
	4. yum install PyYAML
	5. cd quads
	6. bin/quads.py --init
	7. If there's an error relating to opt/quads/log/quads.log, execute the following: 		touch /opt/quads/log/quads.log	
	8. If you receive the following warning:  "WARNING - Warning: /opt/quads/data/schedule.yaml exists. Use --force to initialize.", use bin/quads.py --init --force 

# Starting Commands

