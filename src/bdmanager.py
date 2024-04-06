import psycopg2
from config import config

class BDManager:
    def get_companies_and_vacancies_count(database_name):
    """
    Получает список всех компаний и количество вакансий у каждой компании
    """
    params = config()
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute("""
                SELECT employers.employer_name as employer, COUNT(*)
                FROM employers
                JOIN vacancies using (employer_id)
                GROUP BY employer
                """)
        response = cur.fetchall()
    for r in response:
        print(f"{r[0]} - {r[1]} вакансий")
    conn.close()

    def get_all_vacancies(database_name):
    """
    Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
    """
    params = config()
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute("""
               SELECT
               employers.employer_name,
               vacancies.vacancy_name,
               vacancies.salary_from,
               vacancies.salary_to,
               vacancies.vacancy_url
               FROM employers
               JOIN vacancies USING (employer_id)
               """)
        response = cur.fetchall()
    for r in response:
        print(f"{r[0]} / {r[1]} / {r[2]}-{r[3]} RUR / ссылка {r[4]}")

    def get_avg_salary(database_name):
    """
    Получает среднюю зарплату по вакансиям
    """
    params = config()
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute("""
                SELECT AVG((salary_from + salary_to)/2)
                FROM vacancies
                """)
        response = cur.fetchall()
    print(f"Средняя зарплата по всем вакансиям базы данных - {round(response[0][0])} рублей")

    def get_vacancies_with_higher_salary(database_name):
    """
    Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
    """
    params = config()
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute("""SELECT 
                employers.employer_name,
                vacancies.vacancy_name,
                vacancies.salary_from,
                vacancies.salary_to,
                vacancies.vacancy_url
                FROM employers
                JOIN vacancies USING (employer_id)
                WHERE ((vacancies.salary_from + vacancies.salary_to)/2) >
                (SELECT AVG((salary_from + salary_to)/2) FROM vacancies)""")
        response = cur.fetchall()
    cls.get_avg_salary(database_name)
    print("\nЗарплата по данным вакансиям выше средней по всей базе:\n")
    for r in response:
        print(f"{r[0]} / {r[1]} / {r[2]}-{r[3]} RUR / ссылка {r[4]}")

    def get_vacancies_with_keyword(database_name, query):
    """
    Получает список всех вакансий, в названии которых содержатся переданные в метод слова
    """
    params = config()
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute(f"""
                SELECT
                employers.employer_name,
                vacancies.vacancy_name,
                vacancies.salary_from,
                vacancies.salary_to,
                vacancies.vacancy_url
                FROM employers
                JOIN vacancies USING (employer_id)
                WHERE vacancies.vacancy_name LIKE '%{query.lower()}%'
                """)
        response = cur.fetchall()
    if not response:
        print("\nПо вашему запросу ничего не найдено\n")
    else:
        print("\nПо вашему запросу найдены следующие вакансии:\n")
        for r in response:
            print(f"{r[0]} / {r[1]} / {r[2]}-{r[3]} RUR / ссылка {r[4]}")