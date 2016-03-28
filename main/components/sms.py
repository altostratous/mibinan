from suds.client import Client
from django.conf import settings


class NetScSmsClient(Client):
    def __init__(self, url):
        Client.__init__(self, url)

    def send_sms(self, to, text):
        sms_settings = settings.SMS_SETTINGS
        to_numbers = self.factory.create('ArrayOfString')
        to_numbers.string = to
        result = self.service.SendSms(sms_settings['username'],
                                      sms_settings['password'],
                                      to_numbers, '50001333789521',
                                      text,
                                      False, '')
        return result
