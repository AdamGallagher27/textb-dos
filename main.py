import importlib.util

# file path to block class
block_path = 'classes\Block.py'

# load module from path
spec = importlib.util.spec_from_file_location('Block', block_path)
my_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(my_module)

# Block class
Block = my_module.Block

block_order = 0

block_list = []


def add_block(text):
    block = Block(block_order, text)
    block_list.push(block)
    block_order += 1


