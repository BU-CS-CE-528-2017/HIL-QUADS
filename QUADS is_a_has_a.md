# libquads.py Class description
##Hosts
 
`_init_`

`host_list`

Members: `data`

##Clouds

`_init_`

`cloud_list`

Members: `data`

##History

`_init_`

Members: `data`

##QUADSData

`_init_` initializes QUADSData object using [Hosts](#hosts), [Clouds](#clouds) and [History](#history)

##QUADS

`_init_`

Members: `config, statedir, movecommand, datearg, syncstate, initialize, force`
#
`_quads_history_init` to initialize history

Members: `data`([History](#history))
#
`quads_write_data` to write data back

Members: `data` (all 3 [Hosts](#hosts), [Clouds](#clouds) and [History](#history))
#
`quads_init_data` if passed --init, the config data is wiped

Members: `data` (all 3 [Hosts](#hosts), [Clouds](#clouds) and [History](#history))
#
`_quads_find_current` which is a helper function called from other methods and not from main()

Members: `host, history, current_time, requested_time, start_obj, end_obj, default_cloud, current_cloud, current_override`
#
`quads_sync_state` for syncing the statedir db for hosts with schedule

Members: `default_cloud, current_cloud, current_override`
#
`quads_list_hosts` to list the hosts

Members: `host_list()`
#
`quads_list_clouds` to list clouds

Members: `cloud_list()`
#
`quads_list_owners` to list owners

Members: `clouds.data`
#
`quads_list_cc` to list cc users

Members: `data`
#
`quads_list_tickets` to list the tickets

Members: `clouds.data`
#
`quads_list_qinq` list qinq status

Members: `cloud.data`
#
`quads_remove_host` remove a host

Members: `hosts.data`
#
`quads_remove_cloud` remove cloud

Members: `hosts.data`
#






