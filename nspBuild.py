import sys, os
from struct import pack as pk, unpack as upk

def gen_header(argc, argv):
    stringTable = '\x00'.join([os.path.basename(file) for file in argv[1:]])
    headerSize = 0x10 + (argc-1)*0x18 + len(stringTable)
    remainder = 0x10 - headerSize%0x10
    headerSize += remainder
    
    fileSizes = [os.path.getsize(file) for file in argv[1:]]
    fileOffsets = [sum(fileSizes[:n]) for n in range(argc-1)]
    
    fileNamesLengths = [len(os.path.basename(file))+1 for file in argv[1:]] # +1 for the \x00 separator
    stringTableOffsets = [sum(fileNamesLengths[:n]) for n in range(argc-1)]
    
    header =  b''
    header += b'PFS0'
    header += pk('<I', argc-1)
    header += pk('<I', len(stringTable)+remainder)
    header += b'\x00\x00\x00\x00'
    
    for n in range(argc-1):
        header += pk('<Q', fileOffsets[n])
        header += pk('<Q', fileSizes[n])
        header += pk('<I', stringTableOffsets[n])
        header += b'\x00\x00\x00\x00'
    header += stringTable.encode()
    header += remainder * b'\x00'
    
    return header   

def mk_nsp(argc, argv):
    if argc == 1:
        print('Usage is: %s file1 file 2 ...' % sys.argv[0])
        return 1
        
    name = input('Name of output nsp? ')
    outf = open(os.path.join(os.path.dirname(__file__), name), 'wb')
    
    print('Generating header...')
    header = gen_header(argc, argv)
    outf.write(header)
    
    for f in argv[1:]:
        print('Appending %s...' % f)
        with open(f, 'rb') as inf:
            while True:
                buf = inf.read(4096)
                if not buf:
                    break
                outf.write(buf)
    
    print('Saved to %s!' % outf.name)
    outf.close()
    
    return 0
    
if __name__ == '__main__':
    sys.exit(mk_nsp(len(sys.argv), sys.argv))