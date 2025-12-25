import patient_data
import config
import base64
import qrcode
import flet
import io


class url:
    pretty: str
    full: str


def open_url(_=None):
    config.page.launch_url(
        url.full,
        web_window_name='_blank',
    )


def gen_qr(
    url: str
) -> str:
    buf = io.BytesIO()
    qrcode.make(url).save(buf)
    return base64.b64encode(buf.getvalue()).decode('utf-8')


def close_dialog(
    _ = None,
):
    dialog.open = False
    config.page.update()


close_button = flet.FilledButton(
    'Close',
    on_click=close_dialog,
)

title = flet.Text(
    'Show this qr to the patient',
    text_align=flet.TextAlign.CENTER,
)

url_button = flet.TextButton(
    on_click=open_url,
)

image = flet.Image(
    filter_quality=flet.FilterQuality.NONE,
)

column = flet.Column(
    controls=[
        title,
        image,
        url_button,
        close_button,
    ],
    horizontal_alignment=flet.CrossAxisAlignment.STRETCH,
    tight=True,
)

dialog = flet.AlertDialog(
    modal=True,
    content=column,
)


def show_qr(
    _ = None,
) -> None:
    global url
    assert patient_data.phone
    assert patient_data.phone.value
    url.pretty = f'AllergoProba.kz/order/{patient_data.phone.value}'
    url.full = f'https://{url.pretty}'
    image.src_base64 = gen_qr(url.full)
    url_button.text = url.pretty
    dialog.open = True
    config.page.update()
