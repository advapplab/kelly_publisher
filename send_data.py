
import datetime
import pandas as pd

from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, MQTTOptions, DCCSOptions, NodeConfig, EdgeConfig
from wisepaasdatahubedgesdk.Model.Edge import DeviceConfig, AnalogTagConfig, EdgeData, EdgeTag, TextTagConfig
import wisepaasdatahubedgesdk.Common.Constants as constant

# NodeName: dai
# NodeID: 444cbfad-250c-4243-a14f-5ea956339702
# Cre: a56a8afb7d6c9595a1d838a6d95c2dlb
# DCCS URL: http://api-dccs-ensaas.aiot.twcc.ai/

SCADA_ID = '444cbfad-250c-4243-a14f-5ea956339702'
SCADA_NAME = 'kelly'

NODE_NAME = 'dai'
DEVICE_ID = 'm01'
DEVICE_NAME = 'machine01'

DHB_MQTT_HOST = '103.124.74.162'
DHB_MQTT_PORT = 1883
DHB_MQTT_USER = "b8qJj7g4plqa%3A8xen3XV9M7qD:xeCZGRBPLcOLQrUoGHen"
DHB_MQTT_PASS = "xeCZGRBPLcOLQrUoGHen"

DCCS_KEY = "a56a8afb7d6c9595a1d838a6d95c2dlb"
DCCS_URL = "http://api-dccs-ensaas.aiot.twcc.ai/"


def scada_conn ():

    options = EdgeAgentOptions(
        #reconnectInterval = 1, # MQTT reconnect interval seconds
        #nodeId = DEVICE_ID, # Getting from SCADA portal
        #deviceId = DEVICE_ID, # If type is Device, DeviceId must be filled
        #type = constant.EdgeType['Gateway'], # Choice your edge is Gateway or Device, Default is Gateway
        #heartbeat = 60, # Default is 60 seconds
        #dataRecover = False, # Need to recover data or not when disconnected

        # connectType = constant.ConnectType['MQTT'], # Connection type (DCCS, MQTT), default is DCCS    
        # MQTT = MQTTOptions( # If connectType is MQTT, must fill this options
        #     hostName = DHB_MQTT_HOST,
        #     port = DHB_MQTT_PORT,
        #     userName = DHB_MQTT_USER,
        #     password = DHB_MQTT_PASS,
        #     protocalType = constant.Protocol['TCP'] # MQTT protocal (TCP, Websocket), default is TCP
        # )

        connectType = constant.ConnectType['DCCS'],
        DCCS = DCCSOptions(
                apiUrl = DCCS_URL, 
                credentialKey = DCCS_KEY)
    )

    edgeAgent = EdgeAgent( options = options )
    edgeAgent.connect()
    
    return edgeAgent

def scada_client (data_dict):

    config = EdgeConfig()

    # print('scada session #2')
    nodeConfig = NodeConfig(#name = scada_name,
                                #description = 'Machine Name',
                                #description = scada_name,
                                #primaryIP = None,
                                #backupIP = None,
                                #primaryPort = None,
                                #backupPort = None,
                                nodeType = constant.EdgeType['Device']
                                )
    config.node = nodeConfig

    # print('scada session #3')
    deviceConfig = DeviceConfig(id = DEVICE_ID,
                                name = DEVICE_NAME,
                                #comPortNumber = None,
                                deviceType = 'Device Type',
                                #description = 'w46 Device',
                                description = DEVICE_NAME
                                #ip = None,
                                #port = None
                                )
    config.node.deviceList.append(deviceConfig)


    analogTag = AnalogTagConfig(name = 'quantity',
                                description = 'Production quantity',
                                readOnly = False,
                                arraySize = 0,
                                spanHigh = 10000,
                                spanLow = 0,
                                engineerUnit = '',
                                #engineerUnit = None,
                                integerDisplayFormat = 30,
                                fractionDisplayFormat = 40
                                )

    config.node.deviceList[0].analogTagList.append(analogTag)
    edgeAgent.uploadConfig(constant.ActionType['Create'], edgeConfig = config)

    #print(output_df)
    edgeData = EdgeData()


    
    tag = EdgeTag(DEVICE_ID, 'quantity', data_dict['pline_output'])
    edgeData.tagList.append(tag)
    #print("===================================")
    #print(deviceID,tagName,value)
    #print("===================================")
    #print(edgeData)
    #print(len(str(value)))
    #print("===================================")
    #print(tag)
    # print('scada session #5-1')
    #result = edgeAgent.sendData(data=edgeData)
    # print('scada session #5-2')
    #time.sleep(1)

    #     print(datetime.datetime.now(), '|',
    #           inspect.getframeinfo(inspect.currentframe()).function, '| Scada send data')
    edgeData.timestamp = datetime.datetime.fromtimestamp(data_dict['timestamp']) - datetime.timedelta(hours=8)

    #     print('edge datetime', datetime.datetime.fromtimestamp(data_dict['timestamp']) - datetime.timedelta(hours=8))


    result = edgeAgent.sendData(data=edgeData)


if __name__ == '__main__':

    # connect
    edgeAgent = scada_conn ()
    print(edgeAgent.isConnected())
    
    data_dict = dict()
    data_dict['timestamp'] = 1638722328
    data_dict['pline_output'] = 1

    scada_client(data_dict)

    # disconnect
    edgeAgent.disconnect()
    print(edgeAgent.isConnected())