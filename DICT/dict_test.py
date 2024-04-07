menu = {'Book': 300, 'Pen': 45, 'Notebook': 60, 'Geometry Box': 100, 'Markers': 50, 'Ruler': 15,'Colour Pencils': 200}
print(menu)
lower_keys = {}
for i in menu:
    lower_keys = {i.lower(): menu[i] for i in menu}
print(lower_keys)
