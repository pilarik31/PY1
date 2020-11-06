from CoronaApi import CoronaApi
from pprint import pprint

corona = CoronaApi()
data = corona.get()


for val in data['data']:
    print('Date: ' + val['datum'])
    print('Newly infected: ' + str(val['prirustkovy_pocet_nakazenych']))
    print('Total infected: ' + str(val['kumulativni_pocet_nakazenych']))
    print('===')
# %%
