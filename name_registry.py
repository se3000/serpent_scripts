from pyethereum import tester, utils

s = tester.state()
c = s.abi_contract('namecoin.se')
public_key0 = utils.privtoaddr(tester.k0)
public_key1 = utils.privtoaddr(tester.k1)

c.register('steve', public_key0)
c.register('steve', public_key1)

print(str(c.ask('steve')))
print(str(public_key0))
print(str(public_key0 == c.ask('steve')))
