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

Members: `data`
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

