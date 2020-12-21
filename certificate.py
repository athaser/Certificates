from __future__ import print_function, unicode_literals

from datetime import datetime, timedelta
from OpenSSL import crypto

# load private key
ftype = crypto.FILETYPE_PEM
with open('cert.key', 'rb') as f: k = f.read()
k = crypto.load_privatekey(ftype, k)

now    = datetime.now()
expire = now + timedelta(days=365)

# country (countryName, C)
# state or province name (stateOrProvinceName, ST)
# locality (locality, L)
# organization (organizationName, O)
# organizational unit (organizationalUnitName, OU)
# common name (commonName, CN)

cert = crypto.X509()
cert.get_subject().C  = "Te"
cert.get_subject().ST = "Greece"
cert.get_subject().L  = "Thessaloniki"
cert.get_subject().O  = "Certificate"
cert.get_subject().OU = "Python"
cert.get_subject().CN = "pythoncertificate"
cert.set_serial_number(1000)
cert.set_notBefore(now.strftime("%Y%m%d%H%M%SZ").encode())
cert.set_notAfter(expire.strftime("%Y%m%d%H%M%SZ").encode())
cert.set_issuer(cert.get_subject())
cert.set_pubkey(k)
cert.sign(k, 'sha1')

with open('cert.pem', "wb") as f:
    f.write(crypto.dump_certificate(ftype, cert))