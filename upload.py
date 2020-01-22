import configparser
import os
import requests
from requests_toolbelt.multipart import encoder


index = 0
def printProcess(msg):
    global index
    index=index+1
    print('============:'+str(index) + '.'+msg)
#读取配置
printProcess('读取配置文件')
config = configparser.ConfigParser()
config.read('./conf.ini')
srcPath=config['DEFAULT']['srcPath']
pgyConf = config['PGYER']
pgyUKey=pgyConf['uKey']
pgyApiKey=pgyConf['apiKey']
installPwd = pgyConf['installPwd']



def build():
    #执行打包命令
    printProcess('打包')
    os.system(srcPath +'/gradlew')
    apkPath = srcPath +'/app/build/outputs/apk/debug/app-debug.apk'
    return apkPath

def uploadApp(path):
#上传apk到蒲公英
    printProcess('上传开始')
    headers = {
        "enctype":"multipart/form-data"
    }
    params={
        "_api_key": pgyApiKey,
        "buildInstallType":2,
        "buildPassword":installPwd
        }
    files={
        "file": open(path, 'rb'),
    }

    response = requests.post('https://www.pgyer.com/apiv2/app/upload',data=params,files=files, headers=headers)
    printProcess('上传完成')
    return response.text

path = build()
result = uploadApp(path)


