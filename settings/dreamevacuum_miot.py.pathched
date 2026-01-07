"""Dreame Vacuum."""

import logging
from enum import Enum
from typing import Dict, Optional, List

import click

from miio.click_common import command, format_output, LiteralParamType
from miio.exceptions import DeviceException
from miio.miot_device import DeviceStatus as DeviceStatusContainer
from miio.miot_device import MiotDevice, MiotMapping
from miio.utils import deprecated

_LOGGER = logging.getLogger(__name__)


DREAME_1C  = "dreame.vacuum.mc1808"
DREAME_F9  = "dreame.vacuum.p2008"
DREAME_D9  = "dreame.vacuum.p2009"
DREAME_Z10_PRO = "dreame.vacuum.p2028"


_DREAME_1C_MAPPING: MiotMapping = {
    # https://home.miot-spec.com/spec/dreame.vacuum.mc1808
    "battery_level": {"siid": 2, "piid": 1},
    "charging_state": {"siid": 2, "piid": 2},
    "device_fault": {"siid": 3, "piid": 1},
    "device_status": {"siid": 3, "piid": 2},
    "brush_left_time": {"siid": 26, "piid": 1},
    "brush_life_level": {"siid": 26, "piid": 2},
    "filter_life_level": {"siid": 27, "piid": 1},
    "filter_left_time": {"siid": 27, "piid": 2},
    "brush_left_time2": {"siid": 28, "piid": 1},
    "brush_life_level2": {"siid": 28, "piid": 2},
    "operating_mode": {"siid": 18, "piid": 1},
    "cleaning_mode": {"siid": 18, "piid": 6},
    "delete_timer": {"siid": 18, "piid": 8},
    "cleaning_time": {"siid": 18, "piid": 2},
    "cleaning_area": {"siid": 18, "piid": 4},
    "first_clean_time": {"siid": 18, "piid": 12},
    "total_clean_time": {"siid": 18, "piid": 13},
    "total_clean_times": {"siid": 18, "piid": 14},
    "total_clean_area": {"siid": 18, "piid": 15},
    "life_sieve": {"siid": 19, "piid": 1},
    "life_brush_side": {"siid": 19, "piid": 2},
    "life_brush_main": {"siid": 19, "piid": 3},
    "dnd_timer_enable": {"siid": 20, "piid": 1},
    "dnd_start_time": {"siid": 20, "piid": 2},
    "dnd_stop_time": {"siid": 20, "piid": 3},
    "deg": {"siid": 21, "piid": 1, "access": ["write"]},
    "speed": {"siid": 21, "piid": 2, "access": ["write"]},
    "map_view": {"siid": 23, "piid": 1},
    "frame_info": {"siid": 23, "piid": 2},
    "volume": {"siid": 24, "piid": 1},
    "voice_package": {"siid": 24, "piid": 3},
    "timezone": {"siid": 25, "piid": 1},
    "home": {"siid": 2, "aiid": 1},
    "locate": {"siid": 17, "aiid": 1},
    "start_clean": {"siid": 3, "aiid": 1},
    "stop_clean": {"siid": 3, "aiid": 2},
    "reset_mainbrush_life": {"siid": 26, "aiid": 1},
    "reset_filter_life": {"siid": 27, "aiid": 1},
    "reset_sidebrush_life": {"siid": 28, "aiid": 1},
    "move": {"siid": 21, "aiid": 1},
    "play_sound": {"siid": 24, "aiid": 3},
}


