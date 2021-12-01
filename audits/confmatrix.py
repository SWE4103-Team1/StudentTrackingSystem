from StudentTrackingSystemApp.configfuncs import excel_in_dict as xls_confs


_mat_elective_to_type = {
    "BAS SCI": "NS",
    "CSE - ITS": "CSE-ITS",
    "CSE - HSS": "CSE-HSS",
    "CSE - OPEN": "CSE-OPEN",
    "TE": "TE",
}


def non_core_requirements(mat_sheet_name):
    conf_mat = xls_confs[mat_sheet_name]

    non_core_requirements = {}

    def add_non_core_req(course_type, credit_hours):
        type_reqs = non_core_requirements.get(
            course_type, {"num_courses": 0, "credit_hours": 0}
        )
        type_reqs["num_courses"] += 1
        type_reqs["credit_hours"] += credit_hours
        non_core_requirements[course_type] = type_reqs

    for row_idx, row in conf_mat.iterrows():
        col_idx = 0
        for _, value in row.items():
            if value in _mat_elective_to_type:
                course_type = _mat_elective_to_type[value]
                credit_hours = _course_credit_hours(conf_mat, row_idx, col_idx)
                add_non_core_req(course_type, credit_hours)
            col_idx += 1

    return non_core_requirements


def best_fit_config_matrix(cohort):
    cohort_start_year = cohort.split("-")[0]
    target_year = int(cohort_start_year)

    def is_target_year(sheet):
        mat_start_year = sheet.split("-")[0]
        if mat_start_year.isnumeric():
            try:
                mat_start_year = int(mat_start_year)
            except ValueError:
                return False
            return mat_start_year == target_year
        return False

    student_mat = list(filter(is_target_year, xls_confs.keys()))
    if len(student_mat) < 1:
        raise RuntimeError(
            "No suitable matrix in configration file for start year {}".format(
                target_year
            )
        )
    return student_mat[0]


def _course_credit_hours(conf_mat, code_row, code_col):
    _CH_ROW_OFFSET = 3
    _CH_COL_OFFSET = 1
    credit_hour_row = code_row + _CH_ROW_OFFSET
    credit_hour_col = code_col + _CH_COL_OFFSET
    return int(conf_mat.iat[credit_hour_row, credit_hour_col])
