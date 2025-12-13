import patient_data
import prescription
import config
import flet


controls = [
    patient_data.patient_data_container,
    prescription.prescription_container,
]


def main(
    page: flet.Page,
) -> None:
    patient_data.patient_data_container.height = config.card_height
    prescription.prescription_container.height = config.card_height
    page.vertical_alignment=flet.MainAxisAlignment.CENTER
    page.scroll = None
    cards_row = flet.Row(
        controls,
    )
    create_order_row = flet.Row(
        [flet.FilledButton('Create order', expand=True)]
    )
    page.add(cards_row)
    page.add(create_order_row)
