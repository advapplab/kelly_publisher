
import datetime
import pandas as pd

from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, MQTTOptions, DCCSOptions, NodeConfig, EdgeConfig
from wisepaasdatahubedgesdk.Model.Edge import DeviceConfig, AnalogTagConfig, EdgeData, EdgeTag, TextTagConfig
import wisepaasdatahubedgesdk.Common.Constants as constant


def scada_conn (scada_id, device_id, device_name):

    # TODO: tobe comfirm
    # datahub
    DHB_MQTT_HOST = '10.10.0.14'
    DHB_MQTT_PORT = 1883
    DHB_MQTT_USER = "6d657c0a-7fc9-44be-b220-819efb23fbdb:403e3cd7-92ef-457b-9309-64970864bde5"
    DHB_MQTT_PASS = "u3s9tqk0bvn9sklt6dr8j1jpe9"
    
    options = EdgeAgentOptions(
        reconnectInterval = 1, # MQTT reconnect interval seconds
        nodeId = scada_id, # Getting from SCADA portal
        deviceId = device_id, # If type is Device, DeviceId must be filled
        type = constant.EdgeType['Gateway'], # Choice your edge is Gateway or Device, Default is Gateway
        heartbeat = 60, # Default is 60 seconds
        dataRecover = False, # Need to recover data or not when disconnected
        connectType = constant.ConnectType['MQTT'], # Connection type (DCCS, MQTT), default is DCCS
        
        MQTT = MQTTOptions( # If connectType is MQTT, must fill this options
            hostName = DHB_MQTT_HOST,
            port = DHB_MQTT_PORT,
            userName = DHB_MQTT_USER,
            password = DHB_MQTT_PASS,
            protocalType = constant.Protocol['TCP'] # MQTT protocal (TCP, Websocket), default is TCP
        )
    )

    edgeAgent = EdgeAgent( options = options )
    edgeAgent.connect()
    
    return edgeAgent

def scada_client (data_dict):

    # TODO
    output_df = pd.DataFrame(list(data_dict.items()),columns = ['features','values']).T

    
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
    deviceConfig = DeviceConfig(id = device_id,
                                name = device_name,
                                #comPortNumber = None,
                                deviceType = 'Device Type',
                                #description = 'w46 Device',
                                description = device_name
                                #ip = None,
                                #port = None
                                )
    config.node.deviceList.append(deviceConfig)

    # print('scada session #4')
    for feature in list(output_df):
    #     textTag = TextTagConfig(name = feature ,
    #                             description = feature ,
    #                             readOnly = True, 
    #                             arraySize = 0)
        analogTag = AnalogTagConfig(name = feature,
                                    description = feature,
                                    readOnly = False,
                                    arraySize = 0,
                                    spanHigh = 100000000000000000000000000000,
                                    spanLow = -100000000000,
                                    engineerUnit = '',
                                    #engineerUnit = None,
                                    integerDisplayFormat = 30,
                                    fractionDisplayFormat = 40
                                    )

        config.node.deviceList[0].analogTagList.append(analogTag)

    # TODO: command when config get ready
    result = edgeAgent.uploadConfig(constant.ActionType['Create'], edgeConfig = config)


    #print(output_df)
    edgeData = EdgeData()
    for feature in list(output_df):
        #edgeData = EdgeData()
        deviceID = device_id
        tagName = feature
        #print("===================================")
        #print(output_df[feature].tail(1).values[0])
        value = float(output_df[feature].tail(1).values[0])
        value = "%.2f" % round(value, 2)
        
    #         print(value)
        tag = EdgeTag(deviceID,tagName,value)
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

    print(datetime.datetime.now(), '|',
            inspect.getframeinfo(inspect.currentframe()).function, '| send data, edge datetime',
            datetime.datetime.fromtimestamp(data_dict['timestamp']) - datetime.timedelta(hours=8))

    result = edgeAgent.sendData(data=edgeData)


if __name__ == '__main__':

    SCADA_ID = '18c23d90-9a7a-4168-9a3e-6189db45cd1b'
    SCADA_NAME = 'kelly'

    device_id = 'm01'
    device_name = 'machine01'

    edgeAgent = scada_conn (SCADA_ID, device_id, device_name)

    data_dict = {'timestamp': 1638722328,
                 'device_id': device_id,
                 'device_name': device_name,
                 'machine':'machine_01',
                 'pline_output': 0}

    scada_client(data_dict)

    if edgeAgent is not None: edgeAgent.disconnect()
    pass