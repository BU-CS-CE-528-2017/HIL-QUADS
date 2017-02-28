#HIL model.py class descriptions

All appear to be subclassed from db.Model

 

##Project

###Members:

    Id (integer)
    Label (string)
    Nodes (backref)
    Networks_created (backref)
    Networks_access (backref)

###Methods:

    _init_

 

##Nic

###Members:

    Id (integer)
    Label (string)
    Owner_id (node.id)
    Owner (Node)
    Mac_addr (string)
    Port_id (port.id)
    Port (Port)
    Current_action (backref)
    Attachments (backref)

###Methods:

    _init_

 

##Node

###Members:

    Id (integer)
    Label (string)
    Project_id (project.id)
    Project (Project)
    Obm_id (obm.id)
    Nics (backref)
    Obm (Obm)
    Metadata (backref)

###Methods:

    none

 

##Metadata

###Members:

    Id (int)
    Label (string)
    Value (string)
    Owner_id (node.id)
    Owner (Node)

###Methods:

    _init_

 

##Network

###Members:

    Id (int)
    Label (string)
    Owner_id (project.id)
    Owner (Project)
    Access (Project or None)
    Allocated (Boolean)
    Network_id (used by driver)
    Scheduled_nics (backref)
    Attachments (backref)

###Methods:

    _init_

 

##Port

###Members:

    Id (int)
    Label (string)
    Owner_id (switch.id)
    Owner (Switch)
    Nic (backref)

###Methods:

    _init_

 

##Switch

###Members:

    Id (int)
    Label (string)
    Type (string)
    _mapper_args_
        Polymorphic_identity
        Polymorphic_on
    Ports (backref)

###Methods:

    Validate (static)
    Session
    Apply_network
    Disconnect
    Get_port_networks

 

##Obm

###Members:

    Id (int)
    Type (string)
    _mapper_args_
        Polymorphic_on
    Node (backref)

###Methods:

    Validate (static)
    Power_cycle
    Power_off
    Start_console
    Stop_console
    Delete_console
    Get_console
    Get_console_log_filename

 

##NetworkingAction

###Members:

    Id (int)
    Nic_id (nic.id)
    New_network_id (network.id)
    Channel (string)
    Nic
    New_network

 

##NetworkAttachment

###Members:

    Id (int)
    Nic_id (nic.id)
    Network_id (network.id)
    Channel (string)
    Nic
    Network
