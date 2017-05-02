# Initial Setup of HIL and QUADS:

## HIL:

	1. cd to directory you're using for development
	2. git clone https://github.com/BUEC528-HIL-QUADS/hil
	3. cd hil
	4. copy-paste the following: yum install epel-release bridge-utils  gcc  httpd  ipmitool libvirt libxml2-devel  libxslt-devel  mod_wsgi net-tools python-pip python-psycopg2 python-virtinst python-virtualenv qemu-kvm telnet vconfig virt-install -y
	5. virtualenv .venv
	6. source .venv/bin/activate
	7. pip install -e .
	8. cp examples/haas.cfg.dev-no-hardware haas.cfg
	9. haas-admin db create
    10. create a new file called client_env
    11. In the file put: export HAAS_ENDPOINT=http://127.0.0.1:5000
    12. source client_env
	13. haas serve 5000 &
	14. haas serve_networks


	Leave the haas servers running, you can see changes happen in this window as commands are executed


	From separate teminal window:
	15. cd [hil installation path]/
	16. source .venv/bin/activate
    17. source client_env
	18. pip install -e .

	You are now free to use HIL from the second terminal window
	haas list_nodes all should return 0


## QUADS:

	1. Open a new terminal window
	2. cd to the same directory as hil
	3. git clone https://github.com/BUEC528-HIL-QUADS/quads
    4. git fetch origin
    5. git checkout final-demo
	6. yum install PyYAML, pip install pytest
	7. cd quads
	8. bin/quads.py --init
	9. If there's an error relating to opt/quads/log/quads.log, execute the following: 		touch /opt/quads/log/quads.log
	10. If you receive the following warning:  "WARNING - Warning: /opt/quads/data/schedule.yaml exists. Use --force to initialize.",
       use bin/quads.py --init --force
	11. Go into quads/conf/quads.yml, and go to lines 13-15.  The only lines you should leave uncommented is the
       hardware service you'd like to use, for example a HIL user would leave line 13, "hardwareservice: Hil", uncommented, and comment out lines 14 and 15.
       If you'd like to use the native QUADS hardware, Juniper, then you'd leave the line "hardwareservice: QuadsNative" uncommented.
       By default, it is set to Mock.

# Starting Commands
### Some basic commands to get you started using our implementation
	1. bin/quads.py --define-cloud cloud01 --description "Primary Cloud Environment"
	2. bin/quads.py --define-cloud cloud02 --description "02 Cloud Environment"
	3. bin/quads.py --define-cloud cloud03 --description "03 Cloud Environment"
	4. bin/quads.py --ls-clouds
	5. bin/quads.py --define-host host01 --default-cloud cloud01
	6. bin/quads.py --define-host host02 --default-cloud cloud02
	7. bin/quads.py --define-host host 03 --default-cloud cloud03
	8. go back to your terminal window from HIL steps 16-19
	9. haas list_projects
	10. haas list_nodes
	11. haas list_networks
	12. If you want to run our pytests, go into quads/testing and run pytest -v test_inventory.py
