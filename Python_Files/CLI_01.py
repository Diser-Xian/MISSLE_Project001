import time, psutil
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table


class Usage_veiwer():
    
    def __init__(self):
        self.__network_IO = psutil.net_io_counters()
        self.__cpu_perc = psutil.cpu_percent(interval=1)
        self.__ram_inf = psutil.virtual_memory()
        self.__disk_inf = psutil.disk_usage("/")
        self.__console_ = Console()
        
        
        
    
    def System(self):
        ram_total = "self.__ram_inf.total / (1024**3):.2f"+" GB"
        ram_used = "self.__ram_inf.used / (1024**3):.2f"+" GB"
        ram_avail = "self.__ram_inf.available / (1024**3):.2f"+" GB"

        
        
        table = Table(title = "Storages")
        
        #Column
        table.add_column("unit", style="cyan")
        table.add_column("usage", style="magenta")
        
        
        #Row
        table.add_row("Disk", self.__disk_inf)
        table.add_row("Ram", f"{ram_avail} / {ram_total}")
        
        
        
        self.__console_.print(table)
        


         
      
        
        
        
        
        
CLI = Usage_veiwer()
CLI.System()