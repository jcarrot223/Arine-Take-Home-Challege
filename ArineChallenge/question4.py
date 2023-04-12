def get_tablet_meds(data_obj: dict) -> list:
    tablet_meds = []
    
    if "medications" in data_obj:
        for med in data_obj["medications"]:
            if "doseForm" in med and "tablet" in med["doseForm"].lower():
                tablet_meds.append(med)
    
    return tablet_meds
