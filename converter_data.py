import datetime

def unix_para_data(timestamp):
    """Converte um timestamp Unix para um objeto datetime.

    Args:
        timestamp (int): O timestamp Unix a ser convertido.

    Returns:
        datetime.datetime: O objeto datetime correspondente ao timestamp.
    """

    data_e_hora = datetime.datetime.fromtimestamp(timestamp)
    return data_e_hora.strftime('%d/%m/%Y %H:%M:%S')  # Formata a data como dd/mm/yyyy HH:MM:SS

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python converter_data.py <timestamp>")
        sys.exit(1)

    timestamp = int(sys.argv[1])
    data_formatada = unix_para_data(timestamp)
    print(data_formatada)