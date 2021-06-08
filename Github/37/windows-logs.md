```
[2021-06-08T22:24:10.604Z] [INFO]: f5.chariot.convert called
[2021-06-08T22:24:10.605Z] [INFO]: f5.chariot.convert text found
[2021-06-08T22:24:10.882Z] [INFO]: ACC METADATA {
  recognized: {
    'ltm virtual /Common/vs_hcf_443': {
      destination: '/Common/192.168.0.1:443',
      'ip-protocol': 'tcp',
      mask: '255.255.255.255',
      pool: '/Common/hcf_80',
      profiles: '{',
      '/Common/tcp': {},
      '}': '',
      source: '0.0.0.0/0',
      'translate-address': 'enabled',
      'translate-port': 'enabled'
    },
    'ltm pool /Common/hcf_80': {
      description: 'hcf_80',
      members: '{',
      '}': '',
      monitor: '/Common/http'
    },
    'ltm node /Common/10.0.0.1': { address: '10.0.0.1' }
  },
  supported: {
    'ltm virtual /Common/vs_hcf_443': {
      destination: '/Common/192.168.0.1:443',
      'ip-protocol': 'tcp',
      mask: '255.255.255.255',
      pool: '/Common/hcf_80',
      profiles: '{',
      '/Common/tcp': {},
      '}': '',
      source: '0.0.0.0/0',
      'translate-address': 'enabled',
      'translate-port': 'enabled'
    },
    'ltm pool /Common/hcf_80': {
      description: 'hcf_80',
      members: '{',
      '}': '',
      monitor: '/Common/http'
    }
  },
  unSupported: { 'ltm node /Common/10.0.0.1': { address: '10.0.0.1' } },
  declarationInfo: {
    classes: { Pool: 1, Service_Generic: 1 },
    maps: {
      applications: [ '/Common/Shared' ],
      objects: [ '/Common/Shared/vs_hcf_443', '/Common/Shared/hcf_80' ],
      tenants: [ '/Common' ]
    },
    total: 2
  }
}
```