import config
import flet

controls = [
    flet.Text('Patient Data'),
]

for hint_text in (
    'IIN',
    'Patient Full Name',
    'Phone',
    'Date of Birth',
):
    controls.append(
        flet.TextField(
            hint_text=hint_text,
            filled=True,
            border=flet.InputBorder.OUTLINE,
            border_color=flet.Colors.TRANSPARENT,
            border_radius=config.border_radius,
        )
    )


patient_data_card = flet.Card(
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

patient_data_container = flet.Container(
    content=patient_data_card,
    col={'sm': 12, 'md': 5},
    expand=True,
)
