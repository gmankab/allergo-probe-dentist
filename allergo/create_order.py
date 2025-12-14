import patient_data
import flet
import qr


create_order_button = flet.FilledButton(
    'Create order',
    expand=True,
    disabled=True,
    on_click=qr.show_qr,
)
create_order_row = flet.Row(
    [create_order_button]
)


def update_create_order(
    _ = None,
) -> None:
    create_order_button.disabled = not bool(patient_data.phone.value)
    create_order_button.update()

patient_data.phone.on_change=update_create_order
