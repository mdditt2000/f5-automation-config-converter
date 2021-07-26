[2021-07-26T21:08:00.956Z] [INFO]: ACC Details:  {
  name: 'f5-as3-config-converter',
  author: 'F5 Networks',
  description: 'F5 AS3 Config Converter',
  version: '1.13.0',
  license: 'Apache-2.0',
  repository: 'git+https://github.com/f5devcentral/f5-as3-config-converter.git'
}
[2021-07-26T21:08:00.958Z] [INFO]: f5.chariot.convert called
[2021-07-26T21:08:00.960Z] [INFO]: f5.chariot.convert text found
[2021-07-26T21:08:01.400Z] [INFO]: ACC METADATA {
  recognized: {
    'ltm monitor https /Common/test_monitor_password': {
      adaptive: 'disabled',
      'defaults-from': '/Common/https',
      destination: '*:*',
      interval: '5',
      'ip-dscp': '0',
      password: '$M$OC$bN53XhCrVMTvO2+ZlApH7A==',
      recv: 'none',
      'recv-disable': 'none',
      send: '"GET /\\r\\n"',
      'time-until-up': '0',
      timeout: '16',
      username: 'test'
    }
  },
  supported: {
    'ltm monitor https /Common/test_monitor_password': {
      adaptive: 'disabled',
      'defaults-from': '/Common/https',
      destination: '*:*',
      interval: '5',
      'ip-dscp': '0',
      password: '$M$OC$bN53XhCrVMTvO2+ZlApH7A==',
      recv: 'none',
      'recv-disable': 'none',
      send: '"GET /\\r\\n"',
      'time-until-up': '0',
      timeout: '16',
      username: 'test'
    }
  },
  unSupported: {},
  declarationInfo: {
    classes: { Monitor: 1 },
    maps: {
      applications: [ '/Common/Shared' ],
      objects: [ '/Common/Shared/test_monitor_password' ],
      tenants: [ '/Common' ]
    },
    total: 1
  }
}