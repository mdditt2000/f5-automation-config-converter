[2021-07-26T15:57:38.988Z] [INFO]: ACC Details:  {
  name: 'f5-as3-config-converter',
  author: 'F5 Networks',
  description: 'F5 AS3 Config Converter',
  version: '1.13.0',
  license: 'Apache-2.0',
  repository: 'git+https://github.com/f5devcentral/f5-as3-config-converter.git'
}
[2021-07-26T15:57:38.990Z] [INFO]: f5.chariot.convert called
[2021-07-26T15:57:38.991Z] [INFO]: f5.chariot.convert text found
[2021-07-26T15:57:39.358Z] [INFO]: ACC METADATA {
  recognized: {
    'sys file ssl-cert /Common/custom_ssl_cert_key': {
      'cache-path': '/config/filestore/files_d/Common_d/certificate_d/:Common:custom_ssl_cert_key_220931_1',
      revision: '1',
      'source-path': '/var/run/key_mgmt/iirKX1/ssl.crt/custom_ssl_cert_key'
    },
    'sys file ssl-key /Common/custom_ssl_cert_key': {
      'cache-path': '/config/filestore/files_d/Common_d/certificate_key_d/:Common:custom_ssl_cert_key_220928_1',
      revision: '1',
      'source-path': '/var/run/key_mgmt/rO92Q0/ssl.key/custom_ssl_cert_key'
    },
    'ltm profile server-ssl /Common/custom_ssl_server_profile': {
      'alert-timeout': 'indefinite',
      'app-service': 'none',
      'bypass-on-client-cert-fail': 'disabled',
      'bypass-on-handshake-alert': 'disabled',
      'cache-size': '262144',
      'cache-timeout': '3600',
      cert: '/Common/custom_ssl_cert_key',
      chain: 'none',
      'cipher-group': 'none',
      ciphers: 'DEFAULT',
      'defaults-from': '/Common/serverssl',
      'generic-alert': 'enabled',
      'handshake-timeout': '10',
      key: '/Common/custom_ssl_cert_key',
      'max-active-handshakes': 'indefinite',
      'mod-ssl-methods': 'disabled',
      mode: 'enabled',
      options: [ 'dont-insert-empty-fragments', 'no-tlsv1.3' ],
      'proxy-ssl': 'disabled',
      'proxy-ssl-passthrough': 'disabled',
      'renegotiate-period': 'indefinite',
      'renegotiate-size': 'indefinite',
      renegotiation: 'enabled',
      'secure-renegotiation': 'require-strict',
      'server-name': 'none',
      'session-mirroring': 'disabled',
      'session-ticket': 'disabled',
      'sni-default': 'false',
      'sni-require': 'false',
      'ssl-forward-proxy': 'disabled',
      'ssl-forward-proxy-bypass': 'disabled',
      'ssl-forward-proxy-verified-handshake': 'disabled',
      'ssl-sign-hash': 'any',
      'strict-resume': 'disabled',
      'unclean-shutdown': 'enabled'
    },
    'ltm virtual /tenant_3/application_3/VS_app2': {
      'creation-time': '2021-01-13:07:49:19',
      destination: '/tenant_3/application_3/10.144.18.33:0',
      'ip-protocol': 'tcp',
      'last-modified-time': '2021-05-20:19:13:15',
      mask: '255.255.255.255',
      profiles: {
        '/Common/custom_ssl_client_profile': { context: 'clientside' },
        '/Common/custom_ssl_server_profile': { context: 'serverside' },
        '/Common/tcp': {}
      },
      source: '0.0.0.0/24',
      'translate-address': 'enabled',
      'translate-port': 'disabled'
    },
    'ltm virtual-address /tenant_3/application_3/10.144.18.33': {
      address: '10.144.18.33',
      arp: 'enabled',
      mask: '255.255.255.255',
      'traffic-group': '/Common/traffic-group-1'
    },
    'ltm profile client-ssl /Common/custom_ssl_client_profile': {
      'app-service': 'none',
      'cert-key-chain': {
        custom_ssl_cert_key_0: {
          cert: '/Common/custom_ssl_cert_key',
          key: '/Common/custom_ssl_cert_key'
        }
      },
      'defaults-from': '/Common/clientssl',
      'inherit-ca-certkeychain': 'true',
      'inherit-certkeychain': 'false'
    }
  },
  supported: {
    'sys file ssl-cert /Common/custom_ssl_cert_key': {
      'cache-path': '/config/filestore/files_d/Common_d/certificate_d/:Common:custom_ssl_cert_key_220931_1',
      revision: '1',
      'source-path': '/var/run/key_mgmt/iirKX1/ssl.crt/custom_ssl_cert_key'
    },
    'sys file ssl-key /Common/custom_ssl_cert_key': {
      'cache-path': '/config/filestore/files_d/Common_d/certificate_key_d/:Common:custom_ssl_cert_key_220928_1',
      revision: '1',
      'source-path': '/var/run/key_mgmt/rO92Q0/ssl.key/custom_ssl_cert_key'
    },
    'ltm profile server-ssl /Common/custom_ssl_server_profile': {
      'alert-timeout': 'indefinite',
      'app-service': 'none',
      'bypass-on-client-cert-fail': 'disabled',
      'bypass-on-handshake-alert': 'disabled',
      'cache-size': '262144',
      'cache-timeout': '3600',
      cert: '/Common/custom_ssl_cert_key',
      chain: 'none',
      'cipher-group': 'none',
      ciphers: 'DEFAULT',
      'defaults-from': '/Common/serverssl',
      'generic-alert': 'enabled',
      'handshake-timeout': '10',
      key: '/Common/custom_ssl_cert_key',
      'max-active-handshakes': 'indefinite',
      'mod-ssl-methods': 'disabled',
      mode: 'enabled',
      options: [ 'dont-insert-empty-fragments', 'no-tlsv1.3' ],
      'proxy-ssl': 'disabled',
      'proxy-ssl-passthrough': 'disabled',
      'renegotiate-period': 'indefinite',
      'renegotiate-size': 'indefinite',
      renegotiation: 'enabled',
      'secure-renegotiation': 'require-strict',
      'server-name': 'none',
      'session-mirroring': 'disabled',
      'session-ticket': 'disabled',
      'sni-default': 'false',
      'sni-require': 'false',
      'ssl-forward-proxy': 'disabled',
      'ssl-forward-proxy-bypass': 'disabled',
      'ssl-forward-proxy-verified-handshake': 'disabled',
      'ssl-sign-hash': 'any',
      'strict-resume': 'disabled',
      'unclean-shutdown': 'enabled'
    },
    'ltm virtual /tenant_3/application_3/VS_app2': {
      'creation-time': '2021-01-13:07:49:19',
      destination: '/tenant_3/application_3/10.144.18.33:0',
      'ip-protocol': 'tcp',
      'last-modified-time': '2021-05-20:19:13:15',
      mask: '255.255.255.255',
      profiles: {
        '/Common/custom_ssl_client_profile': { context: 'clientside' },
        '/Common/custom_ssl_server_profile': { context: 'serverside' },
        '/Common/tcp': {}
      },
      source: '0.0.0.0/24',
      'translate-address': 'enabled',
      'translate-port': 'disabled'
    },
    'ltm virtual-address /tenant_3/application_3/10.144.18.33': {
      address: '10.144.18.33',
      arp: 'enabled',
      mask: '255.255.255.255',
      'traffic-group': '/Common/traffic-group-1'
    },
    'ltm profile client-ssl /Common/custom_ssl_client_profile': {
      'app-service': 'none',
      'cert-key-chain': {
        custom_ssl_cert_key_0: {
          cert: '/Common/custom_ssl_cert_key',
          key: '/Common/custom_ssl_cert_key'
        }
      },
      'defaults-from': '/Common/clientssl',
      'inherit-ca-certkeychain': 'true',
      'inherit-certkeychain': 'false'
    }
  },
  unSupported: {},
  declarationInfo: {
    classes: { Certificate: 1, Service_TCP: 1, TLS_Client: 1, TLS_Server: 1 },
    maps: {
      applications: [ '/Common/Shared', '/tenant_3/application_3' ],
      objects: [
        '/Common/Shared/custom_ssl_cert_key',
        '/Common/Shared/custom_ssl_server_profile',
        '/Common/Shared/custom_ssl_client_profile',
        '/tenant_3/application_3/VS_app2'
      ],
      tenants: [ '/Common', '/tenant_3' ]
    },
    total: 4
  }
}
