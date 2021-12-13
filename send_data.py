
import datetime
import time
import string
import random
import threading

from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent
import wisepaasdatahubedgesdk.Common.Constants as constant
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, MQTTOptions, DCCSOptions, EdgeData, EdgeTag, EdgeStatus, EdgeDeviceStatus, EdgeConfig, NodeConfig, DeviceConfig, AnalogTagConfig, DiscreteTagConfig, TextTagConfig
from wisepaasdatahubedgesdk.Common.Utils import RepeatedTimer

NODE_ID = '444cbfad-250c-4243-a14f-5ea956339702'
DCCS_KEY = "a56a8afb7d6c9595a1d838a6d95c2dlb"
DCCS_URL = "http://api-dccs-ensaas.aiot.twcc.ai/"
<<<<<<< HEAD
EQU = 'Machine 02'
VALUE = 1
=======
EQU = 'Machine 01'
today = datetime.date.today()
filename = str(today) + '_Vibration.txt'
with open(filename, 'r') as f:
    VALUE  = f.readline()
    VALUE  = int(VALUE )
VALUE = 0
>>>>>>> fd64e6eee4fea060f1fbc6ad22abfa1cc1a5c5c1

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

# def __generateBatchData():    # send data in batch for high frequency data
#   array = []
#   for n in range(1, 10):
#     edgeData = EdgeData()
#     for i in range(1, 1 + 1):
#       for j in range(1, 1 + 1):
#         deviceId = 'Device' + str(i)
#         tagName = 'ATag' + str(j)
#         value = 2
#         tag = EdgeTag(deviceId, tagName, value)
#         edgeData.tagList.append(tag)
#     #   for j in range(1, 1 + 1):
#     #     deviceId = 'Device' + str(i)
#     #     tagName = 'DTag' + str(j)
#     #     value = random.randint(0,99)
#     #     value = value % 2
#     #     tag = EdgeTag(deviceId, tagName, value)
#     #     edgeData.tagList.append(tag)
#     #   for j in range(1, 1 + 1):
#     #     deviceId = 'Device' + str(i)
#     #     tagName = 'TTag' + str(j)
#     #     value = random.uniform(0, 100)
#     #     value = 'TEST ' + str(value)
#     #     tag = EdgeTag(deviceId, tagName, value)
#     #     edgeData.tagList.append(tag)
#     array.append(edgeData)
#   return array

def __generateData():
    edgeData = EdgeData()
    #for i in range(1, 1 + 1):
        #for j in range(1, 1 + 1):
    deviceId = EQU
    tagName = 'ATag'
    value = int(random.uniform(0, 100))
    tag = EdgeTag(deviceId, tagName, VALUE)
    edgeData.tagList.append(tag)
    # for j in range(1, 1 + 1):
    deviceId = EQU
    tagName = 'DTag'
    value = random.randint(0,99)
    value = value % 2
    tag = EdgeTag(deviceId, tagName, VALUE)
    edgeData.tagList.append(tag)

    d01=datetime.datetime.now()
    d01tamp = d01.timestamp()
    d01tamp1 = '{:%Y,%m,%d,%H,%M,%S}'.format(d01)
    dateString = d01tamp1
    dateFormatter = "%Y,%m,%d,%H,%M,%S"
    d1=datetime.datetime.strptime(dateString, dateFormatter)
    d2=d1.timestamp()
    d3=datetime.datetime.fromtimestamp(d2)
    edgeData.timestamp = d3

    print(datetime.datetime.now() - datetime.timedelta(hours=8))
    return edgeData

def __generateConfig():

    config = EdgeConfig()

    deviceConfig = DeviceConfig(id = EQU,
                                name = EQU,
                                description = EQU,
                                deviceType = 'Gearing Machine',
                                retentionPolicyName = '')
    
    analog = AnalogTagConfig(name = 'ATag',
                                description = 'ATag',
                                readOnly = False,
                                arraySize = 0,
                                spanHigh = 1000,
                                spanLow = 0,
                                engineerUnit = '',
                                integerDisplayFormat = 4,
                                fractionDisplayFormat = 2)

    deviceConfig.analogTagList.append(analog)

    discrete = DiscreteTagConfig(name = 'DTag',
                                description = 'DTag1',
                                readOnly = False,
                                arraySize = 0,
                                state0 = 'Stop',
                                state1 = 'Start')
    deviceConfig.discreteTagList.append(discrete)
  
#   text = TextTagConfig(name = 'TTag1',
#     description = 'TTag1',
#     readOnly = False,
#     arraySize = 0)
#   deviceConfig.textTagList.append(text)

    config.node.deviceList.append(deviceConfig)
    return config


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

for i in range(1, 200):
    __sendData()
    time.sleep(1)

# for i in range(1, 2):
    # __sendData()
    # time.sleep(1)