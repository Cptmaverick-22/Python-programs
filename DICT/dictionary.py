menu = {'Book': 300, 'Pen': 45, 'Notebook': 60, 'Geometry Box': 100, 'Markers': 50, 'Ruler': 15,
            'Colour Pencils': 200}
print(menu)
menu_lower = {i.lower(): menu[i] for i in menu}
print(menu_lower)