from dataclasses import dataclass
from datetime import date

@dataclass
class Expense:
    category: str
    amount: float
    date: str
    description: str