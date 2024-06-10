import flet as ft 
HEIGHT = 800
WIDTH = 400
btn = ft.IconButton(icon=ft.icons.MIC,icon_color="BLACK"),
text = ft.Text(value = "18/400 apna gokuldham , pleasant park,\n andheri(w)",color="BLACK",italic=True,size=10)
def homePage(page : ft.Page):
    home_Page = ft.Container(
        height = HEIGHT,
        width = WIDTH,
        bgcolor=ft.colors.YELLOW_100,
        padding=ft.padding.only(0,20,0,0),
        border_radius=20,
        content=
            ft.Column(
                controls=[
                    ft.Container(height=30),
                    ft.Row(
                        controls=[
                                ft.Container(width=30),
                                ft.IconButton(
                                    icon=ft.icons.PERSON_2_ROUNDED,
                                    icon_size=70,
                                    bgcolor="white",
                                    icon_color="BLACK",
                                    style=ft.ButtonStyle(
                                        side={
                                            ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLACK),
                                        },
                                        
                                    ),
                                    
                                ),
                                ft.Container(height=30),
                                ft.TextButton(
                                    content=ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.Text(value="Address",size=18,italic=True,color=ft.colors.BLACK),
                                                    text
                                                ],
                                                alignment=ft.MainAxisAlignment.END,
                                                spacing=5,
                                            ),
                                            padding=ft.padding.all(10),
                                            ),
                                    expand=True,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=1),
                                    )
                                    ),
                                ft.Container(width=10)
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Container(height=20),
                    ft.Row(
                        controls=[
                            ft.Container(
                                width=350,
                                bgcolor=ft.colors.TRANSPARENT,
                                content=ft.SearchBar(
                                bar_hint_text=("search here......"),
                                view_elevation=4,
                                expand=True,
                                width = 30,
                                bar_bgcolor=ft.colors.WHITE,
                                bar_leading=ft.IconButton(icon=ft.icons.SEARCH,icon_color="BLACK",alignment=ft.alignment.center_right),
                                view_surface_tint_color="White",
                                view_side=ft.border_radius.all(10),
                                bar_trailing=btn,
                                view_bgcolor="White",
                                divider_color=ft.colors.BACKGROUND,
                                controls=[
            ft.ListTile(
                leading=ft.Image(
                    src="food App/assests/Domino's.png",
                    fit=ft.ImageFit.FILL,
                    width=40
                    ),
                title=ft.Text("Dominos",color="Black",weight=ft.FontWeight.BOLD),
                subtitle=ft.Text(value="Restaurant",color="Black",size=10),
                trailing=ft.Icon(ft.icons.RESTAURANT,size=13),
                icon_color="BLack",
                hover_color="Blue",
                ),
            
            ft.ListTile(
                leading=ft.Image(
                    src = "food App/assests/Mcdonalds.png",
                    width=40,
                ),
                title=ft.Text("Mcdonald's",color="Black",weight=ft.FontWeight.BOLD),
                subtitle=ft.Text(value="Restaurant",color="Black",size=10),
                trailing=ft.Icon(ft.icons.RESTAURANT,size=13),
                icon_color="BLACK",
                hover_color="Blue",
            ),
            ft.ListTile(
                leading=ft.Image(
                    src = "food App/assests/biryani.png",
                    width=40,
                ),
                title=ft.Text("Biryani",color="Black",weight=ft.FontWeight.BOLD),
                subtitle=ft.Text(value="Dish",color="Black",size=10),
                trailing=ft.Icon(ft.icons.RICE_BOWL,size=13),
                icon_color="BLACK",
                hover_color="Blue",
            ),
            ft.ListTile(
                leading=ft.Image(
                    src = "food App/assests/pizza.png",
                    width=40,
                ),
                title=ft.Text("pizza",color="Black",weight=ft.FontWeight.BOLD),
                subtitle=ft.Text(value="Food",color="Black",size=10),
                trailing=ft.Icon(ft.icons.LOCAL_PIZZA_OUTLINED,size=13),
                icon_color="BLACK",
                hover_color="Blue",
            )
        ],
                            )
                            )
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Container(height=10),
                    ft.Container(
                        bgcolor=ft.colors.TRANSPARENT,
                        height=150,
                        border_radius=ft.border_radius.all(20),
                        padding=10,
                        content=ft.Column(
                            controls=[
                                ft.Container(width=30),
                                ft.Text(value="  Top picks......",italic=True,color="black"),
                                ft.Container(height=10),
                                ft.Row(
                            expand=1,
                            scroll="always",
                            controls=[
                                ft.Container(width=10),
                                ft.Image(
                                    src = "food App/assests/icecream.png",
                                    fit=ft.ImageFit.FILL,
                                    height=60,
                                    width=60,
                                ),
                                ft.Container(width=10),
                                ft.Image(
                                    src = "food App/assests/cake.png",
                                    fit=ft.ImageFit.FILL,
                                    height=60,
                                    width=60,
                                ),
                                ft.Container(width=10),
                                ft.Image(
                                    src = "food App/assests/pizza.png",
                                    fit=ft.ImageFit.FILL,
                                    height=60,
                                    width=60,
                                ),
                                ft.Container(width=10),
                                ft.Image(
                                    src = "food App/assests/biryani.png",
                                    fit=ft.ImageFit.FILL,
                                    height=60,
                                    width=60,
                                ),
                                ft.Container(width=10),
                                ft.Image(
                                    src = "food App/assests/noodles.png",
                                    fit=ft.ImageFit.FILL,
                                    height=60,
                                    width=60,
                                ),
                                ft.Container(width=10),
                                ft.Image(
                                    src = "food App/assests/paratha.png",
                                    fit=ft.ImageFit.FILL,
                                    height=60,
                                    width=60,
                                ),
                                ft.Container(width=10),
                                ft.Image(
                                    src = "food App/assests/Pav-Bhaji.png",
                                    fit=ft.ImageFit.FILL,
                                    height=60,
                                    width=60,
                                ),
                            ]
                        ),
                            ],alignment=ft.MainAxisAlignment.CENTER
                        )
                    ),
                    ft.Text(value="    Top deals......",italic=True,color="black"),
                    ft.Row(
                        controls=[
                    ft.Container(width=30),
                    ft.Container(
                        height=270,
                        width=300,
                        bgcolor=ft.colors.TRANSPARENT,
                        expand=1,
                        content=
                        ft.Column(
                            scroll=ft.ScrollMode.ALWAYS,
                            on_scroll_interval=0,
                            controls=[
                                ft.Image(
                                    src="food App/assests/kfc.png",
                                    fit = ft.ImageFit.FILL,
                                    height=250,
                                    width=300,
                                    border_radius=20
                                ),
                                ft.Image(
                                    src="food App/assests/little king.png",
                                    fit = ft.ImageFit.FILL,
                                    height=250,
                                    width=300,
                                    border_radius=20,
                                ),
                                ft.Image(
                                    src="food App/assests/subway.png",
                                    fit = ft.ImageFit.FILL,
                                    height=250,
                                    width=300,
                                    border_radius=20,
                                ),
                                ft.Image(
                                    src="food App/assests/theobroma.png",
                                    fit = ft.ImageFit.FILL,
                                    height=250,
                                    width=300,
                                    border_radius=20,
                                ),
                            ]
                        )
                        ),
                            ],
                    ),
                        ft.CupertinoNavigationBar(
                            height = 59,
                            width=700,
                            active_color="BLACK",
                            inactive_color = "Grey",
                            bgcolor="White",
                            border=ft.border.all(color="Black"),
                            destinations=[
                                ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                                ft.NavigationDestination(icon=ft.icons.DISCOUNT, label="Commute"),
                                ft.NavigationDestination(icon=ft.icons.FASTFOOD,label="FOOD"),
                                ft.NavigationDestination(icon=ft.icons.PERSON_2_ROUNDED,label="Profile"),
                            ]
                        )
                ]
            )
    )
    page.add(home_Page)
ft.app(target=homePage,assets_dir="assets",)