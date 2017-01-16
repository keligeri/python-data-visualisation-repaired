import psycopg2
import random

"""
    - egy függvény csak egy dolgot csináljon!!! PL: company_by_color
        - legyen egy, ami csak átváltja a pénznemeket
        - erre mondta Laci, hogy lehetne egy külön class, ami nem csinál semmit (ezt még nem csináltam meg) 
          csak a nevek érthetősége miatt létezne (nem line[0] lenne hanem x.currency pl)
"""


class Converter:
    """This is the controller class. This include the connect to the database, and call the SQL class methods, then\
    create some data manipulation"""

    def __init__(self, query=None):
        self.query = query
        # use our connection values to establish a connection
        self.conn = psycopg2.connect("dbname='keli' user='keli' host='localhost' password='*******'")
        # set autocommit option, to do every query when we call it
        self.conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        self.cursor = self.conn.cursor()

    def bigger_than_average(self):
        # execute the query
        self.cursor.execute(self.query)
        # Fetch and print the result of the last execution
        rows = self.cursor.fetchall()
        return rows

    def company_by_color(self):
        self.cursor.execute(self.query)
        rows = self.cursor.fetchall()
        return rows

    def get_color_by_company(self, number_of_project_ls, company_by_color_ls):
        # Data manipulations
        company_by_color_dict = {}

        for line in company_by_color_ls:
            if line[1] not in company_by_color_dict:
                company_by_color_dict[line[1]] = line[2]
            else:
                company_by_color_dict[line[1]] += "," + line[2]

        company_by_random_color_ls = []

        for key, value in company_by_color_dict.items():
            current_value = value.split(",")
            company_by_random_color_ls.append([key, random.choice(current_value)])

        # iterate over the result list (company_name, project_number)
        for line in number_of_project_ls:
            # iterate over company_by_random_color (company_name, main_color)
            for index, company in enumerate(company_by_random_color_ls):
                # if the company_name is in the company_by_random_color that time append project count
                if line[0] in company:
                    company_by_random_color_ls[index].append(line[1])

        return company_by_random_color_ls

    def number_of_project_by_clients(self):
        self.cursor.execute(self.query)
        rows = self.cursor.fetchall()
        return rows

    def project_name_with_budget(self):
        self.cursor.execute(self.query)
        rows = self.cursor.fetchall()
        return rows

    def change_currency(self, project_name_w_budget_ls):
        project_name_by_budget = []

        for line in project_name_w_budget_ls:
            if line[3] == "GBP":
                project_name_by_budget.append([line[1], (line[2] * 1.15212953), line[5]])
            elif line[3] == "USD":
                project_name_by_budget.append([line[1], (line[2] * 0.947404821), line[5]])
            else:
                project_name_by_budget.append([line[1], line[2], line[5]])

        return project_name_by_budget

    def get_name_status_and_color(self):
        self.cursor.execute(self.query)
        rows = self.cursor.fetchall()
        return rows

    def change_color_based_on_status(self, name_status_color_ls):
        name_status_ls = []

        for line in name_status_color_ls:
            if line[1] == 1:
                name_status_ls.append([line[0], line[1], "#aba8a8"])
            elif line[1] == 2:
                name_status_ls.append([line[0], line[1], "#b6aeae"])
            elif line[1] == 3:
                name_status_ls.append([line[0], line[1], "#d0c9c9"])
            else:
                name_status_ls.append([line[0], line[1], "#ece6e6"])

        return name_status_ls
