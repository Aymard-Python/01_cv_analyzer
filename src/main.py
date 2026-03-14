from loader import reader_cv_json
from validator import validate_schema, validate_content, check_required_fields, validate_string_list, validate_date
from extractor import extract
from report import generate_report


def main():
    
    data = reader_cv_json("../data/cvs.json")

    validate_schema(data)
    validate_content(data)
    validate_date(data)

    stats = extract(data)

    report = generate_report(stats, data)

    print(report)

if __name__ == "__main__":
    main()