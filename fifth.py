
import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    """
    Tato funkce načte binární soubor z cesty file_name,
    z něj přečte prvních header_length bytů a ty vrátí pomocí return
    """
    with open(file_name, 'rb') as file:
        return file.read(header_length)
     


def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné jpeg_header
    """
    # načti hlavičku souboru
    header = read_header(file_name, len(jpeg_header))

    # vyhodnoť zda je soubor jpeg
    if header != jpeg_header:
        return False
    else:
        return header == jpeg_header


def is_gif(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanými hlavičkami v proměnných gif_header1 a gif_header2
    """
    header1 = read_header(file_name, len(gif_header1))
    header2 = read_header(file_name, len(gif_header2))
    # vyhodnoť zda je soubor gif
    if header1 != gif_header1:
        return header2 == gif_header2
    elif header2 != gif_header2:
        return header1 == gif_header1
    else:
        return False


def is_png(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné png_header
    """
    header =  read_header(file_name, len(png_header))    
    # vyhodnoť zda je soubor png
    if header != png_header:
        return False
    else:
        return header == png_header


def print_file_type(file_name):
    """
    Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    # přidej try-catch blok, odchyť obecnou vyjímku Exception a vypiš ji    
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    
    except IndexError:
        print('Nebylo zadáno názvu souboru jako argumentu příkazové řádky nebo cesty k obrazku.')
    except FileNotFoundError:
        print(f'Soubor {file_name} nebyl nalezen.')
    except Exception as e:
        print(f'Nastala chyba: {e}')
