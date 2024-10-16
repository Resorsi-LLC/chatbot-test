from schemas.job_description import YEARS_OF_EXPERIENCE_ENUM


def parse_years_of_experience(years_of_experience):
    min_years = years_of_experience.get("min")
    max_years = years_of_experience.get("max")

    result = set()  # Use a set to avoid duplicate values

    # Handle 'Not Specified' and numerical values for min
    if min_years != "Not Specified":
        if min_years is not None:
            if min_years < 3:
                result.update(YEARS_OF_EXPERIENCE_ENUM[1:])
            elif 3 <= min_years < 6:
                result.update(YEARS_OF_EXPERIENCE_ENUM[2:])
            elif 6 <= min_years < 9:
                result.update(YEARS_OF_EXPERIENCE_ENUM[3:])
            elif min_years >= 9:
                result.update(YEARS_OF_EXPERIENCE_ENUM[4:])
    else:
        result.add("Not Specified")

    # Handle 'Not Specified' and numerical values for max
    if max_years != "Not Specified":
        if max_years is not None:
            if max_years < 3:
                result.update(YEARS_OF_EXPERIENCE_ENUM[1:2])
            elif 3 <= max_years < 6:
                result.update(YEARS_OF_EXPERIENCE_ENUM[1:3])
            elif 6 <= max_years < 9:
                result.update(YEARS_OF_EXPERIENCE_ENUM[1:4])
            elif max_years >= 9:
                result.update(YEARS_OF_EXPERIENCE_ENUM[1:])
    else:
        result.add("Not Specified")

    # Ensure the result is not empty
    if not result:
        result.add("Not Specified")

    # Convert the set back to a sorted list
    result = sorted(result, key=lambda x: YEARS_OF_EXPERIENCE_ENUM.index(x))

    # Remove 'Not Specified' if specific ranges are present
    if "Not Specified" in result and len(result) > 1:
        result.remove("Not Specified")

    return list(result)


def parse_english_level(english_level):
    if "Not Specified" in english_level:
        english_level.remove("Not Specified")
    return english_level


def parse_inferred_data_from_job_description(job_description):
    copy = job_description.copy()

    years_of_experience = copy.get("years_of_experience", {})
    copy["years_of_experience"] = parse_years_of_experience(years_of_experience)

    english_level = copy.get("english_level", [])
    copy["english_level"] = parse_english_level(english_level)

    return copy
