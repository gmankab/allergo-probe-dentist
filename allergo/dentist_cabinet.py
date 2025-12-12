import patient_data
import prescription
import config
import flet


patient_data_container = flet.Container(
    content=patient_data.patient_data,
    col={'sm': 12, 'md': 5},
    expand=True,
)
prescription_container = flet.Container(
    content=prescription.prescription,
    col={'sm': 12, 'md': 5},
    expand=True,
)
create_order_button = flet.Container(
    content=flet.FilledButton('Create order', expand=True),
    col={'sm': 12, 'md': 10},
)


def main(page: flet.Page):
    page.padding = flet.padding.only(
        left=config.padding,
        right=config.padding,
    )
    cards_row = flet.ResponsiveRow(
        controls=[patient_data_container, prescription_container],
        alignment=flet.MainAxisAlignment.CENTER,
    )
    button_row = flet.ResponsiveRow(
        controls=[create_order_button],
        alignment=flet.MainAxisAlignment.CENTER,
    )
    column = flet.Column(
        controls=[cards_row, button_row],
        scroll=flet.ScrollMode.AUTO,
    )
    container = flet.Container(
        content=column,
        alignment=flet.alignment.center,
        expand=True,
    )
    page.add(container)
