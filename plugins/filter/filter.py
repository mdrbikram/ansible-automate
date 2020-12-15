import re

class FilterModule:
    @staticmethod
    def filters():
        return {
                'startwith': FilterModule.starts_with,
                'devip' : FilterModule.dev_ip
    }

    @staticmethod
    def starts_with(item):
        this=[]
        for i in item:
          if i.startswith("Device"):
            this.append(i)
        return this


    @staticmethod
    def dev_ip(item):
        indict = {}
        a = item.lstrip('-')
        b = a.strip('\n')
        for i in b.split("-------------------------"):
         listsplit = i.split('\n')
         for j in listsplit:
          if j.startswith('Device'):
           device = j[11:]
           indict[device] = {}
           indict[device]['name'] = device
          if j.startswith('Platform'):
           indict[device]['platform']=j.split(',')[0]
          text = ''.join(listsplit)
          if ' IP ' in text:
            if j.startswith('  IP address'):
              indict[device]['ipaddr'] = j[14:]
          else:
            indict[device]['ipaddr'] = 'N/A'
        return indict

