import decimal
from enum import Enum


class NotConnectedException(Exception):
    pass


class PowerState(Enum):
    ON = 1
    OFF = 0


class Unit(Enum):
    KWH = 'kwh'
    PERCENT = 'pct'
    DEGREE = 'deg'
    KILO_GRAM = 'kg'
    GRAM = 'g'
    KW = 'kw'
    M3HOUR = 'm3h'
    METERSEC = 'm/s'
    NONE = ''


class State(Enum):
    WAIT = 'state_0'
    IGNITION_1 = 'state_1'
    IGNITION__1 = 'state_2'
    IGNITION_2 = 'state_3'
    IGNITION__2 = 'state_4'
    POWER = 'state_5'
    PAUSE = 'state_6'
    HOT_WATER = 'state_7'
    TEMPERATURE_ERROR = 'state_8'
    STOPPED_TEMPERATURE_REACHED = 'state_9'
    SUMMER_STOP = 'state_10'
    ALARM_BURNER_TOO_HOT = 'state_11'
    PLUG_DISCONNECTED = 'state_12'
    FAULT_IGNITION = 'state_13'
    OFF = 'state_14'
    ERROR_BOILER_TEMP_SENSOR = 'state_15'
    ERROR_PHOTO_SENSOR = 'state_16'
    ERROR_BURNER_TEMP_SENSOR = 'state_17'
    ERROR_MOTOR_OUTPUT = 'state_19'
    ERROR_NO_FIRE_OUT_OF_PELLETS = 'state_20'
    STOPPED_BY_EXTERNAL_TEMPERATURE = 'state_22'
    STOPPED_BY_TIMER = 'state_23'
    STOPPED_BY_EXTERNAL_CONTACT = 'state_24'
    STOPPED_BY_WEATHER_COMP = 'state_25'
    FAIL_ON_FAN = 'state_26'
    ERROR_NO_FIRE_ADJUSTMENT_LOW = 'state_27'
    DOOR_OPEN = 'state_28'
    OVERHEAT_AUGER_DISCONNECTED = 'state_29'
    STOPPED_BY_CASCADE = 'state_30'
    COMPRESSOR_FAILURE = 'state_31'

    ALARM_BACKPRESSURE_HIGH = 'state_36'
    ERROR_AIRFLOW_CANNOT_BE_REACHED = 'state_37'
    OUTLET_TEMPERATURE_TOO_HIGH = 'state_38'
    ASH_BOX_NOT_CONNECTED = 'state_39'
    AIRFLOW_CALIBRATION = 'state_40'
    ERROR_BOILER_UNDERPRESSURE = 'state_41'
    ERROR_OXYGEN_SENSOR = 'state_42'
    COMPRESSOR_CLEANING = 'state_43'
    IGNITION_FAILED = 'state_44'
    CONDENSATION_COLLECTOR_FULL = 'state_45'



    @property
    def label(self):
        return STATE_TRANSLATIONS.get(self.value)


STATE_BY_VALUE = {key.value: key for key in State}

# Human-readable translations for `state_*` keys.
STATE_TRANSLATIONS = {
    'state_0': 'Wait',
    'state_1': 'Ignition 1',
    'state_2': 'Ignition 1 (alt)',
    'state_3': 'Ignition 2',
    'state_4': 'Ignition 2 (alt)',
    'state_5': 'Power',
    'state_6': 'Pause',
    'state_7': 'Hot water',
    'state_8': 'Temperature error',
    'state_9': 'Stopped (temperature reached)',
    'state_10': 'Summer stop',
    'state_11': 'Alarm: burner too hot',
    'state_12': 'Plug disconnected',
    'state_13': 'Fault ignition',
    'state_14': 'Off',
    'state_15': 'Error: boiler temp sensor',
    'state_16': 'Error: photo sensor',
    'state_17': 'Error: burner temp sensor',
    'state_19': 'Error: motor output',
    'state_20': 'Error: no fire out of pellets',
    'state_22': 'Stopped by external temperature',
    'state_23': 'Stopped by timer',
    'state_24': 'Stopped by external contact',
    'state_25': 'Stopped by weather compensation',
    'state_26': 'Fail on fan',
    'state_27': 'Error: no fire adjustment low',
    'state_28': 'Door open',
    'state_29': 'Overheat / auger disconnected',
    'state_30': 'Stopped by cascade',
    'state_31': 'Compressor failure',
    'state_36': 'Alarm: backpressure high',
    'state_37': 'Error: airflow cannot be reached',
    'state_38': 'Outlet temperature too high',
    'state_39': 'Ash box not connected',
    'state_40': 'Airflow calibration',
    'state_41': 'Error: boiler underpressure',
    'state_42': 'Error: oxygen sensor',
    'state_43': 'Compressor cleaning',
    'state_44': 'Ignition failed',
    'state_45': 'Condensation collector full',
}


