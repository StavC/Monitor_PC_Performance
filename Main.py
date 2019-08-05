import psutil
from psutil._common import bytes2human
def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))



def main():

   print(psutil.net_io_counters())
   pprint_ntuple(psutil.net_io_counters())
   print("X" * 100)
   svmem = psutil.virtual_memory()
   pprint_ntuple(svmem)
   print("X" * 100)
   cpu = psutil.cpu_percent(interval=1, percpu=False)
   print(f"{cpu} Precent")























if __name__ == '__main__':
    main()
