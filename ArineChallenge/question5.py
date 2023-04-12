
from typing import Optional
from datetime import datetime

def get_latest_med_ndc(data_obj: dict) -> Optional[str]:
    latest_fill_date = None
    latest_ndc9 = None
    
    if "medications" in data_obj:
        for med in data_obj["medications"]:
            if "fills" in med:
                for fill in med["fills"]:
                    if "fillDate" in fill:
                        fill_date = datetime.strptime(fill["fillDate"], "%Y-%m-%d")
                        if latest_fill_date is None or fill_date > latest_fill_date:
                            latest_fill_date = fill_date
                            latest_ndc9 = med["ndc9"]
                            
    return latest_ndc9

