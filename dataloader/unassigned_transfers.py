import pandas as pd


def get_transfer_unassigned_courses(course_titles):
    transfer_course_codes = []
    course_dictionary = {
        "BLOCK": "EXTRA",
        "SCIENCE": "BAS SCI",
        "LANGUAGE": "CSE-OPEN",
        "HUM": "CSE-HSS",
        "OPEN": "CSE-OPEN",
        "TECHNICAL ELECTIVE": "TE",
    }
    for title in course_titles.values():
        if (
            "SCIENCE" in title
            or "PHYSICS" in title
            or "CHEMISTRY" in title
            or "BIOLOGY" in title
        ):
            transfer_course_codes.append(course_dictionary["SCIENCE"])
        elif (
            "ARTS" in title
            or "COMPLEMENTARY STUDIES" in title
            or "COMPLIMENTARY STUDIES" in title
            or "OPEN ELECTIVE" in title
        ):
            transfer_course_codes.append(course_dictionary["OPEN"])
        elif "TECHNICAL ELECTIVE" in title:
            transfer_course_codes.append(course_dictionary["TECHNICAL ELECTIVE"])
        elif "FRENCH" in title or "ENGLISH" in title or "SPANISH" in title:
            transfer_course_codes.append(course_dictionary["LANGUAGE"])
        elif "HUM" in title:
            transfer_course_codes.append(course_dictionary["HUM"])
        elif "ASSIGNED" in title:
            transfer_course_codes.append(title)
        else:
            transfer_course_codes.append("BLOCK")
    return pd.Series(transfer_course_codes)


def fix_course_title(course_titles):
    course_title_dictionary = {
        (
            "U/A BASIC SCIENCE ELECTIVE",
            "U/A SCIENCE ELECTIVE",
            "U/A BASIC SCIENCE",
            "U/A SCIENCE",
        ): "U/A BAS SCI",
        "U/A FRENCH": "U/A CSE-OPEN (FRENCH)",
        "U/A ENGLISH": "U/A CSE-OPEN (ENGLISH)",
        "U/A SPANISH": "U/A CSE-OPEN (SPANISH)",
        ("U/A HUMANITIES", "HUM"): "U/A CSE-HSS",
        (
            "A-LEVEL PHYSICS",
            "UNASSIGNED PHYSICS 1ST YR",
            "UNASSIGNED PHYSICS",
        ): "U/A BAS SCI (PHYS)",
        ("A-LEVEL CHEMISTRY", "UNASSIGNED CHEMISTRY 1ST YR"): "U/A BAS SCI (CHEM)",
        ("A-LEVEL BIOLOGY", "UNASSIGNED BIOLOGY 1ST YR"): "U/A BAS SCI (BIO)",
        (
            "COMPLEMENTARY STUDIES ELECTIVE",
            "COMPLIMENTARY STUDIES ELECTIVE",
            "U/A OPEN ELECTIVE",
            "U/A ARTS",
            "U/A OPEN ARTS",
            "U/A OPEN ELECTIVE",
        ): "U/A CSE-OPEN",
        ("BLOCK TRANSFER, U/A BLOCK TRANSFER"): "U/A BLOCK",
        ("U/A TECHNICAL ELECTIVE", "TECHNICAL ELECTIVE"): "U/A TE",
    }

    for key in course_title_dictionary:
        course_titles.replace(
            key, course_title_dictionary[key], inplace=True, regex=True
        )

    return course_titles
