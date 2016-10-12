# Blocks

It's an example of DATA DSL for static block management.  
It was created for Moscow Python conf, you can find slides here http://moscowpython.bro.engineering/  

Source code for model interpreter is here https://github.com/ir4y/blocks/blob/master/block/models/__init__.py  
Source code for admin interpreter is here https://github.com/ir4y/blocks/blob/master/block/admin/schema.py  

You can change schema file https://github.com/ir4y/blocks/blob/master/config/settings/group_schema.yml to create admin structure you want.
But you need to restart Django app manually because it doesn't watch YAML file for auto reload.
