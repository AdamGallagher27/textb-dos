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

# loading classes from class folder
Block = load_class('Block')
LinkedList = load_class('LinkedList')

# create new block classes
block_1 = Block('this is text one')
block_2 = Block('this is text two')

# linked list which will hold all blocks
block_list = LinkedList()

# add to the end of linked list
block_list.append(block_1)
block_list.append(block_2)

# print list
block_list.print_list()