from pyethereum import tester, utils

key = 'steve'
s = tester.state()
registry = s.abi_contract('name_registry.se')
public_key0 = utils.privtoaddr(tester.k0)
public_key1 = utils.privtoaddr(tester.k1)

registry.register(key, sender=tester.k0)
registry.set_value(key, 'rules', sender=tester.k0)

registry.register(key, sender=tester.k1)
registry.set_value(key, 'stinks', sender=tester.k1)

print(key)
print(str(registry.value(key)))
