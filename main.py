from storage import DataManager
from interface import AppInterface

#----------------------------- APP SETUP ------------------------------ #
data_manager = DataManager()
app = AppInterface(data_manager)
app.window.mainloop()
# --------------------------------------------------------------------- #
