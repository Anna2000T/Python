import flet as ft
def main(page: ft.Page):

    page.title= "Dolgozat",
    page.scroll = ft.ScrollMode.AUTO


    page.add(ft.Row(controls=[
        ft.Text(value="Hello") ,
        ft.Text(value="World")
        ])

    )

    page.add(
        ft.Container(
            content=ft.Text("A", text_align="center"),
            bgcolor="lightblue",
            height=200,
            width=2000,
            alignment=ft.alignment.center,
            


        ),
    )

    page.add(
        ft.Row(controls=[

            ft.Container(
                width=200,
                height=200,
                bgcolor="yellow"
            ),

            ft.Container(
                width=200,
                height=200,
                bgcolor="blue",
                

            ),


            ft.Container(
                width=200,
                height=200,
                bgcolor="green"
            ),


            ft.Container(
                width=200,
                height=200,
                bgcolor="black"
            ),

            ft.Container(
                width=200,
                height=200,
                bgcolor="red"
            ),




        ])
    )
    
    page.update()



ft.app(target=main)