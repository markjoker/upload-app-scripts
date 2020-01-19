import configparser
import os

#读取配置
config = configparser.ConfigParser()
config.read('./conf.ini')
srcPath=config['DEFAULT']['srcPath']

#执行打包命令
os.system(srcPath +'/gradlew')