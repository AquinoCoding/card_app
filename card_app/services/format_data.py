from datetime import datetime

def formata_data(data: datetime) -> str:
    return data.strftime("%d/%m/%Y às %H:%M:%S")