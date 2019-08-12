import psutil
from psutil._common import bytes2human
def pprint_ntuple(nt):
    details=[]
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        details.append(('%-10s : %7s' % (name.capitalize(), value)))
    return details


def main():

   network_details=[]
   network_details=pprint_ntuple(psutil.net_io_counters())
   print(network_details)
   bytes_sent =network_details[0]
   bytes_recv=network_details[1]
   packets_sent=network_details[2]
   packets_recv=network_details[3]
   i=0
   while i<4:
       print(network_details[i])
       i=i+1

   '''
   print("X" * 100)
   svmem = psutil.virtual_memory()
   pprint_ntuple(svmem)
   print("X" * 100)


   cpu = psutil.cpu_percent(interval=1, percpu=False)
   print(f"{cpu} Precent")

    '''





















if __name__ == '__main__':
    main()