class Substate(Enum):
    PELLETS = 'lng_substate_2'
    STARTPULSE = 'lng_substate_3'
    IGNITION = 'lng_substate_4'
    COOLING_BOILER = 'lng_substate_5'
    COOLING_BURNER = 'lng_substate_6'
    FAN_CLEANING = 'lng_substate_7'
    ASH_REMOVAL = 'lng_substate_8'
    COMPRESSOR_CLEAN_WAIT_VALVE_1 = 'lng_substate_9'
    COMPRESSOR_CLEAN_VALVE_1_ACTIVE = 'lng_substate_10'
    COMPRESSOR_CLEAN_WAIT_VALVE_2 = 'lng_substate_11'
    COMPRESSOR_CLEAN_VALVE_2_ACTIVE = 'lng_substate_12'
    COMPRESSOR_CLEAN_WAIT_VALVE_3 = 'lng_substate_13'
    COMPRESSOR_CLEAN_VALVE_3_ACTIVE = 'lng_substate_14'
    EXTERNAL_CONTACT = 'lng_substate_15'
    OVERRUN = 'lng_substate_16'
    RESIDUAL_HEAT_TO_DHW = 'lng_substate_17'
    VACUUM_TRANSPORT_ACTIVE = 'lng_substate_18'
    AIRFLOW_CALIB_WAIT_SHUTDOWN = 'lng_substate_19'
    AIRFLOW_CALIB_IN_PROGRESS = 'lng_substate_20'
    CALCULATED_EFFICIENCY = 'lng_substate_21'

    @property
    def label(self):
        return SUBSTATE_TRANSLATIONS.get(self.value)


SUBSTATE_BY_VALUE = {key.value: key for key in Substate}

# Human-readable translations for `lng_substate_*` keys.
# Keep translations in the client so presentation layers (Home Assistant)
# don't need to know the internal lng_substate keys.
SUBSTATE_TRANSLATIONS = {
    'lng_substate_2': 'Pellets',
    'lng_substate_3': 'Start pulse',
    'lng_substate_4': 'Ignition',
    'lng_substate_5': 'Cooling (boiler)',
    'lng_substate_6': 'Cooling (burner)',
    'lng_substate_7': 'Fan cleaning',
    'lng_substate_8': 'Ash removal',
    'lng_substate_9': 'Compressor clean: wait valve 1',
    'lng_substate_10': 'Compressor clean: valve 1 active',
    'lng_substate_11': 'Compressor clean: wait valve 2',
    'lng_substate_12': 'Compressor clean: valve 2 active',
    'lng_substate_13': 'Compressor clean: wait valve 3',
    'lng_substate_14': 'Compressor clean: valve 3 active',
    'lng_substate_15': 'External contact',
    'lng_substate_16': 'Overrun',
    'lng_substate_17': 'Residual heat to DHW',
    'lng_substate_18': 'Vacuum transport active',
    'lng_substate_19': 'Airflow calibration (wait shutdown)',
    'lng_substate_20': 'Airflow calibration (in progress)',
    'lng_substate_21': 'Calculated efficiency',
}


