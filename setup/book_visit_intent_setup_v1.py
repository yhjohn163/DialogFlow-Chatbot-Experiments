# Imports the Google Cloud client library
import os
import dialogflow_v2 as dialogflow
import management.intent_management as intent_mng

# use GCP credentials and specify dialogflow project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users\jack\Desktop\work\Google\pythontest-f8d5e75dddcd.json"
projectID = "pythontest-59c9c"

client = dialogflow.IntentsClient()
parent = client.project_agent_path(projectID)
# root intent: the user express the need of a certain type of medic
intent = {

    "display_name": "book_visit",
    "webhook_state": True,

    "training_phrases": [{"parts": [{"text": "cerca un "}, {"text": "podologo",
                                                            "entity_type": "@medical_profession", "alias": "medic"}]},
                         {"parts": [{"text": "trovami un "}, {"text": "dietista", "entity_type": "@medical_profession",
                                                              "alias": "medic"}]},
                         {"parts": [{"text": "ho bisogno di un "}, {"text": "infermiere",
                                                                    "entity_type": "@medical_profession",
                                                                    "alias": "medic"}]}],

    "output_contexts": [{"name": "projects/{}/agent/sessions/setup_session/contexts/book_visit".format(projectID),
                         "lifespan_count": 5}],

    "parameters": [{"display_name": "medic", "entity_type_display_name": "@medical_profession",
                    "value": "$medic.original", "mandatory": True}]}

# stores the intent id in response.name[-36:], we need it in the code for the next (followup) intent.
response = client.create_intent(parent, intent)

# followup intent 1, asks for the place where you want to find the specified type of medic

intent_followup1 = {
    "display_name": "book_visit_followup1",
    "webhook_state": True,
    "training_phrases": [{"parts": [{"text": "a "}, {"text": "roma",
                                                     "entity_type": "@sys.geo-city", "alias": "place"}]},
                         {"parts": [{"text": "vicino a "}, {"text": "milano",
                                                            "entity_type": "@sys.geo-city", "alias": "place"}]}],

    "input_context_names": ["projects/{}/agent/sessions/setup_session/contexts/book_visit".format(projectID)],
    "parent_followup_intent_name": "projects/{}/agent/intents/{}".format(projectID, response.name[-36:]),
    "output_contexts": [{"name": "projects/{}/agent/sessions/setup_session/contexts/book_visit".format(projectID),
                         "lifespan_count": 5}],
    "parameters": [{"display_name": "place", "entity_type_display_name": "@sys.geo-city",
                    "value": "place.original", "mandatory": True}]}


response = client.create_intent(parent, intent_followup1)

# followup intent 2, asks for the desired day

intent_followup2 = {
    "display_name": "book_visit_followup2",
    "webhook_state": True,
    "training_phrases": [{"parts": [{"text": "il giorno "}, {"text": "14",
                                                             "entity_type": "@day_of_the_month", "alias": "day"}]}],

    "input_context_names": ["projects/{}/agent/sessions/setup_session/contexts/book_visit".format(projectID)],
    "parent_followup_intent_name": "projects/{}/agent/intents/{}".format(projectID, response.name[-36:]),
    "output_contexts": [{"name": "projects/{}/agent/sessions/setup_session/contexts/book_visit".format(projectID),
                         "lifespan_count": 5}],
    "parameters": [{"display_name": "day", "entity_type_display_name": "@day_of_the_month",
                    "value": "day.original", "mandatory": True}]}


response = client.create_intent(parent, intent_followup2)

# followup intent 3, asks for the desired hour

intent_followup3 = {
    "display_name": "book_visit_followup3",
    "webhook_state": True,
    "training_phrases": [{"parts": [{"text": "alle "}, {"text": "14",
                                                        "entity_type": "@hour_of_the_day", "alias": "hour"}]},
                         {"parts": [{"text": "15", "entity_type": "@hour_of_the_day", "alias": "hour"}]}],

    "input_context_names": ["projects/{}/agent/sessions/setup_session/contexts/book_visit".format(projectID)],
    "parent_followup_intent_name": "projects/{}/agent/intents/{}".format(projectID, response.name[-36:]),
    "output_contexts": [{"name": "projects/{}/agent/sessions/setup_session/contexts/book_visit".format(projectID),
                         "lifespan_count": 5}],
    "parameters": [{"display_name": "hour", "entity_type_display_name": "@hour_of_the_day",
                    "value": "hour.original", "mandatory": True}]}


response = client.create_intent(parent, intent_followup3)










