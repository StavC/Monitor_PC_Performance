def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))


def main():

    svmem=psutil.virtual_memory()
    pprint_ntuple(svmem)
    print("X"*100)
    cpu=psutil.cpu_percent(interval=1,percpu=False)
    print(cpu)


