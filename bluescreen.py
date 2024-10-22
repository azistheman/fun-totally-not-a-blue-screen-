import tkinter as tk
import time

def show_blue_screen():
    # Create a full-screen window to simulate a blue screen
    blue_screen = tk.Tk()
    blue_screen.title("Blue Screen of Death Simulation")

    # Make the window fullscreen and hide the cursor
    blue_screen.attributes("-fullscreen", True)
    blue_screen.config(cursor="none")

    # Set background to Windows BSOD blue color
    blue_screen.configure(background="#0078D7")

    # Get the screen dimensions
    screen_width = blue_screen.winfo_screenwidth()
    screen_height = blue_screen.winfo_screenheight()

    # Add the Windows 11 BSOD sad face
    sad_face = tk.Label(blue_screen, text=":(", fg="white", bg="#0078D7", font=("Segoe UI Emoji", 150))
    sad_face.place(relx=0.2, rely=0.2, anchor="center")  # Position closer to top-left

    # Add the Windows BSOD message
    message = tk.Label(blue_screen, text="Your PC ran into a problem and needs to restart.\n"
                                         "We're just collecting some error info, and then we'll restart for you.",
                       fg="white", bg="#0078D7", font=("Segoe UI", 26), justify="left")
    message.place(relx=0.5, rely=0.4, anchor="center")  # Centered message below sad face

    # Add percentage complete text
    percentage = tk.Label(blue_screen, text="0% complete", fg="white", bg="#0078D7", font=("Segoe UI", 24))
    percentage.place(relx=0.5, rely=0.5, anchor="center")  # Positioned just below the main message

    # Add additional BSOD details (stop code and troubleshooting info)
    stop_code_message = tk.Label(blue_screen, text="For more information about this issue and possible fixes, visit our website.\n"
                                                   "If you call a support person, give them this info:\n"
                                                   "Stop code: 0x00000000",
                                 fg="white", bg="#0078D7", font=("Segoe UI", 16), justify="left")
    stop_code_message.place(relx=0.5, rely=0.65, anchor="center")  # Placed lower on the screen

    # Simulate the percentage count for a more authentic feel
    def update_percentage():
        for i in range(1, 101):
            percentage.config(text=f"{i}% complete")
            blue_screen.update()
            time.sleep(0.05)  # Adjust speed for the percentage increment

    blue_screen.after(1000, update_percentage)  # Start percentage after 1 second

    # Close the blue screen after 10 seconds (enough time for percentage to reach 100%)
    blue_screen.after(10000, blue_screen.destroy)
    blue_screen.mainloop()

# Simulate blue screen
show_blue_screen()

# Once the blue screen is closed, normal functionality resumes
print("Blue screen simulation completed. Back to normal.")