_DREAME_F9_MAPPING: MiotMapping = {
    # https://home.miot-spec.com/spec/dreame.vacuum.p2008
    # https://home.miot-spec.com/spec/dreame.vacuum.p2009
    "battery_level": {"siid": 3, "piid": 1},
    "charging_state": {"siid": 3, "piid": 2},
    "device_fault": {"siid": 2, "piid": 2},
    "device_status": {"siid": 2, "piid": 1},
    "brush_left_time": {"siid": 9, "piid": 1},
    "brush_life_level": {"siid": 9, "piid": 2},
    "filter_life_level": {"siid": 11, "piid": 1},
    "filter_left_time": {"siid": 11, "piid": 2},
    "brush_left_time2": {"siid": 10, "piid": 1},
    "brush_life_level2": {"siid": 10, "piid": 2},
    "operating_mode": {"siid": 4, "piid": 1},
    "cleaning_mode": {"siid": 4, "piid": 4},
    "delete_timer": {"siid": 18, "piid": 8},
    "dnd_timer_enable": {"siid": 5, "piid": 1},
    "dnd_start_time": {"siid": 5, "piid": 2},
    "dnd_stop_time": {"siid": 5, "piid": 3},
    "cleaning_time": {"siid": 4, "piid": 2},
    "cleaning_area": {"siid": 4, "piid": 3},
    "first_clean_time": {"siid": 12, "piid": 1},
    "total_clean_time": {"siid": 12, "piid": 2},
    "total_clean_times": {"siid": 12, "piid": 3},
    "total_clean_area": {"siid": 12, "piid": 4},
    "map_view": {"siid": 6, "piid": 1},
    "frame_info": {"siid": 6, "piid": 2},
    "volume": {"siid": 7, "piid": 1},
    "voice_package": {"siid": 7, "piid": 2},
    "water_flow": {"siid": 4, "piid": 5},
    "water_box_carriage_status": {"siid": 4, "piid": 6},
    "timezone": {"siid": 8, "piid": 1},
    "home": {"siid": 3, "aiid": 1},
    "locate": {"siid": 7, "aiid": 1},
    "start_clean": {"siid": 4, "aiid": 1},
    "stop_clean": {"siid": 4, "aiid": 2},
    "reset_mainbrush_life": {"siid": 9, "aiid": 1},
    "reset_filter_life": {"siid": 11, "aiid": 1},
    "reset_sidebrush_life": {"siid": 10, "aiid": 1},
    "move": {"siid": 21, "aiid": 1},
    "play_sound": {"siid": 7, "aiid": 2},
}


_DREAME_Z10_PRO_MAPPING: MiotMapping = {
    # https://home.miot-spec.com/spec/dreame.vacuum.p2028
    "battery_level": {"siid": 3, "piid": 1},
    "charging_state": {"siid": 3, "piid": 2},
    "device_fault": {"siid": 2, "piid": 2},
    "device_status": {"siid": 2, "piid": 1},
    "brush_left_time": {"siid": 9, "piid": 1},
    "brush_life_level": {"siid": 9, "piid": 2},
    "filter_life_level": {"siid": 11, "piid": 1},
    "filter_left_time": {"siid": 11, "piid": 2},
    "brush_left_time2": {"siid": 10, "piid": 1},
    "brush_life_level2": {"siid": 10, "piid": 2},    
    "operating_mode": {"siid": 4, "piid": 1},
    "cleaning_mode": {"siid": 4, "piid": 4}, 
    "dnd_timer_enable": {"siid": 5, "piid": 1},
    "dnd_start_time": {"siid": 5, "piid": 2},
    "dnd_stop_time": {"siid": 5, "piid": 3},          
    "cleaning_time": {"siid": 4, "piid": 2},
    "cleaning_area": {"siid": 4, "piid": 3},
    "first_clean_time": {"siid": 12, "piid": 1},
    "total_clean_time": {"siid": 12, "piid": 2},
    "total_clean_times": {"siid": 12, "piid": 3},
    "total_clean_area": {"siid": 12, "piid": 4},    
    "map_view": {"siid": 6, "piid": 1}, 
    "frame_info": {"siid": 6, "piid": 2},
    "volume": {"siid": 7, "piid": 1},
    "voice_package": {"siid": 7, "piid": 2}, 
    "water_flow": {"siid": 4, "piid": 5},           
    "water_box_carriage_status": {"siid": 4, "piid": 6},
    "timezone": {"siid": 8, "piid": 1}, 
    "timer_clean": {"siid": 8, "piid": 2},     
    "emptybase_auto": {"siid": 15, "piid": 1},
    "emptybase_times": {"siid": 15, "piid": 2},        
    "emptybase_enable": {"siid": 15, "piid": 3},   
    "home": {"siid": 3, "aiid": 1},
    "locate": {"siid": 7, "aiid": 1},
    "start_clean": {"siid": 4, "aiid": 1},
    "stop_clean": {"siid": 4, "aiid": 2},
    "start_clean_extend": {"siid": 4, "aiid": 1},
    "delete_timer": {"siid": 8, "aiid": 1},      
    "reset_mainbrush_life": {"siid": 9, "aiid": 1},
    "reset_filter_life": {"siid": 11, "aiid": 1},
    "reset_sidebrush_life": {"siid": 10, "aiid": 1},
    "play_sound": {"siid": 7, "aiid": 2},
}

