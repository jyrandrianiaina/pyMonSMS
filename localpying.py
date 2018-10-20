import pyping
import gammu.smsd
import sys
smsd = gammu.smsd.SMSD('/etc/gammu-smsdrc')
def localping():
    my_server = ["8.8.8.8","1.1.1.1","1.0.0.1","8.8.4.4"]
    s1 = []
    for myip in my_server:
        response = pyping.ping(myip,timeout=10000)
        if response.ret_code == 0:
            sms = myip +" : " +response.avg_rtt+ "ms"
        else:
            response.max_rtt = " "
            response.avg_rtt = "OFFLINE"
            sms = myip +" : " +response.avg_rtt
        s1.append(sms)
    return s1

def sending_sms(requester):
    message = {
        'Text': localping() ,
        'SMSC': {'Location': 1},
        'Number': requester
    }
    smsd.InjectSMS([message])    
    print 'sms is sent'
sending_sms(sys.argv[1])

