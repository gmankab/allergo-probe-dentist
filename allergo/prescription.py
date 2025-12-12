import config
import flet


controls = [
    flet.Text('Prescription'),
    flet.Dropdown(
        label='Select Tariff',
        filled=True,
        border=flet.InputBorder.OUTLINE,
        border_color=flet.Colors.TRANSPARENT,
        border_radius=config.border_radius,
        expand=True,
    ),
    flet.Checkbox(label='Lidocaine'),
    flet.Checkbox(label='Articaine'),
    flet.Checkbox(label='Mepivacaine'),
    flet.SearchBar(
        bar_hint_text='Search',
        bar_elevation=0,
        view_elevation=0,
    ),
]


prescription = flet.Card(
    flet.Container(
        content=flet.Column(controls),
        padding=config.padding,
        border_radius=config.border_radius,
    ),
    shape=flet.RoundedRectangleBorder(radius=config.padding),
    height=config.card_height
)