MIOT_MAPPING: Dict[str, MiotMapping] = {
    DREAME_1C:  _DREAME_1C_MAPPING,
    DREAME_F9:  _DREAME_F9_MAPPING,
    DREAME_D9:  _DREAME_F9_MAPPING,
    DREAME_Z10_PRO: _DREAME_Z10_PRO_MAPPING,
}


class FormattableEnum(Enum):
    def __str__(self):
        return f"{self.name}"


class ChargingState(FormattableEnum):
    Charging = 1
    Discharging = 2
    Charging2 = 4
    GoCharging = 5


class CleaningModeDreame1C(FormattableEnum):
    Quiet = 0
    Default = 1
    Medium = 2
    Strong = 3


class CleaningModeDreameF9(FormattableEnum):
    Quiet = 0
    Standart = 1
    Strong = 2
    Turbo = 3


class OperatingMode(FormattableEnum):    
    Paused = 1
    Cleaning = 2
    GoCharging = 3
    Charging = 6
    ManualCleaning = 13
    Sleeping = 14
    ManualPaused = 17
    RoomCleaning = 18
    ZoneCleaning = 19
           

class FaultStatus(FormattableEnum):
    NoFaults = 0


class DeviceStatus(FormattableEnum):     
    Sweeping = 1
    Idle = 2
    Paused = 3
    Error = 4
    GoCharging = 5
    Charging = 6
    Mopping = 7
    ManualSweeping = 13


class WaterFlow(FormattableEnum):
    Low = 1
    Medium = 2
    High = 3


def _enum_as_dict(cls):
    return {x.name: x.value for x in list(cls)}


def _get_cleaning_mode_enum_class(model):
    """Return cleaning mode enum class for model if found or None."""
    if model == DREAME_1C:
        return CleaningModeDreame1C
    elif model in [DREAME_F9, DREAME_D9, DREAME_Z10_PRO]:
        return CleaningModeDreameF9


