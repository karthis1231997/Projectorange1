import configparser

config = configparser.RawConfigParser()
config.read('C:\\Users\\hkarthis\\PycharmProjects\\Projectoneorange\\Configurations\\config.ini')


class Readconfig:
    @staticmethod
    def getorangeurl():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getuserid():
        userid = config.get('common info', 'username')
        return userid

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password
