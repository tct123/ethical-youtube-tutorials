import flet as ft


def main(page: ft.Page):
    page.window.always_on_top = True
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage(
            src="https://images.unsplash.com/photo-1547721064-da6cfb341d50",
            fit=ft.ImageFit.COVER,
            opacity=0.2,
        ),
        gradient=ft.LinearGradient(
            colors=[ft.Colors.RED, ft.Colors.BLUE],
            stops=[0, 1],
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
        ),
    )

    """
    page.foreground_decoration = ft.BoxDecoration(
        image=ft.DecorationImage(
            src="https://images.unsplash.com/photo-1547721064-da6cfb341d50",
            fit=ft.ImageFit.COVER,
            opacity=0.2,
        ),
        gradient=ft.LinearGradient(
            colors=[
                ft.Colors.with_opacity(0.2, ft.Colors.RED),
                ft.Colors.with_opacity(0.2, ft.Colors.BLUE),
            ],
            stops=[0, 1],
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
        ),
    )
    """
    page.add(ft.SafeArea(ft.Text("Hello, Flet!", size=50)))


ft.app(main)
