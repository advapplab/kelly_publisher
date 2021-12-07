
import datetime
import time
import string
import threading

from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent
import wisepaasdatahubedgesdk.Common.Constants as constant
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, MQTTOptions, DCCSOptions, EdgeData, EdgeTag, EdgeStatus, EdgeDeviceStatus, EdgeConfig, NodeConfig, DeviceConfig, AnalogTagConfig, DiscreteTagConfig, TextTagConfig
from wisepaasdatahubedgesdk.Common.Utils import RepeatedTimer

NODE_ID = '444cbfad-250c-4243-a14f-5ea956339702'
DCCS_KEY = "a56a8afb7d6c9595a1d838a6d95c2dlb"
DCCS_URL = "http://api-dccs-ensaas.aiot.twcc.ai/"


def on_connected(edgeAgent, isConnected):
    print("connected !")
    config = __generateConfig()
    _edgeAgent.uploadConfig(action = constant.ActionType['Create'], edgeConfig = config)
    
def on_disconnected(edgeAgent, isDisconnected):
    print("disconnected !")

def edgeAgent_on_message(agent, messageReceivedEventArgs):
    print("edgeAgent_on_message !")

def __sendData():
    data = __generateData()
    _edgeAgent.sendData(data)



def __generateData():
    edgeData = EdgeData()
    deviceId = 'Device1'
    tagName = 'DTag1'
    value = 1
    tag = EdgeTag(deviceId, tagName, value)
    edgeData.tagList.append(tag)

    return edgeData

def __generateConfig():
  config = EdgeConfig()
  deviceConfig = DeviceConfig(id = 'Device1',
                                name = 'Device1',
                                description = 'Device1',
                                deviceType = 'Smart Device1',
                                retentionPolicyName = '')

  discrete = DiscreteTagConfig(name = 'DTag1',
                                description = 'DTag1',
                                readOnly = False,
                                arraySize = 0,
                                state0 = 'Stop',
                                state1 = 'Start')

  deviceConfig.discreteTagList.append(discrete)

  config.node.deviceList.append(deviceConfig)
  return config

if __name__ == '__main__':

    _edgeAgent = None
    edgeAgentOptions = EdgeAgentOptions(nodeId = NODE_ID)
    edgeAgentOptions.connectType = constant.ConnectType['DCCS']
    dccsOptions = DCCSOptions(apiUrl = DCCS_URL, credentialKey = DCCS_KEY)
    edgeAgentOptions.DCCS = dccsOptions
    _edgeAgent = EdgeAgent(edgeAgentOptions)
    _edgeAgent.on_connected = on_connected
    _edgeAgent.on_disconnected = on_disconnected
    _edgeAgent.on_message = edgeAgent_on_message

    _edgeAgent.connect()

    time.sleep(5)  # Waiting for connection to be established

    __sendData()
    time.sleep(1)
    _edgeAgent.disconnect()