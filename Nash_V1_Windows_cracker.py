from WinCark_Modules import *

def app():
    print("Welcome to Nash_V1_Windows_Cracker ")
    print("See the readme for more information")
    command = input("What do you want to know  : ")
    if command == "Hardware":
        hardware()
    elif command == "TCP":
        Tcp()
    elif command == "Network_ping":
        Network_ping()
    elif command == "IPV4":
        IPV4()
    elif command == "Target_Info":
        Target_Info()
    elif command == "HTTP":
        HTTP()
    elif command == "Website_trace":
        Website_trace()
    elif command == "Network_status":
        Network_status()
    elif command == "enegry_reports":
        enegry_reports()
    elif command == "Firewall":
        Firewall()
    elif command == "Security":
        Security()

app()
        
