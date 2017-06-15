#!/usr/bin/python
DOCUMENTATION = '''
---
module: hl_crypto_keys
short_description:
    - Retrieve certificates and keys generated by the Hyperledger 
      cryptogen utility.
description:
    - A module for extracting from the file system the output generated by the
      Hyperledger utility "crypt-config" which generates PKI certificates
      and keys.  The result is a JSON object whose structure mirrors the
      layout generated by cryptogen in the file system.  In the deepest
      nesting of the JSON object, the path to the generated certificates and
      keys are stored in arrays with the node identifiers "certificates" and
      "keys", respectively. 
author: Keoja LLC
'''

EXAMPLES = '''
- name: Retrieve the certificates and keys generated by crypto-config.
  hl_crypto_keys:
  register: cryptokeys
'''

def descend(path):
    retValue = {}
    certificates = []
    keys = []
    abs_path = os.path.abspath(path)
    
    for d in os.listdir(abs_path):
        abs_path_extended = os.path.join(abs_path, d)
        if os.path.isdir(abs_path_extended):
           retValue[str(d)] = descend(abs_path_extended)
        else:
            # Key?
            if isKey(d):
                keys.append(abs_path_extended)
            else:
                certificates.append(abs_path_extended)

    # Any Keys?
    if len(keys) > 0:
        retValue['keys'] = keys;
        
    # Any Certificates?
    if len(certificates) > 0:
        retValue['certificates'] = certificates
        
    return retValue

def isKey(fileName):    
    return fileName.endswith("_sk") or fileName.endswith('key')
    
def main():

    module = AnsibleModule(
        argument_spec = dict(
            path    = dict(required=True)
        ),
        add_file_common_args=True,
        supports_check_mode=True
    )

    path = os.path.expanduser(module.params['path'])
    
    try:
        # Does the path the user gave us exist?
        if os.path.exists(path):
            # Is it a folder?
            if os.path.isdir(path) :
                # Yes
                module.exit_json(changed=True, keys=json.dumps(descend(path)))
            else: 
                module.fail_json(changed=False, msg='The path "' + str(os.path.abspath(path)) + '" is not a folder.')
        else:            
            module.fail_json(changed=False, msg='The path "' + str(os.path.abspath(path)) + '" does not exist.')   

    #handle exceptions
    except Exception, e:
        module.fail_json( msg='Error: ' + str(e) )

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
