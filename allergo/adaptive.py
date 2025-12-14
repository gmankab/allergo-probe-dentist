import desktop
import mobile
import config
import flet


def adapt(
    _ = None,
) -> None:
    config.page.clean()
    assert config.page.width
    if config.page.width < 768:
        mobile.mobile(config.page)
    else:
        desktop.desktop(config.page)


def main(
    page: flet.Page,
) -> None:
    config.page = page
    page.on_resized=adapt
    adapt()

