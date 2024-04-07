import config

from src.utils import create_bd, save_data_bd, user_menu

if __name__ == '__main__':
    employers_ids = ['2391264',  # АО Транснефть-Верхняя Волга
                    '1740',  # Яндекс
                    '1734722',  # ООО ТРАНСНЕФТЬ - ДАЛЬНИЙ ВОСТОК
                    '903198',  # АО НК Роснефть-МЗ Нефтепродукт
                    '1373',  # "Аэрофлот"
                    '39305',  # Газпром нефть
                    '1455',  # HeadHunter
                    '15478',  # VK
                    '1057',  # Лаборатория Касперского
                    '78638'  # Тинькофф
                    ]

    params = config.config()

    create_bd("сoursework5", params)
    save_data_bd(employers_ids, "сoursework5", params)
    user_menu("сoursework5")
