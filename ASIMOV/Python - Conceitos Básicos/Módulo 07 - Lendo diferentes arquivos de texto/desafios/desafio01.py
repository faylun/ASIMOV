from pathlib import Path

current_folder = Path(__file__).parent

def update_html(name):
    with open(current_folder / 'view_lista.html') as html_list:
        item_list = html_list.readlines()

    with open(current_folder / 'view_lista_atualizada.html', mode='w') as new_list:
        for i, item in enumerate(item_list):
            if item.strip() == name:
                item_list.pop(i - 2)
                item_list.pop(i - 2)
                item_list.pop(i - 2)
        new_list.writelines(item_list)

update_html('Ir ao shopping')