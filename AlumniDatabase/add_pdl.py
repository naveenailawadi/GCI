from AlumniDatabase.AlumniFinder import PDLbot
from AlumniDatabase.secrets import PDL_KEY
import pandas as pd
import time
import sys


# set the names of the columns with data
NAME_COL = 'Name'
LINKEDIN_COL = 'LinkedIn'


# make a function that handles keyerrors
def safe_extract(dictionary, key):
    # handle none dictionary
    if not dictionary:
        return None

    # handle false type
    try:
        extract = dictionary[key]
    except KeyError:
        extract = None

    return extract


# make a function for safe exports
def safe_export(extrapolated_data, filename):
    # make a dataframe on the extrapolated data
    data = pd.DataFrame({
        "first_name": [safe_extract(entry, "first_name") for entry in extrapolated_data],
        "last_name": [safe_extract(entry, "last_name") for entry in extrapolated_data],
        "linkedin_url": [safe_extract(entry, "linkedin_url") for entry in extrapolated_data],
        "job_title": [safe_extract(entry, "job_title") for entry in extrapolated_data],
        "job_title_role": [safe_extract(entry, "job_title_role") for entry in extrapolated_data],
        "job_company_name": [safe_extract(entry, "job_company_name") for entry in extrapolated_data],
        "job_company_website": [safe_extract(entry, "job_company_website") for entry in extrapolated_data],
        "job_company_industry": [safe_extract(entry, "job_company_industry") for entry in extrapolated_data],
        "job_company_location_locality": [safe_extract(entry, "job_company_location_locality") for entry in extrapolated_data],
        "phone_numbers": [safe_extract(entry, "phone_numbers") for entry in extrapolated_data],
        "emails": [safe_extract(entry, "emails") for entry in extrapolated_data],
        "interests": [safe_extract(entry, "interests") for entry in extrapolated_data],
        "experience": [safe_extract(entry, "experience") for entry in extrapolated_data],
        "profiles": [safe_extract(entry, "profiles") for entry in extrapolated_data]
    })

    # export the data
    data.to_csv(filename, index=False)

# make a main function to iterate through the people of the


def main(filename):
    # open the file
    df = pd.read_csv(filename)

    # make a pdl bot
    bot = PDLbot(PDL_KEY)

    # make a list of new data
    extrapolated_data = []

    # iterate through the rows to get the data entries
    for index, row in df.iterrows():
        names = row[NAME_COL].split(' ')
        first_name = names[0]
        last_name = names[-1]
        linkedin = row[LINKEDIN_COL]

        # get the info
        entry = bot.get_on_name_and_linkedin(first_name, last_name, linkedin)

        extrapolated_data.append(entry)

        # save the data as a backup
        safe_export(extrapolated_data, f"{filename.split('.')[0]}_backup.csv")

        time.sleep(1)

    # save the data for real
    safe_export(extrapolated_data, filename)


if __name__ == '__main__':
    filename = sys.argv[1].strip().replace('\\', '')

    main(filename)
    print('Done!')


'''
NOTES
- Pertinent Data
    - "first_name"
    - "last_name"
    - "linkedin_url"
    - "job_title"
    - "job_title_role"
    - "job_company_industry"
    - "job_company_location_locality"
    - "phone_numbers"
    - "emails"
    - "interests"
    - "experience"
    ⁃ "company"
    ⁃ "name"
    ⁃ "location"
    ⁃ "locality"
    ⁃ "end_date"
    ⁃ "start_date"
    ⁃ "title"
    ⁃ "name"
    ⁃ "role"
    ⁃ "education"
    ⁃ "school"
    ⁃ “Name”
    ⁃ "end_date"
    ⁃ "start_date"
    ⁃ “majors”
    ⁃ “minors”
'''