class DreameVacuumStatus(DeviceStatusContainer):
    def __init__(self, data, model):
        """
        data - device status dictionary
        model - device model name
        """
        self.data = data
        self.model = model

    @property
    def battery_level(self) -> str:
        return self.data["battery_level"]

    @property
    def brush_left_time(self) -> str:
        return self.data["brush_left_time"]

    @property
    def brush_left_time2(self) -> str:
        return self.data["brush_left_time2"]

    @property
    def brush_life_level2(self) -> str:
        return self.data["brush_life_level2"]

    @property
    def brush_life_level(self) -> str:
        return self.data["brush_life_level"]

    @property
    def filter_left_time(self) -> str:
        return self.data["filter_left_time"]

    @property
    def filter_life_level(self) -> str:
        return self.data["filter_life_level"]

    @property
    def device_fault(self) -> Optional[FaultStatus]:
        try:
            return FaultStatus(self.data["device_fault"])
        except ValueError:
            _LOGGER.error("Unknown FaultStatus (%s)", self.data["device_fault"])
            return None

    @property
    def charging_state(self) -> Optional[ChargingState]:
        try:
            return ChargingState(self.data["charging_state"])
        except ValueError:
            _LOGGER.error("Unknown ChargingStats (%s)", self.data["charging_state"])
            return None

    @property
    def operating_mode(self) -> Optional[OperatingMode]:
        try:
            return OperatingMode(self.data["operating_mode"])
        except ValueError:
            _LOGGER.error("Unknown OperatingMode (%s)", self.data["operating_mode"])
            return None

    @property
    def device_status(self) -> Optional[DeviceStatus]:
        try:
            return DeviceStatus(self.data["device_status"])
        except TypeError:
            _LOGGER.error("Unknown DeviceStatus (%s)", self.data["device_status"])
            return None

    @property
    def dnd_timer_enable(self) -> str:
        return self.data["dnd_timer_enable"]

    @property
    def dnd_start_time(self) -> str:
        return self.data["dnd_start_time"]

    @property
    def dnd_stop_time(self) -> str:
        return self.data["dnd_stop_time"]

    @property
    def map_view(self) -> str:
        return self.data["map_view"]

    @property
    def volume(self) -> str:
        return self.data["volume"]

    @property
    def voice_package(self) -> str:
        return self.data["voice_package"]

    @property
    def timezone(self) -> str:
        return self.data["timezone"]

    @property
    def timer_clean(self) -> str:
        return self.data["timer_clean"]
        
    @property
    def emptybase_auto(self) -> str:
        if self.model != DREAME_Z10_PRO:
            _LOGGER.error(f"Autoempty base not available in ({self.model})")
            return None        
        return self.data["emptybase_auto"]

    @property
    def emptybase_times(self) -> str:
        if self.model != DREAME_Z10_PRO:
            _LOGGER.error(f"Autoempty base not available in ({self.model})")
            return None     
        return self.data["emptybase_times"]

    @property
    def emptybase_enable(self) -> str:
        if self.model != DREAME_Z10_PRO:
            _LOGGER.error(f"Autoempty base not available in ({self.model})")
            return None   
        return self.data["emptybase_enable"]
        
    @property
    def cleaning_time(self) -> str:
        return self.data["cleaning_time"]

    @property
    def cleaning_area(self) -> str:
        return self.data["cleaning_area"]

    @property
    def first_clean_time(self) -> str:
        return self.data["first_clean_time"]

    @property
    def total_clean_time(self) -> str:
        return self.data["total_clean_time"]

    @property
    def total_clean_times(self) -> str:
        return self.data["total_clean_times"]

    @property
    def total_clean_area(self) -> str:
        return self.data["total_clean_area"]

    @property
    def cleaning_mode(self):
        cleaning_mode = self.data["cleaning_mode"]
        cleaning_mode_enum_class = _get_cleaning_mode_enum_class(self.model)

        if not cleaning_mode_enum_class:
            _LOGGER.error(f"Unknown model for cleaning mode ({self.model})")
            return None
        try:
            return cleaning_mode_enum_class(cleaning_mode)
        except ValueError:
            _LOGGER.error(f"Unknown CleaningMode ({cleaning_mode})")
            return None

    @property
    def life_sieve(self) -> Optional[str]:
        return self.data.get("life_sieve")

    @property
    def life_brush_side(self) -> Optional[str]:
        return self.data.get("life_brush_side")

    @property
    def life_brush_main(self) -> Optional[str]:
        return self.data.get("life_brush_main")

    # TODO: get/set water flow for Dreame 1C
    @property
    def water_flow(self) -> Optional[WaterFlow]:
        try:
            water_flow = self.data["water_flow"]
        except KeyError:
            return None
        try:
            return WaterFlow(water_flow)
        except ValueError:
            _LOGGER.error("Unknown WaterFlow (%s)", self.data["water_flow"])
            return None

    @property
    def is_water_box_carriage_attached(self) -> Optional[bool]:
        """Return True if water box carriage (mop) is installed, None if sensor not
        present."""
        if "water_box_carriage_status" in self.data:
            return self.data["water_box_carriage_status"] == 1
        return None


