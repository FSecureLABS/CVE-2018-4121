import sys

def print_ln(bytes, out):
  ln = '[ '
  for b in bytes:
    ln += "0x%02x," % ord(b);
  out.write(ln + ' ],')

bytes = open(sys.argv[1]).read()
out = open(sys.argv[2], 'w')

out.write("DYLIB_LENGTH = %d;\n" % len(bytes))
out.write("DYLIB = [\n")

while len(bytes) > 8:
  print_ln(bytes[:8], out)
  bytes = bytes[8:]
  out.write('\n');

if len(bytes):
  bytes = bytes + "\x00"*(8 - len(bytes))
  print_ln(bytes, out)

out.write('];')
