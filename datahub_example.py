import datetime
import time
import string
import random
import threading

from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent
import wisepaasdatahubedgesdk.Common.Constants as constant
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, MQTTOptions, DCCSOptions, EdgeData, EdgeTag, EdgeStatus, EdgeDeviceStatus, EdgeConfig, NodeConfig, DeviceConfig, AnalogTagConfig, DiscreteTagConfig, TextTagConfig
from wisepaasdatahubedgesdk.Common.Utils import RepeatedTimer


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


def __generateBatchData():    # send data in batch for high frequency data
  array = []
  for n in range(1, 10):
    edgeData = EdgeData()
    for i in range(1, 1 + 1):
      for j in range(1, 1 + 1):
        deviceId = 'Device' + str(i)
        tagName = 'ATag' + str(j)
        value = random.uniform(0, 100)
        tag = EdgeTag(deviceId, tagName, value)
        edgeData.tagList.append(tag)
      for j in range(1, 1 + 1):
        deviceId = 'Device' + str(i)
        tagName = 'DTag' + str(j)
        value = random.randint(0,99)
        value = value % 2
        tag = EdgeTag(deviceId, tagName, value)
        edgeData.tagList.append(tag)
      for j in range(1, 1 + 1):
        deviceId = 'Device' + str(i)
        tagName = 'TTag' + str(j)
        value = random.uniform(0, 100)
        value = 'TEST ' + str(value)
        tag = EdgeTag(deviceId, tagName, value)
        edgeData.tagList.append(tag)
    array.append(edgeData)
  return array

def __generateData():
  edgeData = EdgeData()
  for i in range(1, 1 + 1):
    for j in range(1, 1 + 1):
      deviceId = 'Device' + str(i)
      tagName = 'ATag' + str(j)
      value = random.uniform(0, 100)
      tag = EdgeTag(deviceId, tagName, value)
      edgeData.tagList.append(tag)
    for j in range(1, 1 + 1):
      deviceId = 'Device' + str(i)
      tagName = 'DTag' + str(j)
      value = random.randint(0,99)
      value = value % 2
      tag = EdgeTag(deviceId, tagName, value)
      edgeData.tagList.append(tag)
    for j in range(1, 1 + 1):
      deviceId = 'Device' + str(i)
      tagName = 'TTag' + str(j)
      value = random.uniform(0, 100)
      value = 'TEST ' + str(value)
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
  
  analog = AnalogTagConfig(name = 'ATag1',
    description = 'ATag1',
    readOnly = False,
    arraySize = 0,
    spanHigh = 1000,
    spanLow = 0,
    engineerUnit = '',
    integerDisplayFormat = 4,
    fractionDisplayFormat = 2)
  deviceConfig.analogTagList.append(analog)

  discrete = DiscreteTagConfig(name = 'DTag1',
    description = 'DTag1',
    readOnly = False,
    arraySize = 0,
    state0 = 'Stop',
    state1 = 'Start')
  deviceConfig.discreteTagList.append(discrete)
  
  text = TextTagConfig(name = 'TTag1',
    description = 'TTag1',
    readOnly = False,
    arraySize = 0)
  deviceConfig.textTagList.append(text)

  config.node.deviceList.append(deviceConfig)
  return config


_edgeAgent = None
edgeAgentOptions = EdgeAgentOptions(nodeId = '444cbfad-250c-4243-a14f-5ea956339702')
edgeAgentOptions.connectType = constant.ConnectType['DCCS']
dccsOptions = DCCSOptions(apiUrl = 'http://api-dccs-ensaas.aiot.twcc.ai/', credentialKey = 'a56a8afb7d6c9595a1d838a6d95c2dlb')
edgeAgentOptions.DCCS = dccsOptions
_edgeAgent = EdgeAgent(edgeAgentOptions)
_edgeAgent.on_connected = on_connected
_edgeAgent.on_disconnected = on_disconnected
_edgeAgent.on_message = edgeAgent_on_message

_edgeAgent.connect()

time.sleep(5)  # Waiting for connection to be established

for i in range(1, 600):
    __sendData()
    time.sleep(1)