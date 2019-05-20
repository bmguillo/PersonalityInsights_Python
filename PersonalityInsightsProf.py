import json
import sys
#sys.path.append('/anaconda3/')
#sys.path.append('/anaconda3/lib/python3.7/')
#print("\n".join(sys.path))
from os.path import join, dirname
from ibm_watson import PersonalityInsightsV3
from ibm_watson import ApiException



# Authenticate into the service, call PI method & catch error
try:
    personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    iam_apikey='lBams5473McaOiJwFFEwpVYu7Vx4lAPIJ3H0XoFoA8X_',
    url='https://gateway.watsonplatform.net/personality-insights/api'
    )

#stores the text file(same dir as script) input in variable profile_json and json is the output
    with open(join(dirname(__file__), 'markblog.txt')) as profile_text:
#calls the PI profile method to get character traits and shows results
        profile = personality_insights.profile(
        profile_text.read(),#reads txt file in method
        accept='application/json',# accept json as output
        content_type='text/plain',# input is txt file
        consumption_preferences=True,#show consumption preferences on personality profile results
        raw_scores=True # show raw scores on personality results
        ).get_result()
# saves/writes file name personalityresults.json from the profile variable contents or personality trait assessment
        with open('personalityresults.json', 'w') as outfile:
#supports saving stream to file; profile is the personality traits result
            json.dump(profile, outfile, sort_keys=True, indent=4)
#supports pretty formatting to console
            print(json.dumps(profile, indent=4))

#     with open('personalityresults.json') as data_file:
#         data_loaded = json.load(data_file)
#         print(data == data_loaded)

except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)
    
    
