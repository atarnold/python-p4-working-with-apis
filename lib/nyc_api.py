
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "https://proxy.dev.socrata.com/socrata/data.cityofnewyork.us/resource/75e9-fg2t.json"

    response = requests.get(URL)
    return response.content
  def program_agencies(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["cbo_name"])

        return programs_list

#programs = GetPrograms().get_programs()
#print(programs)
programs = GetPrograms()
agencies = programs.program_agencies()

for agency in set(agencies):
    print(agency)