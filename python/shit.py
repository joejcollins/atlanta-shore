import csv
from typing import List
from pydantic import BaseModel

class MyModel(BaseModel):
    field1: str
    field2: int
    field3: float
    field4: List[str]

    @classmethod
    def set_model_values_from_csv(cls, csv_string: str):
        field_mapping = {
            'CSVField1': 'field1',
            'CSVField2': 'field2',
            'CSVField3': 'field3',
            'CSVField4': 'field4',
        }

        csv_data = csv.reader(csv_string.splitlines())

        data = {}
        current_field = None

        for row in csv_data:
            csv_field_name = row[0]
            csv_field_value = row[1]

            if csv_field_name:
                if csv_field_name in field_mapping:
                    model_field_name = field_mapping[csv_field_name]
                    current_field = model_field_name
                    if current_field == 'field4':
                        data[current_field] = []
                    else:
                        data[current_field] = csv_field_value
            elif current_field and csv_field_value:
                if current_field == 'field4':
                    data[current_field].append(csv_field_value)

        # Convert single value to list if needed
        if 'field4' in data and not isinstance(data['field4'], list):
            data['field4'] = [data['field4']]

        model = cls(**data)
        return model

# Example usage
csv_string = '''CSVField1,value1
CSVField2,2
CSVField3,3.14
CSVField4,value2
,value3
'''

model = MyModel.set_model_values_from_csv(csv_string)

print(model.field1)  # Output: value1
print(model.field2)  # Output: 2
print(model.field3)  # Output: 3.14
print(model.field4)  # Output: ['value2', 'value3']
