
  dig

  DNS lookup utility.
  More information: https://manned.org/dig.

  - Lookup the IP(s) associated with a hostname (A records):
    dig +short example.com

  - Get a detailed answer for a given domain (A records):
    dig +noall +answer example.com

  - Query a specific DNS record type associated with a given domain name:
    dig +short example.com A|MX|TXT|CNAME|NS

  - Specify an alternate DNS server to query and optionally use DNS over TLS (DoT):
    dig +tls @1.1.1.1|8.8.8.8|9.9.9.9|... example.com

  - Perform a reverse DNS lookup on an IP address (PTR record):
    dig -x 8.8.8.8

  - Find authoritative name servers for the zone and display SOA records:
    dig +nssearch example.com

  - Perform iterative queries and display the entire trace path to resolve a domain name:
    dig +trace example.com

  - Query a DNS server over a non-standard [p]ort using the TCP protocol:
    dig +tcp -p port @dns_server_ip example.com


