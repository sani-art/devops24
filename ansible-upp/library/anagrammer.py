#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

def run_module():
    
    module_args = dict(
         message=dict(type='str', required=True)
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    message = module.params['message']
    reversed_message = message[::-1]

    if message == 'fail me':
        module.fail_json(msg="You requested this to fail",
                         changed=True,
			 original_mesage=message,
			 reversed_message=reversed_message)

    changed = (message != reversed_message)

    module.exit_json(changed=changed,
		     original_message=message,
                     reversed_message=reversed_message)

if __name__ == '__main__':
    run_module()
