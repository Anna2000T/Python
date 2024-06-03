from tokenize import Double
import flet as ft

import math


def main(page: ft.Page):
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 100
    page.scroll=ft.ScrollMode.ALWAYS,
    page.title = "Calculator"
    page.bgcolor=ft.colors.GREY_100
    

    
    
    
    def button_clicked(e):
        
        tomb = ["a", "á", "b", "c", "cs", "d", "dz", "dzs", "e", "é", "f", "g", "gy", "h", "i", "í", "j", "k", "l", "ly", "m", "n", "ny", "o", "ó", "ö", "ő", "p", "q", "r", "s", "sz", "t", "ty", "u", "ú", "ü", "ű", "v", "w", "x", "y", "z", "zs",     
                "A", "Á", "B", "C", "Cs", "D", "Dz", "Dzs", "E", "É", "F", "G", "Gy", "H", "I", "Í", "J", "K", "L", "Ly", "M", "N", "Ny", "O", "Ó", "Ö", "Ő", "P", "Q", "R", "S", "Sz", "T", "Ty", "U", "Ú", "Ü", "Ű", "V", "W", "X", "Y", "Z", "Zs","."
                ]
        
        for i in tomb:
            if szam_1.value == i or szam_2.value == i:
                ir_2.value = f"Számot adjon meg!"
                print("hiba")
                break

            else:
                if jel.value == "+":     
                    ir_2.value = f"Eredmény: {float(szam_1.value) + float(szam_2.value)}"   
                
                elif jel.value == "-":
                    ir_2.value = f"Eredmény: {float(szam_1.value) - float(szam_2.value)}"
                
                elif jel.value == "*":
                    ir_2.value =f"Eredmény: {float(szam_1.value) * float(szam_2.value)}"
                    
                elif jel.value == "/":
                    if(float(szam_2.value) == 0):
                        ir_2.value = "Nullával nem osztunk!!"
                    else:
                        ir_2.value = f"Eredmény: {float(szam_1.value) // float(szam_2.value)}"
                else:
                    ir_2.value = "Nem megfelelő a bemenet!"
            
        

      
    
        
   
        page.update()
        
    
    
    ir_2 = ft.Text(size=17)
    
    

    
    szam_1 = ft.TextField(
                    width = 70,
                    height=50,
                    bgcolor=ft.colors.WHITE,
                    border_radius=20,
                    
                    
                    )
    
    szam_2 = ft.TextField(
                    width = 70,
                    height=50,
                    bgcolor=ft.colors.WHITE,
                    border_radius=20,
                    
                    )
    
    
    jel = ft.TextField(
                    width = 70,
                    height=50,
                    bgcolor=ft.colors.WHITE,
                    border_radius=20,
                    
                    )
    
    
    

    sor_1 = ft.Row([
            ft.Container(
                    ft.Text("Kérek egy számot: ",size=18),
                    padding=5,
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,
                    border_radius=10,
                    
                    
                 
                ),
            ft.Container(
                    szam_1,
                    alignment=ft.alignment.center,
                    
                
                ),
        ] 
    )
    
    
    
    
    
  
        
    sor_2 = ft.Row([                
   ft.Container(
                    ft.Text("Kérek egy másik számot: ",size=18),
                    padding=5,
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,  
                    border_radius=10,        
                ),
            ft.Container(
                    szam_2,
                    alignment=ft.alignment.center,                  
            ),
                      
        ] )
        
    
   
 
    sor_3 = ft.Row([           
   ft.Container(
                    ft.Text("Kérek műveleti jelet (+ - / * ): ",size=18),
                    padding=5,
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,
                    border_radius=10,
                    
                 
                ),
            ft.Container(
                    jel,
                    alignment=ft.alignment.center,
                    
            )        
        ])
    
       
    
    
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked,width=120,bgcolor=ft.colors.GREY_600,color=ft.colors.WHITE)
    
    
    page.add(
        ft.Column(
            tight=True,
            width=450,
            expand=True,
            spacing=0,
            
            controls=[
                
                ft.Container(
                    sor_1,
                    border=ft.border.only(
                        top=ft.border.BorderSide(3, ft.colors.BLUE_GREY_900),
                        right=ft.border.BorderSide(3,ft.colors.BLUE_GREY_900),
                        left=ft.border.BorderSide(3,ft.colors.BLUE_GREY_900),
                        
                        ),
                    
                    bgcolor=ft.colors.BLUE_GREY_100,
                    padding=20,
                

                    
                ),
                ft.Container(
                    sor_2,
                    bgcolor=ft.colors.BLUE_GREY_100,
                    padding=20,
                    border=ft.border.only(
                        right=ft.border.BorderSide(3, ft.colors.BLUE_GREY_900),
                        left=ft.border.BorderSide(3,ft.colors.BLUE_GREY_900)
                        
                                          ),

                ),
                ft.Container(
                    sor_3,
                    bgcolor=ft.colors.BLUE_GREY_100,
                    padding=20,
                    border=ft.border.only(
                        right=ft.border.BorderSide(3, ft.colors.BLUE_GREY_900),
                        left=ft.border.BorderSide(3,ft.colors.BLUE_GREY_900),
                                          ),

                  
                ),
                ft.Container(
                   ir_2,
                   bgcolor=ft.colors.BLUE_GREY_100,
                   width=450,
                   padding=20,
                   border=ft.border.only(
                       right=ft.border.BorderSide(3, ft.colors.BLUE_GREY_900),
                        left=ft.border.BorderSide(3,ft.colors.BLUE_GREY_900),
                                         ),
           
                ),
                ft.Container(
                   
                   bgcolor=ft.colors.BLUE_GREY_100,
                   padding=20,
                   width=450,
                   border=ft.border.only(bottom=ft.border.BorderSide(3, ft.colors.BLUE_GREY_900),
                                         right=ft.border.BorderSide(3, ft.colors.BLUE_GREY_900),
                        left=ft.border.BorderSide(3,ft.colors.BLUE_GREY_900)),

                  
                ),
                ft.Container(
                   
                   b,
                   alignment=ft.alignment.center,
                   margin=10

                  
                ),
        
                
                    
                    
                
                
                
                
                
            ]
        
        )
        
        
    )
    
    
   
   
        

    
    
    page.update()
    





ft.app(target=main)