from rasa_sdk import Action 
from rasa_sdk.events import SlotSet

from sdk_dados_abertos_camara import endpoints, models

# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionDepsByPartido(Action):
    """
    Action that queries for deputados from a specific partido.
    """
    def name(self):
        return "action_deps_by_partido"

    def run(self, dispatcher, tracker, domain):
        sigla_partido = tracker.get_slot('partido')
        try:
            deputados = endpoints.get_deputados(sigla_partido=sigla_partido, params={'itens': 100}) 
            dispatcher.utter_message(
                template='utter_partido/deputados',
                deputados=[str(d) for d in deputados],
            )
            return [SlotSet("deputados", [d.__dict__() for d in deputados])]
        except Exception as e:
            print(e)
            dispatcher.utter_message(
                template='utter_partido/not_found',
                partido=tracker.get_slot('partido')
            )
            return []
