import configparser
config = configparser.ConfigParser()
config.read('./conf.ini')
srcPath=config['DEFAULT']['srcPath']
print('srcPath:',srcPath)