# Personality Insights Service Python Demo

  The IBM Watson [Personality Insights](https://cloud.ibm.com/docs/services/personality-insights?topic=personality-insights-gettingStarted) service uses linguistic analysis to extract cognitive and social characteristics from input text such as email, text messages, tweets, forum posts, and more. By deriving cognitive and social preferences, the service helps users to understand, connect to, and communicate with other people on a more personalized level.
  
## Getting Started

1. Install [python SDK](https://github.com/watson-developer-cloud/python-sdk).Run pip install --upgrade ibm-watson & the latest is Python 3.7
2. Create a [IBM Cloud Account](http://cloud.ibm.com/)
3. Create an instance of Personality Insights within your IBM Cloud account
4. Within the PersonalityInsightsProf.py file, enter the credentials to authenticate to the service.
- version
- iam_apikey
- url
5. Choose the type of file you want to analyze (txt, JSON or CSV)
6. In the demo I analyze a txt file for personality traits and save results to a JSON file
