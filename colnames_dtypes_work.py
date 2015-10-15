# REMOVED UNNEEDED ONES:
from collections import OrderedDict
# Version 4
	COLNAMES_DTYPES_DICT = OrderedDict([('MMSI', np.int32),
										('Message_ID', np.int32),
										('Repeat_indicator', np.int32),
										('Time', np.object),
										('Millisecond', np.int32),
										('Region', np.float32),
										('Country', np.int32),
										('Base_station', np.int32),
										('Vessel_Name', np.float32),
										('Call_sign', np.float32),
										('IMO_ee', np.float32),
										('Ship_Type', np.float32),
										('Destination', np.float32),
										('ROT', np.float32),
										('SOG', np.float32),
										('Longitude', np.float32),
										('Latitude', np.float32),
										('COG', np.float32),
										('Heading', np.float32),
										('IMO_ihs', np.int32),
										('ShipName', np.object),
										('PortofRegistryCode', np.int32),
										('ShiptypeLevel2', np.object),
										('Voyage', np.object),
										('Direction', np.float32),
										('simple_direction', np.object)] )

# Version 3
	colnames_dtypes_dict = OrderedDict([('MMSI', np.int32),
										('Message_ID', np.int32),
										('Repeat_indicator', np.int32),
										('Time', np.object),
										('Millisecond', np.int32),
										('Region', np.float32),
										('Country', np.int32),
										('Base_station', np.int32),
										('Online_data', np.object),
										('Group_code', np.object),
										('Vessel_Name', np.float32),
										('Call_sign', np.float32),
										('IMO_ee', np.float32),
										('Ship_Type', np.float32),
										('Destination', np.float32),
										('ROT', np.float32),
										('SOG', np.float32),
										('Longitude', np.float32),
										('Latitude', np.float32),
										('COG', np.float32),
										('Heading', np.float32),
										('IMO_ihs', np.int32),
										('ShipName', np.object),
										('PortofRegistryCode', np.int32),
										('ShiptypeLevel2', np.object),
										('unique_trips', np.object),
										('unique_trips_dest', np.object),
										('time_modified', np.float32),
										('day_breaks', np.int16),
										('clusters', np.object),
										('Voyage', np.object),
										('Direction', np.float32),
										('simple_direction', np.object),
										('Distance', np.float32) ] )
# Version 2
colnames_dtypes_dict = OrderedDict( [ ('MMSI',np.int32),
						('Repeat_indicator',np.int32),
						('Time',np.object),
						('Millisecond',np.int32),
						('Region',np.float32),
						('Country',np.int32),
						('Base_station',np.int32),
						('Online_data',np.object),
						('Vessel_Name',np.float32),
						('Call_sign',np.float32),
						('IMO_ee',np.float32),
						('Ship_Type',np.float32),
						('Destination',np.float32),
						('ROT',np.object),
						('SOG',np.float32),
						('Longitude',np.float32),
						('Latitude',np.float32),
						('COG',np.object),
						('Heading',np.object),
						('IMO_ihs',np.int32),
						('ShipName',np.object),
						('PortofRegistryCode',np.int32),
						('ShiptypeLevel2',np.object),
						('day_breaks',np.bool),
						('Voyage',np.object),
						('Direction',np.float32),
						('simple_direction',np.object),
						('Distance',np.float32),
						('akalb_lon', np.float64),
						('akalb_lat', np.float64) ] )

# Version 1
colnames_dtypes_dict = {'MMSI':np.int32,
						'Unnamed: 1':np.int32,
						'MMSI.1':np.int32,
						'Message_ID':np.int32,
						'Repeat_indicator':np.int32,
						'Time':np.object,
						'Millisecond':np.int32,
						'Region':np.float16,
						'Country':np.int32,
						'Base_station':np.int32,
						'Online_data':np.object,
						'Group_code':np.object,
						'Vessel_Name':np.float16,
						'Call_sign':np.float16,
						'IMO_ee':np.float16,
						'Ship_Type':np.float16,
						'Destination':np.float16,
						'ROT':np.object,
						'SOG':np.float16,
						'Longitude':np.float16,
						'Latitude':np.float16,
						'COG':np.object,
						'Heading':np.object,
						'IMO_ihs':np.int32,
						'ShipName':np.object,
						'PortofRegistryCode':np.int32,
						'ShiptypeLevel2':np.object,
						'unique_trips':np.object,
						'unique_trips_dest':np.object,
						'time_modified':np.float16,
						'day_breaks':np.bool,
						'clusters':np.object,
						'Voyage':np.object,
						'Direction':np.float16,
						'simple_direction':np.object,
						'Distance':np.float16}


