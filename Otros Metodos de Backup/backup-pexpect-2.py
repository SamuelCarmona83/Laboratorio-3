import gzip
import pexpect

with gzip.open("backup2.gz", "wb") as f:
  c = pexpect.spawn("pg_dump -h localhost -U postgres my_database")
  f.write(c.read())