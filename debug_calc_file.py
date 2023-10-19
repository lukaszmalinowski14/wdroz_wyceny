file_path = 'N:/Wsp-Ogol/Backlog_raporty_LMA/Nowy folder/calculate__618ers.cprj'
# target_byte = 0x81

# with open(file_path, 'rb') as file:
#     try:
#         while True:
#             byte = file.read(1)
#             if not byte:
#                 # Koniec pliku
#                 break

#             # Sprawdź wartość bajtu
#             if byte[0] == target_byte:
#                 position = file.tell() - 1  # Aktualna pozycja w pliku przed odczytem
#                 print(f"Znaleziono bajt 0x81 na pozycji {position}")

#     except Exception as e:
#         print(f"Wystąpił błąd podczas czytania pliku: {str(e)}")

# print('End')

################################################################

target_byte = 0x81
line_number = 1

with open(file_path, 'rb') as file:
    try:
        while True:
            byte = file.read(1)
            if not byte:
                # Koniec pliku
                break

            # Sprawdź wartość bajtu
            if byte[0] == target_byte:
                position = file.tell() - 1  # Aktualna pozycja w pliku przed odczytem
                with open(file_path, 'r', encoding='utf-8', errors='replace') as text_file:
                    # Odczytaj wszystkie linie przed pozycją
                    lines = text_file.readlines()
                    line_position = 0
                    current_position = 0

                    for i, line in enumerate(lines):
                        current_position += len(line.encode('utf-8'))
                        if current_position >= position:
                            line_position = position - \
                                (current_position - len(line.encode('utf-8')))
                            break

                    print(
                        f"Znaleziono bajt 0x81 na linii {line_number}, znak {line_position}")

            # Zlicz numer linii
            if byte == b'\n':
                line_number += 1

    except Exception as e:
        print(f"Wystąpił błąd podczas czytania pliku: {str(e)}")

print('END')
