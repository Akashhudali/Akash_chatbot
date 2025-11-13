# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa-pro/concepts/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
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
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionShowCProgram(Action):
    def name(self):
        return "action_show_c_program"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        c_code = """Here's a C program to add two numbers:

```c
#include <stdio.h>
int main() {
  int a, b, sum;
  printf("Enter two numbers: ");
  scanf("%d %d", &a, &b);
  sum = a + b;
  printf("Sum = %d", sum);
  return 0;
}
```"""
        dispatcher.utter_message(text=c_code)
        return []