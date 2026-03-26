from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
import time
import os

class Python_TUI():
    
    def __init__(self):
        self.prompt_ = Prompt()
        self.console_ = Console()
        self.username_ = ""
        self.passwd_ = ""
        self.Login_ = False
        
    def  clear(self):
        os.system("cls")
        self.Start_()
        
    def login(self):
        login_credential = Panel("Enter your credentials", title="[blink cyan]LOGIN[/blink cyan]")
        while True:
            user = self.prompt_.ask("User")
            if user == "":
                self.console_.print("[blink green]Please enter a Username[/blink  green]")
            else:
                self.username_ = user
                break
            
        
        while True:           
            passw = self.prompt_.ask("password")
            if passw == "":
                self.console_.print("[blink green]Please enter a password![/blink green]")
            elif len(passw) < 8:
                self.console_.print("[blink green]Password should be more than 7 char![/blink green]")
            else:
                self.passwd_ = passw
                self.Login_ = True
                break
    
    def LOGOUT(self):
        if self.Login_ == True:
            self.Login_ = False
            self.console_.print(Panel("[bold]Successfully Logout![/bold]", title="[bold cyan]Notification[/bold cyan]"))
        else:
            self.console_.print(Panel("[bold]IDOIT! You did not Login![/bold]", title="[bold cyan]Notification[/bold cyan]"))

    def user_info(self):
        
        if self.Login_ == True:
            self.console_.print(Panel(f"User: {self.username_}\nPassword: {self.passwd_}", title="[bold red]User_Info[/bold red]"))
        else:
            self.console_.print(Panel(f"Please LOGIN First", title="[bold red]WARNING[/bold red]"))

    
    def Help(self):
        table_cmd = Table(title="HELP COMMAND")

        self.console_.print(Panel("", title="[bold yellow]HELP[/bold yellow]"))
        
        table_cmd.add_column("Command", style="red", justify="left")
        table_cmd.add_column("Description", style="green")

        table_cmd.add_row("hh","> Show Commands Description")
        table_cmd.add_row("login","> To create a User Account")
        table_cmd.add_row("logout","> To logout a User Account")
        table_cmd.add_row("info","> show User Credentials")        
        table_cmd.add_row("qq","> quit Pyhton TUI")
        table_cmd.add_row("clr","> Clear Python TUI")
        table_cmd.add_row("msg: <<message>>", " display message")
        
        self.console_.print(table_cmd)
            
        
    
    def Start_(self):
        Header = Panel("Python TUI", title="[blink red]TITLE[/blink red]")
        
        self.console_.print(Header)
        
        while True:
            header1= Panel("Command Input:", title="Python_TUI")
            tui_input =  self.console_.input("[bold]$ [/bold]").split()
            
            
            if len(tui_input) == 1:
                cmd_tui = tui_input[0]
                
                match cmd_tui:
                    case "clr":
                        self.clear()
                    case "cls":
                        self.console_.print(Panel("[bold yellow]WAHAHHAHA FUCKING IDIOT!![/bold yellow]\n>>THIS IS NOT CMD OR POWERSHELL!", title="[bold cyan]COMPUTER MSG[/bold cyan]"))
                    case "clear":
                        self.console_.print(Panel("[bold yellow]WAHAHHAHA FUCKING IDIOT!![/bold yellow]\n>>THIS IS NOT LINUX", title="[bold cyan]COMPUTER MSG[/bold cyan]"))
                                    
                    case "login":
                        self.login()
                    case "qq":
                        break
                    case "info":
                        self.user_info()
                    case "hh":
                        self.Help()
                    case "logout":
                        self.LOGOUT()
                    case "fuck":
                        self.console_.print(Panel("Oohh~Dont be angry~, IDIOT!!", title="[bold cyan]Computer Message[/bold cyan]"))
                   
            
            elif len(tui_input) >= 2:
                if tui_input[0] == "msg:":
                    msg = tui_input[1:]
                    self.console_.print(Panel(f"{" ".join(msg)}", title="[bold cyan]TEXT[/bold cyan]"))
                else:
                     continue
            else:
               self.console_.print(Panel(f"{tui_input[0]} Command not found!", title="[bold cyan]WARNING[/bold cyan]"))
                    

                    
                    
                    
                    
                    
                
         
if __name__ == "__main__":
    TUI = Python_TUI()
    TUI.Start_()