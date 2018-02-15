#!/usr/bin/python

valid_chars = [ 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D,   # chars A-M
                0x4E, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A,   # chars N-Z
                0x2D, 0x5F,                                                                     # chars - and _ (dash and underscore)
                0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39]                     # chars 0-9

hash_arr = [0x278CDF58, 0x2D386ECE, 0xABA416E3, 0xBFFDE1F0, 0x6FADB57B,
			0x581419AC, 0xA93A5DA5, 0x9FE09B81, 0x62B621C4, 0x0E2F42D3,
			0x1CB3F267, 0x7DEED7DB, 0x487C3558, 0xBC541011, 0x70F400CF,
			0x7E11E4CF, 0x52FEB192, 0x1E24D477, 0x4A6B6EBC, 0x6DE558E4,
			0x6E4851F8, 0x9F5462ED, 0x896773D7, 0x68B0F30D, 0x7B8B2670,
			0x1E84D9C6, 0xF9B64044, 0x11E91917, 0x7EC953AB, 0x0AFB3480,
			0x5D5421CF, 0x4055C0A5, 0xB4C2ED27, 0x6751A7A7, 0x0F0FC4F7,
			0xBF550EED, 0x1B54824,  0x72C7BD89, 0xB15AFA72, 0xD35C5E5C,
			0x86BD8B3A, 0x334B7FA5, 0x47E5605F, 0xE1E54873, 0xD8367B99]

def getStringHash(process_name):
    ESI= 0xFFFFFFFF
    for char in process_name.upper():
        EDI = ord(char)
        for i in range(0,8):
            EAX = EDI
            EAX = EAX^ESI
            ESI = ESI >> 1
            if EAX & 0x01:
                ESI = ESI ^ 0xEDB88320
            EDI = EDI >> 1
    return ESI


for a in valid_chars:
    for b in valid_chars:
        for c in valid_chars:
            for d in valid_chars:
                process = chr(a)+chr(b)+chr(c)+chr(d)+".EXE"
                string_hash = getStringHash(process)
                if string_hash in hash_arr:
                        print "Hash matches: %s --> %s" % (process.upper(),hex(string_hash)[2:].upper())
