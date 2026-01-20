def zagruzka_discipline(filename):
    disciplines = []
    import os
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден")
        return disciplines

    with open(filename, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            
            parts = line.split(';')
            if len(parts) != 6:
                print(f"Ошибка в строке {line_num}: должно быть 6 полей, найдено {len(parts)}")
                continue
            
            #Проверка, что поля 2–4 (семестр, длительность, часы) — числовые
            if not (parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit()):
                print(f"Ошибка в строке {line_num}: нечисловые данные в полях 2–4")
                continue
            
            discipline = {
                'name': parts[0],
                'semester': int(parts[1]),
                'time': int(parts[2]),
                'hours': int(parts[3]),
                'assessment': parts[4],
                'department': parts[5]
            }
            disciplines.append(discipline)
    return disciplines
