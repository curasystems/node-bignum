{
  'targets': [
    {
      'target_name': 'bignum',
      'sources': [ 'bignum.cc' ],
      "conditions": [
             [ 'OS=="win"', {
          'conditions': [
            # "openssl_root" is the directory on Windows of the OpenSSL files.
            # Check the "target_arch" variable to set good default values for
            # both 64-bit and 32-bit builds of the module.
            ['target_arch=="x64"', {
              'variables': {
                'openssl_root%': 'C:/OpenSSL-Win64'
              },
            }, {
              'variables': {
                'openssl_root%': 'C:/OpenSSL-Win32'
              },
            }],
          ],
          'libraries': [ 
            '-l<(openssl_root)/lib/libeay32.lib',
          ],
          'include_dirs': [
            '<(openssl_root)/include',
          ],
        }],
         ['node_shared_openssl=="false"', {
            # so when "node_shared_openssl" is "false", then OpenSSL has been
            # bundled into the node executable. So we need to include the same
            # header files that were used when building node.
            'include_dirs': [
              '<(node_root_dir)/deps/openssl/openssl/include'
            ],
          "conditions": [
          ['target_arch=="ia32"', {
            'variables': {'openssl_config_path':
                          '<(nodedir)/deps/openssl/config/piii'},
          }, {
            'variables': {'openssl_config_path':
                          '<(nodedir)/deps/openssl/config/k8'},
          }]
          ]
        }]
      ],
      "include_dirs": [
        "<(nodedir)/deps/openssl/openssl/include",
        "<(openssl_config_path)"
      ]
    }
  ]
}