class Value:
    def __init__(self, value, unit):
        # Avoid binary-float artifacts: convert floats via str(), otherwise
        # Decimal(float) will contain long repeating decimals.
        if isinstance(value, float):
            dec = decimal.Decimal(str(value))
        else:
            dec = decimal.Decimal(value)
        # Quantize to 2 decimal places for presentation (e.g. 4.90)
        try:
            q = dec.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)
            # Render with at most 2 decimals but strip trailing zeros so
            # integers become `5` (not `5.00`) and `5.50` becomes `5.5`.
            s = format(q, 'f')
            s = s.rstrip('0').rstrip('.')
            if '.' in s:
                self.value = float(s)
            else:
                try:
                    self.value = int(s)
                except Exception:
                    self.value = float(s)
        except Exception:
            # Fallback: keep original decimal if quantize fails
            self.value = dec
        self.unit = unit

    def __eq__(self, other):
        if not isinstance(other, Value):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.value == other.value and self.unit == other.unit

    def __repr__(self):
        return "%s %s" % (self.value, self.unit)

def get_from_list_by_key(lst, key, value):
    for itm in lst:
        if itm.get(key) == value:
            return itm

class ControllerData:
    def __init__(self, data):
        if data['notconnected'] != 0:
            raise NotConnectedException("Furnace/boiler not connected to StokerCloud")
        self.data = data

    def get_sub_item(self, submenu, _id):
        return get_from_list_by_key(self.data[submenu], 'id', _id)

    @property
    def alarm(self):
        return {
            0: PowerState.OFF,
            1: PowerState.ON
        }.get(self.data['miscdata'].get('alarm'))

    @property
    def running(self):
        return {
            0: PowerState.OFF,
            1: PowerState.ON
        }.get(self.data['miscdata'].get('running'))

    @property
    def serial_number(self):
        return self.data['serial']

    @property
    def boiler_temperature_current(self):
        return Value(self.get_sub_item('frontdata', 'boilertemp')['value'], Unit.DEGREE)\

    @property
    def boiler_temperature_requested(self):
        return Value(self.get_sub_item('frontdata', '-wantedboilertemp')['value'], Unit.DEGREE)

    @property
    def boiler_kw(self):
        return Value(self.get_sub_item('boilerdata', '5')['value'], Unit.KW)

    @property
    def state(self):
        return STATE_BY_VALUE.get(self.data['miscdata']['state']['value'])

    @property
    def hotwater_temperature_current(self):
        return Value(self.get_sub_item('frontdata', 'dhw')['value'], Unit.DEGREE)

    @property
    def hotwater_temperature_requested(self):
        return Value(self.get_sub_item('frontdata', 'dhwwanted')['value'], Unit.DEGREE)

    @property
    def consumption_total(self):
        return Value(self.get_sub_item('hopperdata', '4')['value'], Unit.KILO_GRAM)
    
    @property
    def consumption_day(self):
        return Value(self.get_sub_item('hopperdata', '3')['value'], Unit.KILO_GRAM)

    @property
    def hopper_content(self):
        return Value(self.get_sub_item('frontdata', 'hoppercontent')['value'], Unit.KILO_GRAM)

    @property
    def clock(self):
        return self.data['miscdata'].get('clock', {}).get('value')
    
    @property
    def substate(self):
        val = self.data['miscdata'].get('substate', {}).get('value')
        if val is None:
            return None
        return SUBSTATE_BY_VALUE.get(val)
    
    @property
    def state_label(self):
        st = self.state
        if st is None:
            return None
        try:
            return st.label
        except Exception:
            return str(st)
        
    @property
    def substatesecs(self):
        return self.data['miscdata'].get('substatesecs', {}).get('value')

    @property
    def output(self):
        val = self.data['miscdata'].get('output')
        if val is None:
            return None
        return Value(val, Unit.KW)

    @property
    def output_pct(self):
        val = self.data['miscdata'].get('outputpct')
        if val is None:
            return None
        return Value(val, Unit.PERCENT)

    @property
    def hopper_distance(self):
        return self.data['miscdata'].get('hopperdistance')

    @property
    def hopper_distance_max(self):
        return self.data['miscdata'].get('hopper.distance_max')
