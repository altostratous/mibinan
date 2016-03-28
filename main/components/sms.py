# To use this Client just create it with its default constructor and call send_sms(to_numbers, text)
# To numbers is an array of string and be sure that you have set preferences in settings.py file already
from suds.client import Client
from django.conf import settings


class NetScSmsClient(Client):
    def __init__(self):
        sms_settings = settings.SMS_SETTINGS
        Client.__init__(self, sms_settings['url'])

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
