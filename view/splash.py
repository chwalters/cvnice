from typing import Optional

from glom import glom
from nicegui import ui

from model.application import AppModel

SPLASH_IMAGE_SOURCE="https://deepai.org/machine-learning-model/"

async def splash_content(app_model: AppModel):
    carousel_images = [
        "abstract",
        "cyberpunk",
        "fantasy",
        "hologram",
        "oldtime",
        "origami",
        "zombies"
    ]
    with ui.carousel(
            animated=True,
            arrows=True,
            navigation=True
    ).props(
        'autoplay=true infinite'
    ).classes(
        'row full-width'
    ):
        for carousel_image in carousel_images:
            with ui.carousel_slide().classes('p-0'):
                ui.image(f"images/{carousel_image}.jpeg").classes('w-[100vw]')

    with ui.row().classes('row full-width items-center justify-center'):
        with ui.column().classes('col text-center full-width items-center justify-center'):
            # ui.label(f"{app_model.settings.nomenclature}Nice").classes("text-h1 text-weight-bolder")
            nomenclature: Optional[str] = glom(app_model, "settings.nomenclature", default="CV")
            ui.label(f"because nobody likes writing {nomenclature}s").classes('text-h2')
            ui.label("and you just want to get a job!").classes("text-h3")