def function_with_uncommon_error(data):
    try:
        result = [item['value'] for item in data if 'value' in item]
        return result
    except KeyError:
        print("KeyError: 'value' key not found in one or more dictionaries")
        return []
    except TypeError:
        print("TypeError: Item in the list is not a dictionary")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

data = [{'value': 1}, {'key': 'value'}, {'value': 2, 'other': 3}]
result = function_with_uncommon_error(data)
print(result) # Output: [1, 2]

data = [{'value': 1}, {'value': 'a'}, {'value': 2}]
result = function_with_uncommon_error(data)
print(result) # Output: [1, 'a', 2]

data = [{'key': 1}, {'key': 2}]
result = function_with_uncommon_error(data)
print(result) # Output: []