class DreameVacuum(MiotDevice):
    _supported_models = [
        DREAME_1C,
        DREAME_D9,
        DREAME_F9,
        DREAME_Z10_PRO,        
    ]
    _mappings = MIOT_MAPPING

    @command(
        default_output=format_output(
            "\n",
            "Battery level: {result.battery_level}\n"
            "Brush life level: {result.brush_life_level}\n"
            "Brush left time: {result.brush_left_time}\n"
            "Charging state: {result.charging_state}\n"
            "Cleaning mode: {result.cleaning_mode}\n"
            "Device fault: {result.device_fault}\n"
            "Device status: {result.device_status}\n"
            "Filter left level: {result.filter_left_time}\n"
            "Filter life level: {result.filter_life_level}\n"
            "Life brush main: {result.life_brush_main}\n"
            "Life brush side: {result.life_brush_side}\n"
            "Life sieve: {result.life_sieve}\n"
            "Map view: {result.map_view}\n"
            "Operating mode: {result.operating_mode}\n"
            "Side cleaning brush left time: {result.brush_left_time2}\n"
            "Side cleaning brush life level: {result.brush_life_level2}\n"            
            "Time zone: {result.timezone}\n"   
            "Timer cleaning: {result.timer_clean}\n"                        
            "Empty Base Auto: {result.emptybase_auto}\n"
            "Empty Base Clean Times: {result.emptybase_times}\n"
            "Empty Base Enable: {result.emptybase_enable}\n"                                                
            "DND Timer enabled: {result.dnd_timer_enable}\n"
            "DND Timer start time: {result.dnd_start_time}\n"
            "DND Timer stop time: {result.dnd_stop_time}\n"
            "Voice package: {result.voice_package}\n"
            "Volume: {result.volume}\n"
            "Water flow: {result.water_flow}\n"
            "Water box attached: {result.is_water_box_carriage_attached} \n"
            "Cleaning time: {result.cleaning_time}\n"
            "Cleaning area: {result.cleaning_area}\n"
            "First clean time: {result.first_clean_time}\n"
            "Total clean time: {result.total_clean_time}\n"
            "Total clean times: {result.total_clean_times}\n"
            "Total clean area: {result.total_clean_area}\n",
        )
    )
    def status(self) -> DreameVacuumStatus:
        """State of the vacuum."""

        return DreameVacuumStatus(
            {
                prop["did"]: prop["value"] if prop["code"] == 0 else None
                for prop in self.get_properties_for_mapping(max_properties=10)
            },
            self.model,
        )

    # TODO: check the actual limit for this
    MANUAL_ROTATION_MAX = 120
    MANUAL_ROTATION_MIN = -MANUAL_ROTATION_MAX
    MANUAL_DISTANCE_MAX = 300
    MANUAL_DISTANCE_MIN = -300

    @command()
    def start(self) -> None:
        """Start cleaning."""
        return self.call_action("start_clean")

    @command()
    def stop(self) -> None:
        """Stop cleaning."""
        return self.call_action("stop_clean")

    @command()
    def home(self) -> None:
        """Return to home."""
        return self.call_action("home")

    @command()
    def identify(self) -> None:
        """Locate the device (i am here)."""
        return self.call_action("locate")

    @command()
    def reset_mainbrush_life(self) -> None:
        """Reset main brush life."""
        return self.call_action("reset_mainbrush_life")

    @command()
    def reset_filter_life(self) -> None:
        """Reset filter life."""
        return self.call_action("reset_filter_life")

    @command()
    def reset_sidebrush_life(self) -> None:
        """Reset side brush life."""
        return self.call_action("reset_sidebrush_life")

    @command()
    def play_sound(self) -> None:
        """Play sound."""
        return self.call_action("play_sound")

    @command()
    def fan_speed(self):
        """Return fan speed."""
        dreame_vacuum_status = self.status()
        fanspeed = dreame_vacuum_status.cleaning_mode
        if not fanspeed or fanspeed.value == -1:
            _LOGGER.warning("Unknown fanspeed value received")
            return
        return {fanspeed.name: fanspeed.value}

    @command(click.argument("speed", type=int))
    def set_fan_speed(self, speed: int):
        """Set fan speed.

        :param int speed: Fan speed to set
        """
        fanspeeds_enum = _get_cleaning_mode_enum_class(self.model)
        fanspeed = None
        if not fanspeeds_enum:
            return
        try:
            fanspeed = fanspeeds_enum(speed)
        except ValueError:
            _LOGGER.error(f"Unknown fanspeed value passed {speed}")
            return None
        click.echo(f"Setting fanspeed to {fanspeed.name}")
        return self.set_property("cleaning_mode", fanspeed.value)

    @command()
    def fan_speed_presets(self) -> Dict[str, int]:
        """Return dictionary containing supported fan speeds."""
        fanspeeds_enum = _get_cleaning_mode_enum_class(self.model)
        if not fanspeeds_enum:
            return {}
        return _enum_as_dict(fanspeeds_enum)

    @command()
    def waterflow(self):
        """Get water flow setting."""
        dreame_vacuum_status = self.status()
        waterflow = dreame_vacuum_status.water_flow
        if not waterflow or waterflow.value == -1:
            _LOGGER.warning("Unknown waterflow value received")
            return
        return {waterflow.name: waterflow.value}

    @command(click.argument("value", type=int))
    def set_waterflow(self, value: int):
        """Set water flow.

        :param int value: Water flow value to set
        """
        mapping = self._get_mapping()
        if "water_flow" not in mapping:
            return None
        waterflow = None
        try:
            waterflow = WaterFlow(value)
        except ValueError:
            _LOGGER.error(f"Unknown waterflow value passed {value}")
            return None
        click.echo(f"Setting waterflow to {waterflow.name}")
        return self.set_property("water_flow", waterflow.value)

    @command()
    def waterflow_presets(self) -> Dict[str, int]:
        """Return dictionary containing supported water flow."""
        mapping = self._get_mapping()
        if "water_flow" not in mapping:
            return {}
        return _enum_as_dict(WaterFlow)

    @command()
    def get_rooms_ids_from_timers(self) -> str:
        """Get rooms ids using the timers defined via the Mi Home App."""
        dreame_vacuum_status = self.status()
        timerstxt = dreame_vacuum_status.timer_clean
        if not timerstxt or timerstxt == "-1":
            _LOGGER.warning("Unknown timers value received")
            return
        timers=timerstxt.split(";")

        found=False    
        for timer in timers:
          prop = timer.split("-")
          timer_id=prop[0]
          timer_en=prop[1]
          timer_time=prop[2]
          timer_days=prop[3]
          timer_rep=prop[4]
          xxx=prop[5]
          timer_power=prop[6]
          timer_water=prop[7]                                                                      
          timer_rooms=prop[8]          
          #print("Timer: "+timer_id+" Time: "+timer_time+" Rooms ids: "+timer_rooms)
          if(str(timer_en)=="0" and str(timer_time)=="12:00"):
            return str(timer_rooms)
            found=True
        if(found==False):
          return "Timer NOT ENABLE with time 12:00 not found. Define it to get the rooms ids."
                   
    @command()
    def start_clean_extend(self, params) -> None:
        """Start cleaning (extended with params)."""
        #print("*******TEST******* CLEAN CALL DISABLED ********")
        print(params)
        return self.call_action("start_clean_extend", params)
 
    @command(click.argument("rooms_par", type=LiteralParamType(), required=True))
    def start_clean_rooms(self, rooms_par: List) -> None:
        """Start room-id cleaning. [[i1,r1,p1,w1],[i2,r2,p2,w2],...]"""
        
        if self.model != DREAME_Z10_PRO:
          raise DeviceException("Room clean by IDs not available in %s", self.model)  
        try:
         roomsToclean=len(rooms_par)  
         if(roomsToclean<1):
          raise DeviceException("One or more rooms must be specified: [[i,r,p,w]...] ")  
         for i in range(roomsToclean):
          if(len(rooms_par[i])!=4):
            raise DeviceException("For each room specify: [roomid,repeats,powerlevel,waterlevel]")           
        except:
         raise DeviceException("Use room clean param in this way: [[roomid,repeats,powerlevel,waterlevel],...]") 
          
        cleantask = []
        for room in rooms_par:
          room_id = room[0]
          repeats = room[1]
          power_lev = room[2]
          water_lev = room[3]
          cleantask.append([room_id,repeats,power_lev,water_lev,rooms_par.index(room) + 1,])
        payload = [
            {"piid": 1,     #work mode
             "value": 18},  #roomclean
            {
                "piid": 10, #clean extend data
                "value": '{"selects": ' + str(cleantask).replace(" ", "") + "}",
            },
        ]
        self.start_clean_extend(payload)

    @command(click.argument("zones_par", type=LiteralParamType(), required=True))
    def start_clean_zones(self, zones_par: List) -> None:
        """Start zone area cleaning. [[x1,y1,x2,y2,r1],[......],...]"""    

        if self.model != DREAME_Z10_PRO:
          raise DeviceException("Zone area clean not available in %s", self.model)   
        try:
         zonesToclean=len(zones_par)  
         if(zonesToclean<1):
          raise DeviceException("One or more zones must be specified: [[x1,y1,x2,y2,r1]...] ")  
         for i in range(zonesToclean):
          if(len(zones_par[i])!=5):
            raise DeviceException("For each zone area specify: [bootom left x,bootom left y,top right x,top right y,repeats]")           
        except:
         raise DeviceException("Use zone area clean param in this way: [[bootom left x,bootom left y,top right x,top right y,repeats],...]") 
          
        cleantask = []  
        for zone in zones_par:
          x1 = zone[0]
          y1 = zone[1]
          x2 = zone[2]
          y2 = zone[3]
          rp = zone[4]          
          cleantask.append([x1,y1,x2,y2,rp])                       
        payload = [
            {"piid": 1,     #work mode
             "value": 19},  #zoneclean
            {
                "piid": 10, #clean extend data
                "value": '{"areas": ' + str(cleantask).replace(" ", "") + "}",
            },
        ]           
        self.start_clean_extend(payload)
        
        
    @command(
        click.argument("distance", default=30, type=int),
    )
    def forward(self, distance: int) -> None:
        """Move forward."""
        if distance < self.MANUAL_DISTANCE_MIN or distance > self.MANUAL_DISTANCE_MAX:
            raise DeviceException(
                "Given distance is invalid, should be [%s, %s], was: %s"
                % (self.MANUAL_DISTANCE_MIN, self.MANUAL_DISTANCE_MAX, distance)
            )
        self.call_action(
            "move",
            [
                {
                    "piid": 1,
                    "value": "0",
                },
                {
                    "piid": 2,
                    "value": f"{distance}",
                },
            ],
        )

    @command(
        click.argument("rotatation", default=90, type=int),
    )
    def rotate(self, rotatation: int) -> None:
        """Rotate vacuum."""
        if (
            rotatation < self.MANUAL_ROTATION_MIN
            or rotatation > self.MANUAL_ROTATION_MAX
        ):
            raise DeviceException(
                "Given rotation is invalid, should be [%s, %s], was %s"
                % (self.MANUAL_ROTATION_MIN, self.MANUAL_ROTATION_MAX, rotatation)
            )
        self.call_action(
            "move",
            [
                {
                    "piid": 1,
                    "value": f"{rotatation}",
                },
                {
                    "piid": 2,
                    "value": "0",
                },
            ],
        )


class DreameVacuumMiot(DreameVacuum):
    @deprecated("DreameVacuumMiot is deprectaed. Use DreameVacuum instead.")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
