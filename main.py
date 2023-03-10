"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, querying of the database and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any database related querying should be done using the appropriate functions the module 'database'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""

# Task 10: Import required modules
import csv
import tui
import process as p
import database
import visual

# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.
covid_records = []


def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should be a record in the list 'covid_records'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many records have
    # been loaded and that the data loading operation has completed.
    tui.progress("Data loading", 0)
    print()

    path_name = "data/covid_19_data.csv"
    try:
        with open(path_name) as file:
            csv_reader = csv.reader(file)
            headings = next(csv_reader)
            for records in csv_reader:
                covid_records.append(records)
    except IOError:
        print("Cannot read the file")

    tui.progress("Data loading", 0)
    print(f"{len(covid_records)} records have been loaded")

    tui.progress("Data loading", 100)

    while True:
        # Task 14: Using the appropriate function in the module 'tui', display a menu of options
        # for the different operations that can be performed on the data (menu variant 0).
        # Assign the selected option to a suitable local variable
        user_input = tui.menu()

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #   - If the user selected the option to retrieve an individual record by serial number then
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve (multiple) records by observation dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve records with
        #       - Use the appropriate function in the module 'tui' to display the retrieved records.
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group records by country/region then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the records
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the records then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the records.
        #       - Use the appropriate function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        if user_input == 1:
            tui.progress("Data processing", 0)
            print(f"Your option is:{user_input}")
            print()
            user_fills = tui.menu(1)
            if user_fills == 1:
                tui.progress("Retrieving record by serial number", 0)
                record = p.record_by_serial(covid_records)
                print("The record with serial number specified is:\n")
                tui.display_record(record)
                tui.progress("Retrieving record by serial number", 100)
            elif user_fills == 2:
                tui.progress("Retrieving records by observation dates", 0)
                records = p.records_with_obs_dates(covid_records)
                print("These are the records with the observation dates you specified:\n")
                tui.display_records(records)
                tui.progress("Retrieving records by observation dates", 100)
            elif user_fills == 3:
                tui.progress("Grouping records by country", 0)
                data = p.records_by_country_region(covid_records)
                tui.display_records(data)
                tui.progress("Grouping records by country", 100)
            elif user_fills == 4:
                tui.progress("Collating records summary", 0)
                feed = p.ret_summary(covid_records)
                tui.display_records(feed)
            else:
                tui.error("Invalid option")

        # Task 21: Check if the user selected the option for setting up or querying the database.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has started.
        # - Query the database by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what querying is to be done.
        #   - call the appropriate function in the module 'database' to retrieve the results
        #   - call the appropriate function in the module 'tui' to display the results
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # database querying operation has completed.
        elif user_input == 2:
            user_in = tui.menu(2)
            if user_in == 1:
                tui.progress("Database setup", 0)
                database.set_database(covid_records)
                tui.progress("Database setup", 100)
            elif user_in == 2:
                tui.progress("Retrieving countries' names", 0)
                names = database.ret_c_names()
                tui.display_record(names)
                tui.progress("Retrieving countries' names", 100)
            elif user_in == 3:
                tui.progress("Retrieving confirmed,death,recovery cases", 0)
                info = database.retrieve_all()
                for record in info:
                    print(f"Confirmed:{record[0]}, Deaths:{record[1]}, Recovered:{record[2]}")
                tui.progress("Retrieving confirmed, death, recovery cases", 100)
            elif user_in == 4:
                tui.progress("Retrieving top 5 countries for confirmed cases", 0)
                load = database.retrieve_top5()
                tui.display_records(load)
            elif user_in == 5:
                tui.progress("Retrieving top 5 countries for death", 0)
                assets = database.retrieve_top5_det()
                tui.display_records(assets, cols=[8, 4])
                tui.progress("Retrieving top 5 countries for death", 100)
            else:
                tui.error("Invalid option")

        # Task 27: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        elif user_input == 3:
            tui.progress("Data visualisation operation", 0)
            option = tui.menu(3)
            if option == 1:
                visual.display_top5_with_pie()
            elif option == 2:
                visual.display_top5_c_with_bar()
            elif option == 3:
                visual.run()
            else:
                tui.error("Please select appropriate option")
            tui.progress("Data visualization", 100)
        # Task 31: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        elif user_input == 4:
            break

        # Task 32: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        else:
            tui.error("Invalid option")
        pass


if __name__ == "__main__":
    run()
