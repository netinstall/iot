'''

https://github.com/rytilahti/python-miio/issues/1217

It's already shared.
You can download it here:
https://github.com/FM84DEV/python-miio/blob/feature/dreamef9_support/miio/integrations/vacuum/dreame/dreamevacuum_miot.py

To know the rooms ids you have to make a timer in the App at 12:00 selecting all the rooms in a specific order and disable it.
Then you call the function "get_rooms_ids_from_timers" that return the ids of the rooms in the same order you have specified.
So you can associate your rooms with your ids.
I see that if a new room is discovered the IDs could change.... But this is very uncommon! ;-)

Then you can use:
start_clean_rooms rooms_params
where the argument rooms_params is something like this [[1,1,2,1]] for one room or like this [[1,1,2,1],[2,1,2,1],...] for more.
The number in order are: roomid, repeats, powerlevel, waterlevel.
'''

'''
Патченная dreamevacuum_miot.py лежит так же в settings/dreamevacuum_miot.py.pathched
'''

MARVIN_IP = "192.168.88.105"

# Get token:
# miiocli cloud list

# Get room ids:
#miiocli dreamevacuum --ip 192.168.88.105 --token 58687464486779424d7a72626e545979 get_rooms_ids_from_timers

#[roomid,repeats,powerlevel,waterlevel]
BEDROOM = [[1,1,1,3]]
CORRIDOR_CARPET = [[4,2,3,3]]


