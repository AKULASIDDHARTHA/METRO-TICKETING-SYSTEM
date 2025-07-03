import tkinter as tk
from tkinter import messagebox

FARE_PER_STATION = 25

metro_routes = {
    "Red Line": ["LB Nagar", "Victorial memorial", "Chaitanyapuri", "Dilsukhnagar", "Musarambhag"],
    "Blue Line": ["Uppal", "Stadium", "NGRI", "Habsiguda","Trnaka", "Mettuguda","Secunderabad"]
}

PAYMENT_METHODS = ["UPI", "Card", "Cash"]


def generate_ticket():
    route = route_var.get()
    start_index = start_station_var.get()
    destination_index = destination_station_var.get()
    num_tickets = num_tickets_var.get()
    payment_method = payment_method_var.get()


    if not route or not start_index or not destination_index or not num_tickets or not payment_method:
        messagebox.showerror("Input Error", "Please fill in all fields!")
        return

    if start_index == destination_index:
        messagebox.showerror("Input Error", "Starting and destination stations cannot be the same!")
        return

    try:
        num_tickets = int(num_tickets)
        if num_tickets <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of tickets!")
        return

    
    stations = metro_routes[route]
    stations_traveled = abs(stations.index(start_index) - stations.index(destination_index))
    total_fare = stations_traveled * FARE_PER_STATION * num_tickets

    ticket_message = f"""
    --- Metro Ticket Confirmation ---
    Metro Route: {route}
    From: {start_index}  To: {destination_index}
    Number of Tickets: {num_tickets}
    Total Fare: ₹{total_fare}
    Payment Mode: {payment_method}

    Thank you for using the Metro! Have a safe journey.
    
    """
    messagebox.showinfo("Ticket Confirmation", ticket_message)

root = tk.Tk()
root.title("Metro Ticketing System")
root.geometry("400x400")

tk.Label(root, text="Select Metro Route:").pack()
route_var = tk.StringVar()
route_menu = tk.OptionMenu(root, route_var, *metro_routes.keys())
route_menu.pack()

tk.Label(root, text="Select Starting Station:").pack()
start_station_var = tk.StringVar()
start_menu = tk.OptionMenu(root, start_station_var, "")
start_menu.pack()

tk.Label(root, text="Select Destination Station:").pack()
destination_station_var = tk.StringVar()
destination_menu = tk.OptionMenu(root, destination_station_var, "")
destination_menu.pack()

tk.Label(root, text="Enter Number of Tickets:").pack()
num_tickets_var = tk.Entry(root)
num_tickets_var.pack()

tk.Label(root, text="Select Payment Method:").pack()
payment_method_var = tk.StringVar()
payment_menu = tk.OptionMenu(root, payment_method_var, *PAYMENT_METHODS)
payment_menu.pack()

def update_stations(*args):
    route = route_var.get()
    if route:
        stations = metro_routes[route]

       
        start_menu["menu"].delete(0, "end")
        for station in stations:
            start_menu["menu"].add_command(label=station, command=tk._setit(start_station_var, station))
        
        
        destination_menu["menu"].delete(0, "end")
        for station in stations:
            destination_menu["menu"].add_command(label=station, command=tk._setit(destination_station_var, station))

route_var.trace("w", update_stations)


tk.Button(root, text="Generate Ticket", command=generate_ticket).pack()


root.mainloop()