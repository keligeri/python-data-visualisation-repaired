from sql import SQL
from converter import Converter
from image_generator import ImageGenerator


def main():
    input_num = 1

    while input_num != "0":
        print("\n- - - Menu - - -")
        print("1. Company by color")
        print("2. Project name by budget")
        print("3. Bigger than average")
        print("4. Name and status by color")
        print("0. Exit")
        input_num = input("Choose a number: ")

        # ----> Get the company, with count of the project, and a random color from the projects <----
        if input_num == "1":
            # In this case we have to use two different tables
            number_of_project_query = SQL().number_of_proj_by_clients()
            company_by_color_query = SQL().company_by_color()

            number_of_project_ls = Converter(number_of_project_query).number_of_project_by_clients()
            company_by_color_ls = Converter(company_by_color_query).company_by_color()

            company_w_project_and_color = Converter().get_color_by_company(number_of_project_ls, company_by_color_ls)

            # ImageGenerator(data, width=600, height=600, background="white")
            ImageGenerator(company_w_project_and_color, 600, 600, "#e8f2b3").word_cloud_company_size_by_project()

        # ----> Get the project name, order by budget (change the currency to euro) <----
        elif input_num == "2":
            project_name_w_budget_query = SQL().project_name_by_budget()
            project_name_w_budget_ls = Converter(project_name_w_budget_query).project_name_with_budget()
            project_name_w_budget_euro = Converter().change_currency(project_name_w_budget_ls)

            ImageGenerator(project_name_w_budget_euro, 900, 900).word_cloud_project_by_budget()

        # ----> Get that projects, which has bigger budget than the average <----
        elif input_num == "3":
            bigger_than_average_query = SQL().bigger_than_average()
            bigger_than_average_ls = Converter(bigger_than_average_query).bigger_than_average()

            ImageGenerator(bigger_than_average_ls, 900, 900, "black").word_cloud_bigger_than_avg()

        # ----> Get the name and status with different color <----
        elif input_num == "4":
            name_and_status_query = SQL().get_name_and_status()
            get_name_and_status_ls = Converter(name_and_status_query).get_name_status_and_color()
            name_and_status_with_color = Converter().change_color_based_on_status(get_name_and_status_ls)

            ImageGenerator(name_and_status_with_color).word_cloud_name_status_by_color()

        elif input_num == "0":
            break

        else:
            continue

if __name__ == "__main__":
    main()
