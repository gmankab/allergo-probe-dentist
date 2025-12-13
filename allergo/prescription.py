import config
import flet


tariff_options = [
    flet.DropdownOption('tariff1'),
    flet.DropdownOption('tariff2'),
]

tariff_dropdown = flet.Dropdown(
    hint_text='Select Tariff',
    filled=True,
    border=flet.InputBorder.OUTLINE,
    border_color=flet.Colors.TRANSPARENT,
    border_radius=config.border_radius,
    expand=True,
    options=tariff_options
)

controls = [
    flet.Text('Prescription'),
    tariff_dropdown,
    flet.Checkbox(label='Lidocaine'),
    flet.Checkbox(label='Articaine'),
    flet.Checkbox(label='Mepivacaine'),
    flet.SearchBar(
        bar_hint_text='Search',
        bar_elevation=0,
        view_elevation=0,
    ),
]


prescription_card = flet.Card(
    flet.Container(
        content=flet.Column(controls),
        padding=config.padding,
        border_radius=config.border_radius,
    ),
    shape=flet.RoundedRectangleBorder(
        radius=config.border_radius,
    ),
    height=config.card_height,
)

prescription_container = flet.Container(
    content=prescription_card,
    col={'sm': 12, 'md': 5},
    expand=True,
)
