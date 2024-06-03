import flet as ft
import random 


def main(page: ft.Page):

    page.title = "Form project"
    page.scroll=ft.ScrollMode.ALWAYS
    page.bgcolor=ft.colors.AMBER_50
    page.spacing = 20
    page.padding = 50

    def button_clicked(e):
        
        
        
        if szinek.value:
            ir_3.value = f"Your favorite color: {szinek.value}",
        else:
            ir_3.value = "You didn't choose any color!"
            
        if ker.value and ker_2.value:
            ir.value = f"Full name:  {ker.value}  {ker_2.value}.",
        else:
            ir.value = "Please enter your name!"
            
            
        if leporgo.value:
            ir_2.value = f"You feel: {leporgo.value}"
        else:
            ir_2.value = "You don't feel anything?"
            
            
        
        kaja = ""
        
        
        for i in str(etelek.controls):
            if i == True:
                kaja += i
                ir_4.value = f"Your favorite food {kaja}"
            else:
                ir_4.value = f"You didn't choose anything....."
            
        
          
                




                  
        page.update()
        
        
    
    
    
 
    
    
    
    page.add(
        ft.Text(value="From", 
                size=20,
                text_align= ft.TextAlign.CENTER),
        
    )
    
    ir = ft.Text()
    ir_2 = ft.Text()
    ir_3 = ft.Text()
    ir_4 = ft.Text()
    
    
    page.add(ft.Text(value="Please enter your name: ", size=20))
    
    ker = ft.TextField(label="Enter your surname",width=250)    
    ker_2 = ft.TextField(label="Enter your last name",width=250)
    ker_3 = ft.Text(value="Select your favorite foods: ",size= 20)
    
    
    
 
    
    etelek  = ft.Column(controls=[
    ft.Checkbox(label="Spagetti",value="Spagetti",),
    ft.Checkbox(label="Pizza",value="Pizza"),
    ft.Checkbox(label="French fries",value="French fries"),
    ft.Checkbox(label="Hotdog",value="Hotdog"),
    ft.Checkbox(label="Ice cream",value="Ice cream"),
    ])
 
 
    
    ker_9 = ft.Text(value="Select your favorite color: ",size=20)
    
    szinek = ft.RadioGroup(content=ft.Column([
    ft.Radio(label="red",value="red"),
    ft.Radio(label="green",value="green"),
    ft.Radio(label="blue",value="blue"),
    ft.Radio(label="pink",value="pink"),
    ft.Radio(label="black",value="black")
      
    ]))
    


    leporgo = ft.Dropdown(
            label="How do you feel? ",
            width=300,
        
        options=[
            ft.dropdown.Option("Sad"),
            ft.dropdown.Option("Happy"),
            ft.dropdown.Option("Depressed"),
            ft.dropdown.Option("Lazy"),
            ft.dropdown.Option("Bored"),
        ],
        )
    
    
    
    
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    
    
    page.add(ker,ker_2,ker_3,etelek,ker_9,szinek,leporgo,ir,ir_2,ir_3,ir_4,b),
    
    page.update()





ft.app(target=main)