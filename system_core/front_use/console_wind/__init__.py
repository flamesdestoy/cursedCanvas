from .console_initter import ConsoleInitializer

__version__ = "1.0.0"
__author__ = "DomainExpandor"

def init_console():
    # Import devs interacting entities
    from .console_p import SubScreenFactory
    
    # Setting up the console window and opening it up
    console = ConsoleInitializer().init_console()

    return console