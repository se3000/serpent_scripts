import serpent
from pyethereum import tester, utils, abi

serpent_code = '''
def transfer(amount, recipient):
    log(amount, recipient)
    return(amount)
'''

s = tester.state()
c = s.abi_contract(serpent_code)
public_key1 = utils.privtoaddr(tester.k1)
data = c.transfer(500, public_key1, sender=tester.k0)

print(str(data))
