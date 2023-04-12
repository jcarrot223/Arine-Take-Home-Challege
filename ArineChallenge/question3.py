def get_antihtn_meds(data_obj: dict) -> list:
    antihtn_meds = []
    
    if "medications" in data_obj:
        for med in data_obj["medications"]:
            if "drugGroup" in med and "antihtn" in med["drugGroup"]:
                antihtn_meds.append(med)
    
    return antihtn_meds
