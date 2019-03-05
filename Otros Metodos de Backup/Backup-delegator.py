import gzip
import delegator

with gzip.open("backup.gz", "wb") as f:
  c = delegator.run("pg_dump -h localhost -U postgres cerveza")
  f.write(c.out.encode("utf-8"))