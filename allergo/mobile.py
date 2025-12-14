import patient_data
import prescription
import config
import flet


patient_data_row = flet.Row(
    [patient_data.patient_data_container]
)
prescription_row = flet.Row(
    [prescription.prescription_container]
)
create_order_row = flet.Row(
    [flet.FilledButton('Create order', expand=True)]
)


def mobile(
    page: flet.Page,
) -> None:
    page.padding = flet.padding.only(
        left=config.padding,
        right=config.padding,
    )
    patient_data.patient_data_container.height = None
    prescription.prescription_container.height = None
    page.scroll = flet.ScrollMode.AUTO
    page.add(patient_data_row)
    page.add(prescription_row)
    page.add(create_order_row)
