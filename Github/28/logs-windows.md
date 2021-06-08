```
[2021-06-08T20:40:58.090Z] [INFO]: ACC Details:  {
  name: 'f5-as3-config-converter',
  author: 'F5 Networks',
  description: 'F5 AS3 Config Converter',
  version: '1.12.0',
  license: 'Apache-2.0',
  repository: 'git+https://github.com/f5devcentral/f5-as3-config-converter.git'
}
[2021-06-08T20:40:58.191Z] [INFO]: f5.chariot.convert called
[2021-06-08T20:40:58.193Z] [INFO]: f5.chariot.convert text found
[2021-06-08T20:40:58.849Z] [INFO]: ACC METADATA {
  recognized: {
    'ltm data-group internal /partition_1/string-datagroup': { records: '{', '/api/test/app1': {}, '}': '', type: 'string' },
    'ltm data-group internal /partition_2/address_datagroup': { records: '{', type: 'ip', '}': '' }
  },
  supported: {
    'ltm data-group internal /partition_1/string-datagroup': { records: '{', '/api/test/app1': {}, '}': '', type: 'string' },
    'ltm data-group internal /partition_2/address_datagroup': { records: '{', type: 'ip', '}': '' }
  },
  unSupported: {},
  declarationInfo: {
    classes: { Data_Group: 2 },
    maps: {
      applications: [ '/partition_1/Shared', '/partition_2/Shared' ],
      objects: [
        '/partition_1/Shared/string-datagroup',
        '/partition_2/Shared/address_datagroup'
      ],
      tenants: [ '/partition_1', '/partition_2' ]
    },
    total: 2
  }
}
[2021-06-08T20:45:08.694Z] [INFO]: f5.chariot.convert called
[2021-06-08T20:45:08.695Z] [INFO]: f5.chariot.convert text found
[2021-06-08T20:45:09.000Z] [INFO]: ACC METADATA {
  recognized: {
    'ltm data-group internal /partition_1/string-datagroup': { records: '{', '/api/test/app1': {}, '}': '', type: 'string' },
    'ltm data-group internal /partition_2/address_datagroup': { records: '{', type: 'ip', '}': '' }
  },
  supported: {
    'ltm data-group internal /partition_1/string-datagroup': { records: '{', '/api/test/app1': {}, '}': '', type: 'string' },
    'ltm data-group internal /partition_2/address_datagroup': { records: '{', type: 'ip', '}': '' }
  },
  unSupported: {},
  declarationInfo: {
    classes: { Data_Group: 2 },
    maps: {
      applications: [ '/partition_1/Shared', '/partition_2/Shared' ],
      objects: [
        '/partition_1/Shared/string-datagroup',
        '/partition_2/Shared/address_datagroup'
      ],
      tenants: [ '/partition_1', '/partition_2' ]
    },
    total: 2
  }
}
```