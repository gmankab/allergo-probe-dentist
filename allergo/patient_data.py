import config
import flet


def text_field(
    hint_text: str,
) -> flet.TextField:
    return flet.TextField(
        hint_text=hint_text,
        filled=True,
        border=flet.InputBorder.OUTLINE,
        border_color=flet.Colors.TRANSPARENT,
        border_radius=config.border_radius,
    )

iin = text_field('IIN')
patient_full_name = text_field('Patient Full Name')
phone = text_field('Phone')
date_of_birth = text_field('Date of Birth')

controls = [
    flet.Text('Patient Data'),
    iin,
    patient_full_name,
    phone,
    date_of_birth,
]

patient_data_card = flet.Card(
    flet.Container(
        content=flet.Column(controls),
        padding=config.padding,
        border_radius=config.border_radius,
    ),
    shape=flet.RoundedRectangleBorder(
        radius=config.border_radius,
    ),
)

patient_data_container = flet.Container(
    content=patient_data_card,
    col={'sm': 12, 'md': 5},
    expand=True,
)
