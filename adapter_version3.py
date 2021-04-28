class Elf:
    name = 'Galaderiel'
    def nall_nin(self):
        print('Elf says: Calling the Overlord...') 

class Dwarf:
    def estver_narho(self):
        print('Dwarf says: Calling the Overlord...')
        
class Human:
    def ring_mig(self):
        print('Human says: Calling the Overlord...')



class MinionAdapter:
    _initialised = False 

    def __init__(self, minion, **adapted_methods):
        self.minion = minion 
        print(adapted_methods)
        for key, value in adapted_methods.items():
            func = getattr(self.minion, value)
            self.__setattr__(key, func)

        self._initialised = True 
    
    def __getattr__(self, attr):
        print('have to ...')
        return getattr(self.minion, attr)


    def __setattr__(self, key, value):
        if not self._initialised: # not understand this
            super().__setattr__(key, value) # need to figure this out what this mean
        else:
            setattr(self.minion, key, value)


if __name__=='__main__':
    minion_adapters = [
        MinionAdapter(Elf(), call_me='nall_nin'), 
        MinionAdapter(Dwarf(), call_me = 'estver_narho'),
        MinionAdapter(Human(), call_me='ring_mig')

    ]            

    for adapter in minion_adapters:
        adapter.call_me() 

    print(minion_adapters)
    elf_adapter = minion_adapters[0]
    print()
    print(f'Name from Adapter: {elf_adapter.name}')
    print(f'Name from Minion: {elf_adapter.minion.name}')

    minion_adapters[0].name = 'Elrond'
    
    print()
    print(f'Name from Adapter: {elf_adapter.name}')
    print(f'Name from Minion: {elf_adapter.minion.name}')