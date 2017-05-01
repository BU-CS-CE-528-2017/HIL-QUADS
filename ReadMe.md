Initial Setup of HIL and QUADS:

HIL:
	cd to directory you're using for development
	git clone https://github.com/saacg/hil
	cd hil
	yum install epel-release bridge-utils  gcc  httpd  ipmitool libvirt libxml2-devel  libxslt-devel  mod_wsgi net-tools python-pip python-psycopg2 python-virtinst python-virtualenv qemu-kvm telnet vconfig virt-install -y (just copy-pasting this command is easiest)
	virtualenv .venv
	source .venv/bin/activate
	pip install -e .
	cp examples/haas.cfg.dev-no-hardware haas.cfg
	haas-admin db create
	haas serve 5000
	Leave the haas server running, you can see changes happen in this window as commands are executed

	From separate teminal window:
	cd ~/hil/
	virtualenv .venv
	source .venv/bin/activate
	pip install -e .
	
	You are now free to use HIL from the second terminal window
	haas list_nodes all should return an empty list



QUADS:
	Open a new terminal window
	cd to the same directory as hil	
	git clone https://github.com/saacg/quads
	yum install PyYAML
	cd quads
	bin/quads.py --init
	If you receive the following warning:  "WARNING - Warning: /opt/quads/data/schedule.yaml exists. Use --force to initialize.", use bin/quads.py --init --force 
	







