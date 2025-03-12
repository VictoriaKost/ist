# Импортируем библиотеку для работы с последовательным портом
import serial

# Импортируем модуль time для работы с задержками
import time

# Импортируем инструменты для работы с портами компьютера
import serial.tools.list_ports

# Создаем список доступных скоростей передачи данных
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']

# Получаем список всех доступных последовательных портов
ports = [p.device for p in serial.tools.list_ports.comports()]

# Выбираем первый доступный порт из списка
port_name = ports[0]

# Выбираем максимальную скорость из списка скоростей
port_speed = int(speeds[-1])

# Устанавливаем таймаут для операций с портом
port_timeout = 10

# Создаем объект для работы с последовательным портом
ard = serial.Serial(port_name, port_speed, timeout = port_timeout)

# Делаем задержку в 1 секунду для стабилизации соединения
time.sleep(1)

# Очищаем входной буфер порта
ard.flushInput()

# Начинаем блок обработки исключений
try:
    # Читаем все доступные данные из порта
    msg_bin = ard.read(ard.inWaiting())
    
    # Читаем дополнительные данные, если они появились
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    
    # Преобразуем бинарные данные в строку
    msg_str_ = msg_bin.decode()
    
    # Выводим длину полученных бинарных данных
    print(len(msg_bin))
    
# Обрабатываем возможные ошибки
except Exception as e:
    print('Error!')

# Закрываем соединение с портом
ard.close()

# Делаем небольшую задержку перед выводом
time.sleep(1)

# Выводим полученную строку
print(msg_str_)
