import patient_data
import prescription
import config
import flet


containers_controls = [
    patient_data.patient_data_container,
    prescription.prescription_container,
]
containers_row = flet.Row(
    containers_controls,
)
create_order_row = flet.Row(
    [flet.FilledButton('Create order', expand=True)]
)


def main(
    page: flet.Page,
) -> None:
    assert page.width
    padding = page.width / 12
    page.padding = flet.padding.only(
        left=padding,
        right=padding,
    )
    patient_data.patient_data_container.height = config.card_height
    prescription.prescription_container.height = config.card_height
    page.vertical_alignment=flet.MainAxisAlignment.CENTER
    page.scroll = None
    page.add(containers_row)
    page.add(create_order_row)
