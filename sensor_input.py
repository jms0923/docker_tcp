import json

class sensing:
    def __init__(self):
        # 센서 명 선언.
        self.sen_01 = 'sensor_01'
        self.sen_02 = 'sensor_02'
        self.sen_03 = 'sensor_03'
        self.listSensorName = []
        self.listSensorValue = []

        self.listSensorName.append(self.sen_01)
        self.listSensorName.append(self.sen_02)
        self.listSensorName.append(self.sen_03)

    def sensing(self):
        # 센싱 값 입력 받음.
        for i in range(len(self.listSensorName)):
            print('plz enter ' + self.listSensorName[i] + ' data : ', end='')
            self.listSensorValue.append(input())

        jsonStr = self.makeJsonStr(self.listSensorName, self.listSensorValue)

        return jsonStr

    # json object로 만들어줌.
    def makeJsonStr(self, listSensorName, listSensorValue):
        strJson = '{'
        for i in range(len(listSensorName)):
            strJson += '"' + listSensorName[i] + '":"' + listSensorValue[i] + '"'
            if i < len(listSensorName) - 1:
                strJson += ','
            else:
                strJson += '}'
        # print(strJson)
        # jsonObj = json.loads(strJson)

        return strJson
