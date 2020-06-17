from zlib import crc32

print(crc32(b"squeamish ossifrage") == crc32(b"deltaTvJZx"))

print(crc32(b"buckeroo") == crc32(b"plumless"))
