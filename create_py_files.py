import os

#filesnames
problems = [
    "01_leetcode#1757_recyclable_and_low_fat_products",
    "02_leetcode#584_find_customer_referee",
    "03_leetcode#595_big_countries",
    "04_leetcode#1148_article_views_i",
    "05_leetcode#1683_invalid_tweets",
    "06_leetcode#1378_replace_employee_id_with_the_unique_identifier",
    "07_leetcode#1068_product_sales_analysis_i",
    "08_leetcode#1581_customer_who_visited_but_did_not_make_any_transactions",
    "09_leetcode#197_rising_temperature",
    "10_leetcode#1661_average_time_of_process_per_machine",
    "11_leetcode#577_employee_bonus",
    "12_leetcode#1280_students_and_examinations",
    "13_leetcode#570_managers_with_at_least_5_direct_reports",
    "14_leetcode#1934_confirmation_rate",
    "15_leetcode#620_not_boring_movies",
    "16_leetcode#1251_average_selling_price",
    "17_leetcode#1075_project_employees_i",
    "18_leetcode#1633_percentage_of_users_attended_a_contest",
    "19_leetcode#1211_queries_quality_and_percentage",
    "20_leetcode#1193_monthly_transactions_i",
    "21_leetcode#1174_immediate_food_delivery_ii",
    "22_leetcode#550_game_play_analysis_iv",
    "23_leetcode#2356_number_of_unique_subjects_taught_by_each_teacher",
    "24_leetcode#1141_user_activity_for_the_past_30_days_i",
    "25_leetcode#1070_product_sales_analysis_iii",
    "26_leetcode#596_classes_with_at_least_5_students",
    "27_leetcode#1729_find_followers_count",
    "28_leetcode#619_biggest_single_number",
    "29_leetcode#1045_customers_who_bought_all_products",
    "30_leetcode#1731_the_number_of_employees_which_report_to_each_employee",
    "31_leetcode#1789_primary_department_for_each_employee",
    "32_leetcode#610_triangle_judgement",
    "33_leetcode#180_consecutive_numbers",
    "34_leetcode#1164_product_price_at_a_given_date",
    "35_leetcode#1204_last_person_to_fit_in_the_bus",
    "36_leetcode#1907_count_salary_categories",
    "37_leetcode#1978_employees_whose_manager_left_the_company",
    "38_leetcode#626_exchange_seats",
    "39_leetcode#1341_movie_rating",
    "40_leetcode#1321_restaurant_growth",
    "41_leetcode#602_friend_requests_ii",
    "42_leetcode#585_investments_in_2016",
    "43_leetcode#185_department_top_three_salaries",
    "44_leetcode#1667_fix_names_in_a_table",
    "45_leetcode#1527_patients_with_a_condition",
    "46_leetcode#196_delete_duplicate_emails",
    "47_leetcode#176_second_highest_salary",
    "48_leetcode#1484_group_sold_products_by_the_date",
    "49_leetcode#1327_list_the_products_ordered_in_a_period",
    "50_leetcode#1517_find_users_with_valid_e-mails"
]

# Output directory
output_dir = "Solutions in Pandas"
os.makedirs(output_dir, exist_ok=True)

# Generate files
for problem in problems:
    filename = f"{problem}.py"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w") as f:
        f.write(f"# {problem}\n")
        f.write("# Pandas solution \n\n")

print(f"{len(problems)} Python files created in folder: {output_dir}")