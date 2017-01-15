class SQL:
    """This class contains the methods of sql queries. Every method returns the query as string."""

    def __init__(self):
        self.query = ""

    def number_of_proj_by_clients(self):
        self.query = "SELECT company_name, COUNT(company_name) AS number_of_projects FROM project\
                      GROUP BY company_name\
                      ORDER BY number_of_projects DESC;"
        return self.query

    def company_by_color(self):
        self.query = "SELECT name, company_name, main_color\
                      FROM project\
                      WHERE main_color IS NOT NULL;"
        return self.query

    def project_name_by_budget(self):
        self.query = "SELECT id, name, budget_value::float AS budget, budget_currency, company_name, main_color\
                      FROM project\
                      WHERE name IS NOT NULL\
                      ORDER BY budget DESC;"
        return self.query

    def bigger_than_average(self):
        self.query = "SELECT name, company_name, budget_value, main_color\
                      FROM project\
                      WHERE name IS NOT NULL AND main_color IS NOT NULL AND budget_value::float >\
                      (SELECT AVG(budget_value::float) FROM project)\
                      ORDER BY budget_value::float DESC\
                      LIMIT 30"
        return self.query

    def get_name_and_status(self):
        self.query = "SELECT name, status\
                      FROM project\
                      WHERE name IS NOT NULL;"
        return self.query
