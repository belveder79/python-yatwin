from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_params (an instance of <ParamMethod>)

Constants defined here:
    ENDPOINT
    DESCRIPTION
    GET_PARAMETERS
    POST_PARAMETERS
    RETURNS
    METHOD
    FILES

Imports:
    .method_types
    ..parameters
    .constants.permissions
    .constants.methods
"""

ENDPOINT = 'get_params.cgi'
DESCRIPTION = 'get device parameter'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.ALARM_AUDIO,
    parameters.ALARM_HTTP,
    parameters.ALARM_HTTP_URL,
    parameters.ALARM_INPUT_ARMED,
    parameters.ALARM_IOIN_LEVEL,
    parameters.ALARM_IOLINKAGE,
    parameters.ALARM_IOOUT_LEVEL,
    parameters.ALARM_MAIL,
    parameters.ALARM_MOTION_ARMED,
    parameters.ALARM_MOTION_SENSITIVITY,
    parameters.ALARM_NOTE,
    parameters.ALARM_HTTP_PORT,
    parameters.ALARM_PRESETSIT,
    parameters.ALARM_PWD,
    parameters.ALARM_RECORD,
    parameters.ALARM_SCHEDULE_ENABLE,
    parameters.ALARM_SCHEDULE_FRI_0,
    parameters.ALARM_SCHEDULE_FRI_1,
    parameters.ALARM_SCHEDULE_FRI_2,
    parameters.ALARM_SCHEDULE_MON_0,
    parameters.ALARM_SCHEDULE_MON_1,
    parameters.ALARM_SCHEDULE_MON_2,
    parameters.ALARM_SCHEDULE_TUE_0,
    parameters.ALARM_SCHEDULE_TUE_1,
    parameters.ALARM_SCHEDULE_TUE_2,
    parameters.ALARM_SCHEDULE_WED_0,
    parameters.ALARM_SCHEDULE_WED_1,
    parameters.ALARM_SCHEDULE_WED_2,
    parameters.ALARM_SCHEDULE_THU_0,
    parameters.ALARM_SCHEDULE_THU_1,
    parameters.ALARM_SCHEDULE_THU_2,
    parameters.ALARM_SCHEDULE_SAT_0,
    parameters.ALARM_SCHEDULE_SAT_1,
    parameters.ALARM_SCHEDULE_SAT_2,
    parameters.ALARM_SCHEDULE_SUN_0,
    parameters.ALARM_SCHEDULE_SUN_1,
    parameters.ALARM_SCHEDULE_SUN_2,
    parameters.ALARM_SERVER,
    parameters.ALARM_SNAPSHOT,
    parameters.ALARM_TEMPERATURE,
    parameters.ALARM_UPLOAD_INTERVAL,
    parameters.ALARM_USER,
    parameters.DDNS_HOST,
    parameters.DDNS_MODE,
    parameters.DDNS_PROXY_PORT,
    parameters.DDNS_PROXY_SVR,
    parameters.DDNS_PWD,
    parameters.DDNS_SERVICE,
    parameters.DDNS_STATUS,
    parameters.DDNS_USER,
    parameters.DEV2_ALIAS,
    parameters.DEV2_HOST,
    parameters.DEV2_PORT,
    parameters.DEV2_PWD,
    parameters.DEV2_USER,
    parameters.DEV3_ALIAS,
    parameters.DEV3_HOST,
    parameters.DEV3_PORT,
    parameters.DEV3_PWD,
    parameters.DEV3_USER,
    parameters.DEV4_ALIAS,
    parameters.DEV4_HOST,
    parameters.DEV4_PORT,
    parameters.DEV4_PWD,
    parameters.DEV4_USER,
    parameters.DEV5_ALIAS,
    parameters.DEV5_HOST,
    parameters.DEV5_PORT,
    parameters.DEV5_PWD,
    parameters.DEV5_USER,
    parameters.DEV6_ALIAS,
    parameters.DEV6_HOST,
    parameters.DEV6_PORT,
    parameters.DEV6_PWD,
    parameters.DEV6_USER,
    parameters.DEV7_ALIAS,
    parameters.DEV7_HOST,
    parameters.DEV7_PORT,
    parameters.DEV7_PWD,
    parameters.DEV7_USER,
    parameters.DEV8_ALIAS,
    parameters.DEV8_HOST,
    parameters.DEV8_PORT,
    parameters.DEV8_PWD,
    parameters.DEV8_USER,
    parameters.DEV9_ALIAS,
    parameters.DEV9_HOST,
    parameters.DEV9_PORT,
    parameters.DEV9_PWD,
    parameters.DEV9_USER,
    parameters.DHCPEN,
    parameters.DNS1,
    parameters.DNS2,
    parameters.FTP_DIR,
    parameters.FTP_FILENAME,
    parameters.FTP_MODE,
    parameters.FTP_PORT,
    parameters.FTP_PWD,
    parameters.FTP_SVR,
    parameters.FTP_UPLOAD_INTERVAL,
    parameters.FTP_USER,
    parameters.GATEWAY,
    parameters.IP_ADDRESS,
    parameters.MAIL_INET_IP,
    parameters.MAIL_PORT,
    parameters.MAIL_PWD,
    parameters.MAIL_RECEIVER1,
    parameters.MAIL_RECEIVER2,
    parameters.MAIL_RECEIVER3,
    parameters.MAIL_RECEIVER4,
    parameters.MAIL_SENDER,
    parameters.MAIL_SVR,
    parameters.MAIL_USER,
    parameters.MAILSSL,
    parameters.MASK,
    parameters.MOTION_PLAN_1,
    parameters.MOTION_PLAN_2,
    parameters.MOTION_PLAN_3,
    parameters.MOTION_PLAN_4,
    parameters.MOTION_PLAN_5,
    parameters.MOTION_PLAN_6,
    parameters.MOTION_PLAN_7,
    parameters.MOTION_PLAN_8,
    parameters.MOTION_PLAN_9,
    parameters.MOTION_PLAN_10,
    parameters.MOTION_PLAN_11,
    parameters.MOTION_PLAN_12,
    parameters.MOTION_PLAN_13,
    parameters.MOTION_PLAN_14,
    parameters.MOTION_PLAN_15,
    parameters.MOTION_PLAN_16,
    parameters.MOTION_PLAN_17,
    parameters.MOTION_PLAN_18,
    parameters.MOTION_PLAN_19,
    parameters.MOTION_PLAN_20,
    parameters.MOTION_PLAN_21,
    parameters.TIME_NOW,
    parameters.NTP_ENABLE,
    parameters.NTP_SVR,
    parameters.P2P_UPNP_ENABLE,
    parameters.PORT,
    parameters.PPPOE_ENABLE,
    parameters.PPPOE_PWD,
    parameters.PPPOE_USER,
    parameters.RTSP_AUTH_ENABLE,
    parameters.RTSPPWD,
    parameters.RTSPUSER,
    parameters.TIME_ZONE,
    parameters.UPNP_ENABLE,
    parameters.USER1_NAME,
    parameters.USER1_PWD,
    parameters.USER2_NAME,
    parameters.USER2_PWD,
    parameters.USER3_NAME,
    parameters.USER3_PWD,
    parameters.WIFI_AUTHTYPE,
    parameters.WIFI_CHANNEL,
    parameters.WIFI_DEFKEY,
    parameters.WIFI_ENABLE,
    parameters.WIFI_ENCRYPT,
    parameters.WIFI_KEY1,
    parameters.WIFI_KEY1_BITS,
    parameters.WIFI_KEY2,
    parameters.WIFI_KEY2_BITS,
    parameters.WIFI_KEY3,
    parameters.WIFI_KEY3_BITS,
    parameters.WIFI_KEY4,
    parameters.WIFI_KEY4_BITS,
    parameters.WIFI_KEYFORMAT,
    parameters.WIFI_MODE,
    parameters.WIFI_SSID,
    parameters.WIFI_WPA_PSK,
)
PERMISSION = permissions.MANAGER
METHOD = methods.GET
FILES = ()

get_params = method_types.ParamMethod \
(
    endpoint = ENDPOINT,
    description = DESCRIPTION,
    get_parameters = GET_PARAMETERS,
    post_parameters = POST_PARAMETERS,
    returns = RETURNS,
    permission = PERMISSION,
    method = METHOD,
    files = FILES,
)