#----------style.py----------
from performer.unsunghero import UnsungHero

parent_dir = UnsungHero.parent_dir

#------Window Style------
window_style = {
    'return_keyboard_events': True,
    'keep_on_top': True,
    'titlebar_font': ('sf ui display bold',20),
    'titlebar_icon': f"{parent_dir('images')}/titlebar_icon.png",
    'use_custom_titlebar': True,
    'grab_anywhere': False,
    }

#------Tab Select Style------
select_style = {
    'font': ('sf ui display bold', 16),
    'size': (6,1),
    'justification': 'left',
    'text_color': "#5f5f5f",
    'enable_events': True,
    }

selected_style = {
    'font': ('sf ui display bold', 16),
    'size': (6,1),
    'justification': 'left',
    'text_color': "#ffffff",
    'enable_events': True,
    }

#------Table Style------
table_style = {
    "font": ('sf ui display light', 14),
    "header_font": ('sf ui display bold', 14),
    "num_rows": 5,
    "hide_vertical_scroll": True,
    "headings": ["   TAG   ", "   CODE   ", " PRICE ", " UNITS "],
    "enable_events": True,
}

#------Analyze------
analyze_table_style = {
    "font": ('sf ui display light', 13),
    "header_font": ('sf ui display bold', 13),
    "num_rows": 5,
    "hide_vertical_scroll": True,
    "headings": ["     TAG     ", "   SALES   "],
}

analyze_listbox_style = {
    "enable_events": True,
    "font": ("sf ui display light",13),
    "size": (23,4),
    "readonly": True
}