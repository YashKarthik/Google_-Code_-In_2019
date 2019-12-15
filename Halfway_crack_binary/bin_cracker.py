import sys
from elftools.elf.elffile import ELFFile
from elftools.elf.relocation import RelocationSection
from elftools.elf.descriptions import describe_reloc_type

def process_file(filename):
    print('Processing file:', filename)
    with open(filename, 'rb') as f:
        elffile = ELFFile(f)
        for section in elffile.iter_sections():
            if not isinstance(section, RelocationSection):
                continue
            symtable = elffile.get_section(section['sh_link'])
            print('  %s section with %s relocations' % (
                section.name, section.num_relocations()))
            for reloc in section.iter_relocations():
                symbol = symtable.get_symbol(reloc['r_info_sym'])
                print('    Relocation (%s)' % 'RELA' if reloc.is_RELA() else 'REL')
                # Relocation entry attributes are available through item lookup
                print('      offset = %s' % hex(reloc['r_offset']))
                print(symbol.name, 'type:', describe_reloc_type(reloc['r_info_type'], elffile), 'load at: ', hex(reloc['r_offset']))
if __name__ == '__main__':
    process_file(sys.argv[1])