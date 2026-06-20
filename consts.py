from dataclasses import dataclass


@dataclass
class Models:
    CYNER: str = r"C:\ML_proj\cyner"
    SECURE_BERT: str = r"C:\ML_proj\SecureBERT"


# CYNER use as common unique translation

ORG = "Organization"
SYS = "System"
VUL = "Vulnerability"
MAL = "Malware"
IND = "Indicator"
TIM = "Time"
LOC = "Location"

MAP_DNRTI_TO_CYNER = {
    "HackOrg": ORG,
    "SecTeam": ORG,
    "Idus": ORG,
    "Org": ORG,
    "OffAct": SYS,
    "Way": SYS,
    "Exp": VUL,
    "Tool": MAL,
    "SamFile": IND,
    "Time": TIM,
    "Area": LOC,
}

MAP_SECUREBERT_TO_CYNER = {
    "APT": ORG,
    "SECTEAM": ORG,
    "IDTY": ORG,
    "ACT": SYS,
    "OS": SYS,
    "TOOL": SYS,
    "VULID": VUL,
    "VULNAME": VUL,
    "MAL": MAL,
    "FILE": IND,
    "TIME": TIM,
    "LOC": LOC,
}


CYNER_CATEGORIES = [ORG, SYS, VUL, MAL, IND, TIM, LOC]
MAP_CYNER_TO_CYNER = {cat: cat for cat in CYNER_CATEGORIES}
