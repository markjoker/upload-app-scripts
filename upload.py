import configparser
import os
import requests

#读取配置
config = configparser.ConfigParser()
config.read('./conf.ini')
srcPath=config['DEFAULT']['srcPath']
pgyConf = config['PGYER']
pgyUKey=pgyConf['uKey']
pgyApiKey=pgyConf['apiKey']
installPwd = pgyConf['installPwd']
#执行打包命令
os.system(srcPath +'/gradlew')
apkPath = srcPath +'/app/build/outputs/apk/debug/app-debug.apk'
#上传apk到蒲公英
print(apkPath)
headers = {
    "enctype":"multipart/form-data"
}
params={
    "_api_key": pgyApiKey,
    "buildInstallType":2,
    "buildPassword":installPwd
    }
files={
    "file": open(apkPath, 'rb'),
}
print(params)
response = requests.post('https://www.pgyer.com/apiv2/app/upload',data=params,files=files, headers=headers)
print(response.status_code)
print(response.text)
print(response.json)