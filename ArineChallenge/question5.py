
from typing import Optional
from datetime import datetime

def get_latest_med_ndc(data_obj: dict) -> Optional[str]:
    latest_date = None
    ndc9_latest = None
    
    if "medications" in data_obj:
        for i in data_obj["medications"]:
            if "fills" in i:
                for fill in i["fills"]:
                    if "fillDate" in fill:
                        fill_date = datetime.strptime(fill["fillDate"], "%Y-%m-%d")
                        if latest_date is None or fill_date > latest_date:
                            latest_date = fill_date
                            ndc9_latest = i["ndc9"]
                            
    return ndc9_latest
