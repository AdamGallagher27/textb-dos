
import importlib.util

# function to load in classes 
def load_class(class_name):

    # file path to class
    path = 'classes/{}.py'.format(class_name)

    # load module from path
    spec = importlib.util.spec_from_file_location(class_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # return class
    return getattr(module, class_name)


Brain = load_class('Brain')
Location = load_class('Location')
Item = load_class('Item')

gold_ring = Item('Gold RIng')

test = Location(
    'test',
    'test',
    {
        'north': 'test',
        'south': 'test',
        'east': 'test',
        'west': 'test'
    },
    []
)

starting_location = Location(
    'start loc',
    'this is the start fear not',
    {
        'north': test,
        'south': test,
        'east': test,
        'west': test
    },
    [
        gold_ring
    ]

)

GameState = Brain(starting_location)