import typesense
from python_client import *

# Collection schema (you can optionally include collection creation here) - manually entered
collection_schema = {
    'name': 'products',
    'fields': 
    [
        
      {"name": "__EMPTY", "type": "int32"},
      {"name": "Tests", "type": "string", "optional": True},
      {"name": "Is Test Live", "type": "string", "optional": True},
      {"name": "Test/Profile/Package", "type": "string", "optional": True},
      {"name": "1 line description (20-30 words description)", "type": "string", "optional": True},
      {"name": "Sample type (Blood, urine)\n\nHow is the sample taken? (If one, both, mention)", "type": "string", "optional": True},
      {"name": "Fasting required (Yes/No)", "type": "string", "optional": True},
      {"name": "Alias (2-3) - Other name", "type": "string", "optional": True},
      {"name": "Risk assessment (3-4)\n\nWhat problems is it taken for?", "type": "string", "optional": True},
      {"name": "Final content with subheadings (Doc link)", "type": "string", "optional": True},
      {"name": "Date", "type": "string", "optional": True},
      {"name": "Medical check status", "type": "string", "optional": True},
      {"name": "Name", "type": "string", "optional": True},
      {"name": "Content check status", "type": "string", "optional": True},
      {"name": "Name_1", "type": "string", "optional": True},
      {"name": "Date_2", "type": "string", "optional": True},
      {"name": "Uploaded on CMS panel", "type": "string", "optional": True},
      {"name": "Name_4", "type": "string", "optional": True},
      {"name": "Date_5", "type": "string", "optional": True},
      {
          "name": "embedding",
          "type": "float[]",
          "embed": {
            "from": ["Tests","1 line description (20-30 words description)","Alias (2-3) - Other name","Risk assessment (3-4)\n\nWhat problems is it taken for?"],
            "model_config": {
              "model_name": "ts/all-MiniLM-L12-v2"
            }
          }
      }
      
    ],
    'default_sorting_field': "__EMPTY"
}

