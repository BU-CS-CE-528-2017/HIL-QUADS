# This is a simple script illustrating how to call HIL API 
# 
# Vladimir

import pytest
import haas
from haas import model, server, api
from haas.test_common import config, config_set, fresh_database, \
    fail_on_log_warnings, with_request_context

# This is preliminary setup. You can ignore code starting from this line.

@pytest.fixture
def configure():
    config_set({
        'extensions': {
            'haas.ext.network_allocators.null': '',
            'haas.ext.auth.null': '',
            'haas.ext.obm.ipmi': '',
        },
        'database': {
            'uri': 'sqlite:///:memory:',
        }
    })
    config.load_extensions()

fresh_database = pytest.fixture(fresh_database)
fail_on_log_warnings = pytest.fixture(fail_on_log_warnings)
with_request_context = pytest.yield_fixture(with_request_context)

@pytest.fixture
def server_init():
    server.register_drivers()
    server.validate_state()

default_fixtures = ['fail_on_log_warnings',
                    'configure',
                    'fresh_database',
                    'server_init',
                    'with_request_context']

pytestmark = pytest.mark.usefixtures(*default_fixtures)

# Preliminary setup ends. Stop ignoring code.

# This function will be invoked if you type in shell: py.test HIL_API_demo.py
# You can add more sophisticated API calls which are documented in 
# http://hil.readthedocs.io/en/latest/apidesc.html

def test_test():
    
    api.node_register('node-99', obm={
                "type": "http://schema.massopencloud.org/haas/v0/obm/ipmi",
                "host": "ipmihost",
                "user": "root",
                "password": "tapeworm"})
    api.project_create('anvil-nextgen')
    api.project_connect_node('anvil-nextgen', 'node-99')
    api.project_detach_node('anvil-nextgen', 'node-99')
    api.project_delete('anvil-nextgen')