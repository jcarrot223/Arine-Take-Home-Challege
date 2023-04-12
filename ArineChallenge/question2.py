# def convert_to_float(input_str: str, default: float): 
#     if not input_str.replace(".", "").isnumeric():
#         return default
#     else: 
#         return float(input_str)

def convert_to_float(input_str: str, default: float) -> float:
    if '.' not in input_str:
        return default

    try:
        return float(input_str)
    except ValueError:
        return default
        
print(convert_to_float("1.0", "yes"))