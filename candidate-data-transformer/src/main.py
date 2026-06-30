import json
import typer

from parsers.csv_parser import parse_csv
from parsers.resume_parser import parse_resume
from utils.merger import merge_candidate
from utils.projector import project_output
from utils.validator import validate_candidate

app = typer.Typer()


@app.command()
def run(
    csv_file: str = "data/sample.csv",
    resume_file: str = "data/resume.pdf",
    config_file: str = "config/default.json",
):
    csv_data = parse_csv(csv_file)
    resume_data = parse_resume(resume_file)

    result = merge_candidate(csv_data, resume_data)

    candidate = result["candidate"]

    validated = validate_candidate(candidate)

    if not validated:
        print("Validation Failed!")
        return

    output = project_output(candidate, config_file)

    print("\nOUTPUT\n")
    print(output)

    with open("output/result.json", "w") as f:
        json.dump(output, f, indent=4)

    print("\nOutput saved to output/result.json")


if __name__ == "__main__":
    app()