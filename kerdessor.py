import flet as ft
import hashlib
import random


def main(page: ft.Page):

    page.title = "Quiz project"
    page.scroll=ft.ScrollMode.ALWAYS
    page.padding = 70
    page.bgcolor = ft.colors.BLUE_50
    page.spacing = 20



    def button_clicked(e):
        
        pont = 0        
        if kerdes_1.value == "Amazonas":
            pont+=1
            kerdes_1.border_color="black"
        else:
            kerdes_1.border_color="red"
            
            
            
            
        if kerdes_2.value == "Madrid":
            pont+=1
            kerdes_2.border_color="black"
        else:
            kerdes_2.border_color="red"
            
            
        if leporgo.value == "Joanne Kathleen Rowling":
            pont += 1
            leporgo.border_color="black"
        else:
            leporgo.border_color="red"
            
            
        
        if szuperman.value == "Superman" or szuperman.value == "superman":
            pont += 1
            szuperman.border_color="black"
        else:

            szuperman.border_color="red"
            
        
        if cg.value == "Cristoforo Colombo":
            pont += 1

                 
      
            
        
        if kerdes_3.value == "1492":
            pont+=1
            kerdes_3.border_color="black"
            print(pont)
        else:
            kerdes_3.border_color="red"
            
        
        if (oszlop_valasz_1.value == True and oszlop_valasz_4.value == True) and (oszlop_valasz_2.value == False or oszlop_valasz_3.value == False or oszlop_valasz_5.value == False):
            pont+=1
            print(pont)
            
        
        if leporgo_2.value == "Gigabyte":
            pont+=1
            print(pont)
            leporgo_2.border_color="black"
        else:
            leporgo_2.border_color="red"
            
            
            

            
        
        if pont <= 0:
            valasz.value = f"You didn't get any point.... {pont}"
        elif 0 < pont < 4:
            valasz.value = f"Nice, keep going! {pont}"
        elif 4 <= pont < 7:
            valasz.value = f"Good job! {pont}"
        elif pont >= 7:
            valasz.value = f"Excellent work! {pont}"
        
            
        
        
        
            
        
            
        
        
        
        
        page.update()
            
            
        
        
        
    
    valasz = ft.Text()
    

    page.add(
        ft.Row(controls=[
            
        ft.Text(value="Questions", 
                size=20,
                text_align= ft.TextAlign.CENTER),
        ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.PINK),
        ])
        
    )
    
    

    kerdes_1 = ft.TextField(label="",width=250)  
    kerdes_2 = ft.TextField(label="",width=250)
    kerdes_3 = ft.TextField(label="",width=250)
    
    
    hossz = (
        ft.Column([
            ft.Container(
                    ft.Text("What is the longest river in the world? ",size= 15),
                    padding=5,
              
                ),
            ft.Container(
                    kerdes_1,
                    
                
                ),
        ] 
    )
    )
    
    
    
    hossz_2 = (
        ft.Column([
        
            ft.Container(
                    ft.Text("What is the capital city of Spain? ",size= 15),
                    padding=5,
                    
                    
                 
                ),
            ft.Container(
                    kerdes_2,
                    
                
                ),
            
        ] 
    )
    )
  
    
    
   

    leporgo = ft.Dropdown(
            label="Who wrote the Harry Potter books? ",
            width=300,
        
        options=[
            ft.dropdown.Option("George Orwell"),
            ft.dropdown.Option("Joanne Kathleen Rowling"),
            ft.dropdown.Option("Robin Cook"),
            ft.dropdown.Option("Harlan Ellison"),
        ],
        )
    
    
    kep =(
        ft.Image(src=f"Superman_Vol_5_1_Textless.jpg",width=250,height=250)
        
        )
    szuperman = (ft.TextField(width=200))
    
  
    
    szuperman_2 = ft.Column(
        controls=[
            ft.Container(
                ft.Text("Who is this?"),
                
            ),
            ft.Container(
                
                szuperman
                
            ),
            ft.Container(
            
                kep
                
            ),
            
        ]    
        
    )
    
    
    ker_9 = ft.Text(value="Who discovered America? ",size= 15)
    

    cg = ft.RadioGroup(content=ft.Column([
    ft.Radio(value="Amerigo Vespucc", label="Amerigo Vespucc"),
    ft.Radio(value="Vasco da Gama", label="Vasco da Gama"),
    ft.Radio(value="Cristoforo Colombo", label="Cristoforo Colombo")]))
    
    
    
    
    ker_3 = ft.Text(value="Who are the members of the European Union? ",size= 15)
    
   
    oszlop_valasz_1 = ft.Checkbox(label="Austria")
    oszlop_valasz_2 = ft.Checkbox(label="Izland")
    oszlop_valasz_3 = ft.Checkbox(label="Norway")
    oszlop_valasz_4 = ft.Checkbox(label="Italy")
    oszlop_valasz_5 = ft.Checkbox(label="Switzerland")
  
    
    
    
    hossz_5 = (
        ft.Column([
            ft.Container(
                    ft.Text("When did they discover America? ",size= 15),
                    padding=5,
                    
                    
                    
                 
                ),
            ft.Container(
                    kerdes_3,
                    
                
                ),
        ] 
    )
    )
    
    
    
    
    
    leporgo_2 = ft.Dropdown(
            label="Which one is written correctly?",
            width=300,
        
        options=[
            ft.dropdown.Option("Gigabite"),
            ft.dropdown.Option("Gigabyte"),
            ft.dropdown.Option("Gygabite"),
            ft.dropdown.Option("Gygabyte"),
        ],
        )
    

    
    
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    
    
    page.add(leporgo,hossz,hossz_2,szuperman_2,ker_9,cg,ker_3,oszlop_valasz_1,oszlop_valasz_2,oszlop_valasz_3,oszlop_valasz_4,oszlop_valasz_5,hossz_5,leporgo_2,b,valasz),
 




    page.update()





ft.app(target=main)