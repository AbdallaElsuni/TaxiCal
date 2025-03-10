__all__ = ["FinancialUnit", "Money", "Tax", "Liability", "Debt", "Status", "Records", "Operations", "PaymentStatus", "Custom", "InterestType", "MaritalStatus", "StandardDeduction", "BracketSeal", "Bracket", "Rate", "Others", "Person", "dictionary_to_person", "str_to_money_usd", "dictionary_to_variables", "variables_to_dictionary", "verify_dictionary_integrity"]
import datetime
from decimal import Decimal
from enum import Enum, auto
from dateutil.relativedelta import relativedelta
class Status(Enum):
    OverDue = auto()
    Awaiting = auto()
    Scheduled = auto()
    def __str__(self):
        return self.name
class Records(Enum):
    Value = auto()
    Time = auto()
    Operation = auto()
    def __str__(self):
        return self.name
class Operations(Enum):
    Printing = auto()
    Creation = auto()
    Subtraction = auto()
    Addition = auto()
    Multiplication = auto()
    Division = auto()
    NotSpecified = auto()
    FullPayment = auto()
    PartialPayment = auto()
    FailedPayment = auto()
    def __str__(self):
        return self.name
class PaymentStatus(Enum):
    Paid = auto()
    UnPaid = auto()
    Capitalized = auto()
    NotSpecified = auto()
    PartiallyPaid = auto()
    InterestOnly = auto()
    def __str__(self):
        return self.name
class Custom(Enum):
    Status = auto ()
    Installment = auto()
    Interest = auto()
    Total = auto()
    IncurredToDate = auto()
    CycleStart = auto()
    DueTo = auto()
    TBD = auto()
    NotSpecified = auto()
    NotAccounted = auto()
    def __str__(self):
        return self.name
class InterestType(Enum):
    PerDiem = auto()
    PerMensem = auto()
    def __str__(self):
        return self.name
class MaritalStatus(Enum):
    Single = auto()
    MarriedNoJoint = auto()
    MarriedJoint = auto()
    NotSpecified = auto()
    def __str__(self):
        return self.name
class TaxesVariables(Enum):
    StandardDeduction = auto()
    PersonalExemption = auto()
    BracketSeal = auto()
    Rate = auto()
    Others = auto()
    StateBiggestBracketOrder = auto()
    def __str__(self):
        return self.name
class StandardDeduction(Enum):
    Singles = auto()
    MarriedNoJoint = auto()
    MarriedJoint = auto()
    def __str__(self):
        return self.name
class PersonalExemption(Enum):
    Singles = auto()
    MarriedNoJoint = auto()
    MarriedJoint = auto()
    Dependant = auto()
class BracketSeal(Enum):
    First = auto()
    Second = auto()
    Third = auto()
    Fourth = auto()
    Fifth = auto()
    Sixth = auto()
    Seventh = auto()
    Eighth = auto()
    Ninth = auto()
    Tenth = auto()
    Eleventh = auto()
    Twelfth = auto()
    Last = auto()
    @property
    def bracket(self):
        if self == BracketSeal.First:
            return Bracket.First
        elif self == BracketSeal.Second:
            return Bracket.Second
        elif self == BracketSeal.Third:
            return Bracket.Third
        elif self == BracketSeal.Fourth:
            return Bracket.Fourth
        elif self == BracketSeal.Fifth:
            return Bracket.Fifth
        elif self == BracketSeal.Sixth:
            return Bracket.Sixth
        elif self == BracketSeal.Seventh:
            return Bracket.Seventh
        elif self == BracketSeal.Eighth:
            return Bracket.Eighth
        elif self == BracketSeal.Ninth:
            return Bracket.Ninth
        elif self == BracketSeal.Tenth:
            return Bracket.Tenth
        elif self == BracketSeal.Eleventh:
            return Bracket.Eleventh
        elif self == BracketSeal.Twelfth:
            return Bracket.Twelfth
        elif self == BracketSeal.Last:
            return Bracket.Last
    def __str__(self):
        return self.name
class Bracket(Enum):
    First = auto()
    Second = auto()
    Third = auto()
    Fourth = auto()
    Fifth = auto()
    Sixth = auto()
    Seventh = auto()
    Eighth = auto()
    Ninth = auto()
    Tenth = auto()
    Eleventh = auto()
    Twelfth = auto()
    Last = auto()

    @property
    def seal(self):
        if self == Bracket.First:
            return BracketSeal.First
        elif self == Bracket.Second:
            return BracketSeal.Second
        elif self == Bracket.Third:
            return BracketSeal.Third
        elif self == Bracket.Fourth:
            return BracketSeal.Fourth
        elif self == Bracket.Fifth:
            return BracketSeal.Fifth
        elif self == Bracket.Sixth:
            return BracketSeal.Sixth
        elif self == Bracket.Seventh:
            return BracketSeal.Seventh
        elif self == Bracket.Eighth:
            return BracketSeal.Eighth
        elif self == Bracket.Ninth:
            return BracketSeal.Ninth
        elif self == Bracket.Tenth:
            return BracketSeal.Tenth
        elif self == Bracket.Eleventh:
            return BracketSeal.Eleventh
        elif self == Bracket.Twelfth:
            return BracketSeal.Twelfth
        elif self == Bracket.Last:
            return BracketSeal.Last

    @property
    def order(self):
        if self == Bracket.First:
            return 1
        elif self == Bracket.Second:
            return 2
        elif self == Bracket.Third:
            return 3
        elif self == Bracket.Fourth:
            return 4
        elif self == Bracket.Fifth:
            return 5
        elif self == Bracket.Sixth:
            return 6
        elif self == Bracket.Seventh:
            return 7
        elif self == Bracket.Eighth:
            return 8
        elif self == Bracket.Ninth:
            return 9
        elif self == Bracket.Tenth:
            return 10
        elif self == Bracket.Eleventh:
            return 11
        elif self == Bracket.Twelfth:
            return 12
        elif self == Bracket.Last:
            return 13

    @property
    def rate(self):
        if self == Bracket.First:
            return Rate.FirstBracket
        elif self == Bracket.Second:
            return Rate.SecondBracket
        elif self == Bracket.Third:
            return Rate.ThirdBracket
        elif self == Bracket.Fourth:
            return Rate.FourthBracket
        elif self == Bracket.Fifth:
            return Rate.FifthBracket
        elif self == Bracket.Sixth:
            return Rate.SixthBracket
        elif self == Bracket.Seventh:
            return Rate.SeventhBracket
        elif self == Bracket.Eighth:
            return Rate.EighthBracket
        elif self == Bracket.Ninth:
            return Rate.NinthBracket
        elif self == Bracket.Tenth:
            return Rate.TenthBracket
        elif self == Bracket.Eleventh:
            return Rate.EleventhBracket
        elif self == Bracket.Twelfth:
            return Rate.TwelfthBracket
        elif self == Bracket.Last:
            return Rate.LastBracket
    def __str__(self):
        return self.name
class Rate(Enum):
    SocialSecurity = auto()
    Medicare = auto()
    FirstBracket = auto()
    SecondBracket = auto()
    ThirdBracket = auto()
    FourthBracket = auto()
    FifthBracket = auto()
    SixthBracket = auto()
    SeventhBracket = auto()
    EighthBracket = auto()
    NinthBracket = auto()
    TenthBracket = auto()
    EleventhBracket = auto()
    TwelfthBracket = auto()
    LastBracket = auto()
    def __str__(self):
        return self.name
class Others(Enum):
    SSWageGap = auto()
    def __str__(self):
        return self.name
class State(Enum):
    NotSpecified = auto()
    Alabama = auto()
    Alaska = auto()
    Arizona = auto()
    Arkansas = auto()
    California = auto()
    Colorado = auto()
    Connecticut = auto()
    Delaware = auto()
    Florida = auto()
    Georgia = auto()
    Hawaii = auto()
    Idaho = auto()
    Illinois = auto()
    Indiana = auto()
    Iowa = auto()
    Kansas = auto()
    Kentucky = auto()
    Louisiana = auto()
    Maine = auto()
    Maryland = auto()
    Massachusetts = auto()
    Michigan = auto()
    Minnesota = auto()
    Mississippi = auto()
    Missouri = auto()
    Montana = auto()
    Nebraska = auto()
    Nevada = auto()
    NewHampshire = auto()
    NewJersey = auto()
    NewMexico = auto()
    NewYork = auto()
    NorthCarolina = auto()
    NorthDakota = auto()
    Ohio = auto()
    Oklahoma = auto()
    Oregon = auto()
    Pennsylvania = auto()
    RhodeIsland = auto()
    SouthCarolina = auto()
    SouthDakota = auto()
    Tennessee = auto()
    Texas = auto()
    Utah = auto()
    Vermont = auto()
    Virginia = auto()
    Washington = auto()
    WestVirginia = auto()
    Wisconsin = auto()
    Wyoming = auto()
    def __str__(self):
        return self.name
class FinancialUnit:
    def __init__(self, value = Decimal(0)):
        if value < 0:
            raise ValueError("Financial Units can't be negative.")
        else:
            self.value = Decimal(str(value))
        self.records = {}
        self.rec = 1
        self.log(Operations.Creation)
    def log(self, operation=Operations.NotSpecified):
        current_time = datetime.datetime.now()
        self.records[self.rec] = {}
        self.records[self.rec][Records.Value] = self.value
        self.records[self.rec][Records.Time] = current_time
        self.records[self.rec][Records.Operation] = operation
        self.rec += 1
    @property
    def dollars(self):
        dollars, cents = divmod(self.value, 100)
        return dollars
    @property
    def cents(self):
        dollars, cents = divmod(self.value, 100)
        return cents
    def __str__(self):
        self.log(Operations.Printing)
        if self.value >= 100 or self.value == 0:
            return f'''${round(self.dollars)}.{round(self.cents):02}'''
        else:
            return f'''¢{round(self.cents)}'''
    def __eq__(self, other):
        if isinstance(other, FinancialUnit):
            if self.value == other.value:
                return True
            else:
                return False
    def __ne__(self, other):
        if isinstance(other, FinancialUnit):
            if self.value != other.value:
                return True
            else:
                return False
    def __gt__(self, other):
        if isinstance(other, FinancialUnit):
            if self.value > other.value:
                return True
            else:
                return False
    def __ge__(self, other):
        if isinstance(other, FinancialUnit):
            if self.value >= other.value:
                return True
            else:
                return False
    def __lt__(self, other):
        if isinstance(other, FinancialUnit):
            if self.value < other.value:
                return True
            else:
                return False
    def __le__(self, other):
        if isinstance(other, FinancialUnit):
            if self.value <= other.value:
                return True
            else:
                return False
    def __add__(self, other):
        self.log(Operations.Addition)
        if isinstance(other, FinancialUnit):
            original_type = type(self)
            return original_type(self.value + Decimal(str(other.value)))
    def __iadd__(self, other):
        if isinstance(other, FinancialUnit):
            self.value += other.value
            return self
    def __sub__(self, other):
        self.log(Operations.Subtraction)
        if isinstance(other, FinancialUnit):
            if self >= other:
                original_type = type(self)
                return original_type(self.value - Decimal(str(other.value)))
            else:
                raise ValueError("Subtrahend is greater than Minuend.")
    def __isub__(self, other):
        if isinstance(other, FinancialUnit):
            if self >= other:
                self.value += other.value
                return self
            else:
                raise ValueError("Subtrahend is greater than Minuend.")
    def __mul__(self, other):
        self.log(Operations.Multiplication)
        if not isinstance(other, FinancialUnit):
            original_type = type(self)
            return original_type(self.value * Decimal(str(other)))
    def __truediv__(self, other):
        self.log(Operations.Division)
        if not isinstance(other, FinancialUnit):
            original_type = type(self)
            return original_type(self.value / Decimal(str(other)))
class Money(FinancialUnit):
    def __init__(self, value):
        super().__init__(value)
    def pay(self, to_be_paid, partial_allowed=True):
        if isinstance(to_be_paid, Liability):
            if self >= to_be_paid:
                self.value -= to_be_paid.value
                to_be_paid.paid()
                self.log(Operations.FullPayment)
            else:
                if partial_allowed:
                    to_be_paid.value -= self.value
                    self.value = 0
                    self.log(Operations.PartialPayment)
                else:
                    self.log(Operations.FailedPayment)
                    raise ValueError("Insufficient fund.")
class Liability(FinancialUnit):
    def __init__(self, value, status=PaymentStatus.UnPaid):
        super().__init__(value)
        self.status = status
    def paid(self):
        self.value = 0
        self.status = PaymentStatus.Paid
class Tax(Liability):
    pass
class Debt:
    def __init__(self, principal, apr, date_issued):
        self.status = PaymentStatus.UnPaid
        self.original = Liability(principal)
        self.principal = Liability(principal)
        self.rules = {
            Custom.Interest: InterestType.PerDiem
        }
        self.apr = apr
        self.issued = date_issued
        self.records = {}
        self.now = datetime.datetime.now()
        self.run_time = datetime.datetime.now()
        self.initialize_records(self.year, True)
        self.run()
    def initialize_records(self, year, for_all=False):
        if for_all: month = 0
        else: month = (year - 1) * 12
        while month < year * 12:
            month += 1
            self.records[month] = {}
            self.records[month][Custom.CycleStart] = self.issued + relativedelta(months=month - 1)
            self.records[month][Custom.DueTo] = self.issued + relativedelta(months=month)
            self.records[month][Custom.Status] = PaymentStatus.NotSpecified
            self.records[month][Custom.Installment] = Custom.NotSpecified
            self.records[month][Custom.Interest] = Custom.NotSpecified
            self.records[month][Custom.Total] = Custom.NotSpecified
    def capitalize(self):
        self.principal += self.monthly
    def paid(self):
        self.status = PaymentStatus.Paid
        self.principal.total = 0
    def installment_paid(self):
        self.principal -= self.installment
    def attempt_to_clear(self, payment):
        if isinstance(payment, Money):
            if self.rules[Custom.Interest] == InterestType.PerDiem:
                if payment >= (self.principal + self.incurred):
                    payment.pay(self.incurred)
                    payment.pay(self.principal)
    def run(self):
        for month, month_data in self.records.items():
            self.run_time = self.records[month][Custom.CycleStart]
            status = self.records[month][Custom.Status]
            if self.now > self.run_time + relativedelta(months=1):  # passed one
                self.records[month][Custom.Installment] = self.installment
                self.records[month][Custom.Interest] = self.monthly
                self.records[month][Custom.Total] = self.installment + self.monthly
                self.records[month][Custom.IncurredToDate] = Custom.NotAccounted
                if status not in [PaymentStatus.Paid, PaymentStatus.PartiallyPaid]:
                    self.capitalize()
                    self.records[month][Custom.Status] = Status.OverDue
                elif status == PaymentStatus.Paid:
                    self.installment_paid()
            elif self.run_time <= self.now <= self.run_time + relativedelta(months=1):  # current
                self.records[month][Custom.Installment] = self.installment
                self.records[month][Custom.Interest] = self.monthly
                self.records[month][Custom.Total] = self.installment + self.monthly
                if status not in [PaymentStatus.Paid, PaymentStatus.PartiallyPaid]:
                    self.records[month][Custom.IncurredToDate] = self.incurred
                    self.records[month][Custom.Status] = Status.Awaiting
                elif status == PaymentStatus.Paid:
                    self.records[month][Custom.IncurredToDate] = Custom.NotAccounted
                    self.installment_paid()
            else:
                self.records[month][Custom.IncurredToDate] = Custom.NotAccounted
                self.records[month][Custom.Status] = Status.Scheduled
                self.records[month][Custom.Installment] = Custom.TBD
                self.records[month][Custom.Interest] = Custom.TBD
                self.records[month][Custom.Total] = Custom.TBD
        self.run_time = self.now
    @property
    def incurred(self):
        return  self.daily * relativedelta(self.now, self.run_time).days
    @property
    def monthly_rate(self):
        return self.apr/12
    @property
    def monthly(self):
        return self.principal * self.monthly_rate
    @property
    def daily_rate(self):
        return self.apr/365
    @property
    def daily(self):
        return self.principal * self.daily_rate
    @property
    def month(self):
        return relativedelta(self.run_time, self.issued).months + 1
    @property
    def year(self):
        return relativedelta(self.run_time, self.issued).years + 1
    @property
    def months_left(self):
        return 12 - self.month
    @property
    def installment(self):
        return self.principal / (self.months_left + 1)
updatable_variables = {
    TaxesVariables.StandardDeduction: {
        StandardDeduction.Singles: Money(Decimal("1500000")),
        StandardDeduction.MarriedNoJoint: Money(Decimal("1500000")),
        StandardDeduction.MarriedJoint: Money(Decimal("3000000")),
    },
    TaxesVariables.BracketSeal: {
        MaritalStatus.Single:{
            BracketSeal.First: Money(Decimal("1192500")),
            BracketSeal.Second: Money(Decimal("4847500")),
            BracketSeal.Third: Money(Decimal("10335000")),
            BracketSeal.Fourth: Money(Decimal("19730000")),
            BracketSeal.Fifth: Money(Decimal("25052500")),
            BracketSeal.Sixth: Money(Decimal("62635000")),
        },
        MaritalStatus.MarriedNoJoint: {
            BracketSeal.First: Money(Decimal("1192500")),
            BracketSeal.Second: Money(Decimal("4847500")),
            BracketSeal.Third: Money(Decimal("10335000")),
            BracketSeal.Fourth: Money(Decimal("19730000")),
            BracketSeal.Fifth: Money(Decimal("25052500")),
            BracketSeal.Sixth: Money(Decimal("62635000")),
        },
        MaritalStatus.MarriedJoint: {
            BracketSeal.First: Money(Decimal("2385000")),
            BracketSeal.Second: Money(Decimal("9695000")),
            BracketSeal.Third: Money(Decimal("20670000")),
            BracketSeal.Fourth: Money(Decimal("39460000")),
            BracketSeal.Fifth: Money(Decimal("50105000")),
            BracketSeal.Sixth: Money(Decimal("75160000"))
        },
    },
    TaxesVariables.Rate: {
        Rate.FirstBracket:  Decimal("0.1"),
        Rate.SecondBracket: Decimal("0.12"),
        Rate.ThirdBracket: Decimal("0.22"),
        Rate.FourthBracket: Decimal("0.24"),
        Rate.FifthBracket: Decimal("0.32"),
        Rate.SixthBracket: Decimal("0.35"),
        Rate.SeventhBracket: Decimal("0.37"),
        Rate.SocialSecurity: Decimal("0.062"),
        Rate.Medicare: Decimal("0.0145"),
    },
    TaxesVariables.Others: {
        Others.SSWageGap: Money(Decimal("17610000")),
    }
}
california_variables = { # I verified this myself
    TaxesVariables.StandardDeduction: {
        StandardDeduction.Singles: Money(Decimal("554000")),
        StandardDeduction.MarriedNoJoint: Money(Decimal("554000")),
        StandardDeduction.MarriedJoint: Money(Decimal("1108000")),
    },
    TaxesVariables.PersonalExemption: {
        PersonalExemption.Singles: Money(Decimal("14900")),
        PersonalExemption.MarriedJoint: Money(Decimal("29800")),
        PersonalExemption.MarriedNoJoint: Money(Decimal("29800")),
        PersonalExemption.Dependant: Money(Decimal("46100")),
    },
    TaxesVariables.BracketSeal: {
        MaritalStatus.Single:{
            BracketSeal.First: Money(Decimal("1075600")),
            BracketSeal.Second: Money(Decimal("2549900")),
            BracketSeal.Third: Money(Decimal("4024500")),
            BracketSeal.Fourth: Money(Decimal("5586600")),
            BracketSeal.Fifth: Money(Decimal("7060600")),
            BracketSeal.Sixth: Money(Decimal("36065900")),
            BracketSeal.Seventh: Money(Decimal("43278700")),
            BracketSeal.Eighth: Money(Decimal("72131400")),
            BracketSeal.Ninth: Money(Decimal("100000000")),
        },
        MaritalStatus.MarriedNoJoint: {
            BracketSeal.First: Money(Decimal("1075600")),
            BracketSeal.Second: Money(Decimal("2549900")),
            BracketSeal.Third: Money(Decimal("4024500")),
            BracketSeal.Fourth: Money(Decimal("5586600")),
            BracketSeal.Fifth: Money(Decimal("7060600")),
            BracketSeal.Sixth: Money(Decimal("36065900")),
            BracketSeal.Seventh: Money(Decimal("43278700")),
            BracketSeal.Eighth: Money(Decimal("72131400")),
            BracketSeal.Ninth: Money(Decimal("100000000")),
        },
        MaritalStatus.MarriedJoint: {
            BracketSeal.First: Money(Decimal("2151200")),
            BracketSeal.Second: Money(Decimal("5099800")),
            BracketSeal.Third: Money(Decimal("8049000")),
            BracketSeal.Fourth: Money(Decimal("11173200")),
            BracketSeal.Fifth: Money(Decimal("14173200")),
            BracketSeal.Sixth: Money(Decimal("72131800")),
            BracketSeal.Seventh: Money(Decimal("86557400")),
            BracketSeal.Eighth: Money(Decimal("100000000")),
            BracketSeal.Ninth: Money(Decimal("144262800")),
        },
    },
    TaxesVariables.Rate: {
        Rate.FirstBracket:  Decimal("0.01"),
        Rate.SecondBracket: Decimal("0.02"),
        Rate.ThirdBracket: Decimal("0.04"),
        Rate.FourthBracket: Decimal("0.06"),
        Rate.FifthBracket: Decimal("0.08"),
        Rate.SixthBracket: Decimal("0.09"),
        Rate.SeventhBracket: Decimal("0.103"),
        Rate.EighthBracket: Decimal("0.113"),
        Rate.NinthBracket: Decimal("0.123"),
        Rate.LastBracket: Decimal("0.133"),
    },
    TaxesVariables.StateBiggestBracketOrder: 9
}
new_york_variables = {
    TaxesVariables.StandardDeduction: {
        StandardDeduction.Singles: Money(Decimal("800000")),
        StandardDeduction.MarriedNoJoint: Money(Decimal("800000")),
        StandardDeduction.MarriedJoint: Money(Decimal("1605000")),
    },
    TaxesVariables.PersonalExemption: {
        PersonalExemption.Singles: Money(Decimal("0")),
        PersonalExemption.MarriedJoint: Money(Decimal("0")),
        PersonalExemption.MarriedNoJoint: Money(Decimal("0")),
        PersonalExemption.Dependant: Money(Decimal("0")),
    },
    TaxesVariables.BracketSeal: {
        MaritalStatus.Single: {
            BracketSeal.First: Money(Decimal("850000")),
            BracketSeal.Second: Money(Decimal("1170000")),
            BracketSeal.Third: Money(Decimal("1390000")),
            BracketSeal.Fourth: Money(Decimal("8065000")),
            BracketSeal.Fifth: Money(Decimal("21540000")),
            BracketSeal.Sixth: Money(Decimal("107755000")),
            BracketSeal.Seventh: Money(Decimal("500000000")),
            BracketSeal.Eighth: Money(Decimal("2500000000")),
        },
        MaritalStatus.MarriedNoJoint: {
            BracketSeal.First: Money(Decimal("1280000")),
            BracketSeal.Second: Money(Decimal("1765000")),
            BracketSeal.Third: Money(Decimal("2090000")),
            BracketSeal.Fourth: Money(Decimal("10765000")),
            BracketSeal.Fifth: Money(Decimal("26930000")),
            BracketSeal.Sixth: Money(Decimal("161645000")),
            BracketSeal.Seventh: Money(Decimal("500000000")),
            BracketSeal.Eighth: Money(Decimal("2500000000")),
        },
        MaritalStatus.MarriedJoint: {
            BracketSeal.First: Money(Decimal("1715000")),
            BracketSeal.Second: Money(Decimal("2360000")),
            BracketSeal.Third: Money(Decimal("2790000")),
            BracketSeal.Fourth: Money(Decimal("16155000")),
            BracketSeal.Fifth: Money(Decimal("32320000")),
            BracketSeal.Sixth: Money(Decimal("215535000")),
            BracketSeal.Seventh: Money(Decimal("500000000")),
            BracketSeal.Eighth: Money(Decimal("2500000000")),
        },
    },
    TaxesVariables.Rate: {
        Rate.FirstBracket: Decimal("0.04"),
        Rate.SecondBracket: Decimal("0.045"),
        Rate.ThirdBracket: Decimal("0.0525"),
        Rate.FourthBracket: Decimal("0.055"),
        Rate.FifthBracket: Decimal("0.06"),
        Rate.SixthBracket: Decimal("0.0685"),
        Rate.SeventhBracket: Decimal("0.0965"),
        Rate.EighthBracket: Decimal("0.103"),
        Rate.LastBracket: Decimal("0.109"),
    },
    TaxesVariables.StateBiggestBracketOrder: 8,
}
massachusetts_variables = {
    TaxesVariables.StandardDeduction: {
        StandardDeduction.Singles: Money(Decimal("440000")),
        StandardDeduction.MarriedNoJoint: Money(Decimal("440000")),
        StandardDeduction.MarriedJoint: Money(Decimal("880000")),
    },
    TaxesVariables.PersonalExemption: {
        PersonalExemption.Singles: Money(Decimal("0")),
        PersonalExemption.MarriedJoint: Money(Decimal("0")),
        PersonalExemption.MarriedNoJoint: Money(Decimal("0")),
        PersonalExemption.Dependant: Money(Decimal("0")),
    },
    TaxesVariables.BracketSeal: {
        MaritalStatus.Single: {
            BracketSeal.First: Money(Decimal("100000000")),
            BracketSeal.Second: Money(Decimal("Infinity")),
        },
        MaritalStatus.MarriedNoJoint: {
            BracketSeal.First: Money(Decimal("100000000")),
            BracketSeal.Second: Money(Decimal("Infinity")),
        },
        MaritalStatus.MarriedJoint: {
            BracketSeal.First: Money(Decimal("100000000")),
            BracketSeal.Second: Money(Decimal("Infinity")),
        },
    },
    TaxesVariables.Rate: {
        Rate.FirstBracket: Decimal("0.05"),
        Rate.SecondBracket: Decimal("0.09"),
    },
    TaxesVariables.StateBiggestBracketOrder: 2,
}
new_jersey_variables = {
    TaxesVariables.StandardDeduction: {
        StandardDeduction.Singles: Money(Decimal("1000000")),
        StandardDeduction.MarriedNoJoint: Money(Decimal("1000000")),
        StandardDeduction.MarriedJoint: Money(Decimal("2000000")),
    },
    TaxesVariables.PersonalExemption: {
        PersonalExemption.Singles: Money(Decimal("100000")),
        PersonalExemption.MarriedJoint: Money(Decimal("200000")),
        PersonalExemption.MarriedNoJoint: Money(Decimal("200000")),
        PersonalExemption.Dependant: Money(Decimal("150000")),
    },
    TaxesVariables.BracketSeal: {
        MaritalStatus.Single: {
            BracketSeal.First: Money(Decimal("2000000")),
            BracketSeal.Second: Money(Decimal("Infinity")),
        },
        MaritalStatus.MarriedNoJoint: {
            BracketSeal.First: Money(Decimal("2000000")),
            BracketSeal.Second: Money(Decimal("Infinity")),
        },
        MaritalStatus.MarriedJoint: {
            BracketSeal.First: Money(Decimal("2000000")),
            BracketSeal.Second: Money(Decimal("Infinity")),
        },
    },
    TaxesVariables.Rate: {
        Rate.FirstBracket: Decimal("0.014"),
        Rate.SecondBracket: Decimal("0.1075"),
    },
    TaxesVariables.StateBiggestBracketOrder: 1,
}
def order_to_bracket(order: int):
    if order == 1:
        return Bracket.First
    elif order == 2:
        return Bracket.Second
    elif order == 3:
        return Bracket.Third
    elif order == 4:
        return Bracket.Fourth
    elif order == 5:
        return Bracket.Fifth
    elif order == 6:
        return Bracket.Sixth
    elif order == 7:
        return Bracket.Seventh
    elif order == 8:
        return Bracket.Eighth
    elif order == 9:
        return Bracket.Ninth
    elif order == 10:
        return Bracket.Tenth
    elif order == 11:
        return Bracket.Eleventh
    elif order == 12:
        return Bracket.Twelfth
    elif order == 13:
        return Bracket.Last
    else:
        raise ValueError("Invalid order number")
def variables_to_dictionary(variables):
    return {
    "Comment":"Money value is in cents (value*100)",
    "TaxesVariables.StandardDeduction": {
        "StandardDeduction.Singles": str(variables[TaxesVariables.StandardDeduction][StandardDeduction.Singles].value),
        "StandardDeduction.MarriedNoJoint": str(variables[TaxesVariables.StandardDeduction][StandardDeduction.MarriedNoJoint].value),
        "StandardDeduction.MarriedJoint": str(variables[TaxesVariables.StandardDeduction][StandardDeduction.MarriedJoint].value)
    },
    "TaxesVariables.BracketSeal": {
        "MaritalStatus.Single": {
            "BracketSeal.First": str(variables[TaxesVariables.BracketSeal][MaritalStatus.Single][BracketSeal.First].value),
            "BracketSeal.Second": str(variables[TaxesVariables.BracketSeal][MaritalStatus.Single][BracketSeal.Second].value),
            "BracketSeal.Third": str(variables[TaxesVariables.BracketSeal][MaritalStatus.Single][BracketSeal.Third].value),
            "BracketSeal.Fourth": str(variables[TaxesVariables.BracketSeal][MaritalStatus.Single][BracketSeal.Fourth].value),
            "BracketSeal.Fifth": str(variables[TaxesVariables.BracketSeal][MaritalStatus.Single][BracketSeal.Fifth].value),
            "BracketSeal.Sixth": str(variables[TaxesVariables.BracketSeal][MaritalStatus.Single][BracketSeal.Sixth].value)
        },
        "MaritalStatus.MarriedNoJoint": {
            "BracketSeal.First": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedNoJoint][BracketSeal.First].value),
            "BracketSeal.Second": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedNoJoint][BracketSeal.Second].value),
            "BracketSeal.Third": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedNoJoint][BracketSeal.Third].value),
            "BracketSeal.Fourth": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedNoJoint][BracketSeal.Fourth].value),
            "BracketSeal.Fifth": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedNoJoint][BracketSeal.Fifth].value),
            "BracketSeal.Sixth": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedNoJoint][BracketSeal.Sixth].value)
        },
        "MaritalStatus.MarriedJoint": {
            "BracketSeal.First": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedJoint][BracketSeal.First].value),
            "BracketSeal.Second": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedJoint][BracketSeal.Second].value),
            "BracketSeal.Third": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedJoint][BracketSeal.Third].value),
            "BracketSeal.Fourth": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedJoint][BracketSeal.Fourth].value),
            "BracketSeal.Fifth": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedJoint][BracketSeal.Fifth].value),
            "BracketSeal.Sixth": str(variables[TaxesVariables.BracketSeal][MaritalStatus.MarriedJoint][BracketSeal.Sixth].value)
        }
    },
    "TaxesVariables.Rate": {
        "Rate.FirstBracket": str(variables[TaxesVariables.Rate][Rate.FirstBracket]),
        "Rate.SecondBracket": str(variables[TaxesVariables.Rate][Rate.SecondBracket]),
        "Rate.ThirdBracket": str(variables[TaxesVariables.Rate][Rate.ThirdBracket]),
        "Rate.FourthBracket": str(variables[TaxesVariables.Rate][Rate.FourthBracket]),
        "Rate.FifthBracket": str(variables[TaxesVariables.Rate][Rate.FifthBracket]),
        "Rate.SixthBracket": str(variables[TaxesVariables.Rate][Rate.SixthBracket]),
        "Rate.SeventhBracket": str(variables[TaxesVariables.Rate][Rate.SeventhBracket]),
        "Rate.SocialSecurity": str(variables[TaxesVariables.Rate][Rate.SocialSecurity]),
        "Rate.Medicare": str(variables[TaxesVariables.Rate][Rate.Medicare])
    },
    "TaxesVariables.Others": {
        "Others.SSWageGap": str(variables[TaxesVariables.Others][Others.SSWageGap].value)
    }
}
def dictionary_to_variables(dictionary):
    return {
    TaxesVariables.StandardDeduction: {
        StandardDeduction.Singles: Money(Decimal(dictionary["TaxesVariables.StandardDeduction"]["StandardDeduction.Singles"])),
        StandardDeduction.MarriedNoJoint: Money(Decimal(dictionary["TaxesVariables.StandardDeduction"]["StandardDeduction.MarriedNoJoint"])),
        StandardDeduction.MarriedJoint: Money(Decimal(dictionary["TaxesVariables.StandardDeduction"]["StandardDeduction.MarriedJoint"])),
    },
    TaxesVariables.BracketSeal: {
        MaritalStatus.Single: {
            BracketSeal.First: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.Single"]["BracketSeal.First"])),
            BracketSeal.Second: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.Single"]["BracketSeal.Second"])),
            BracketSeal.Third: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.Single"]["BracketSeal.Third"])),
            BracketSeal.Fourth: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.Single"]["BracketSeal.Fourth"])),
            BracketSeal.Fifth: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.Single"]["BracketSeal.Fifth"])),
            BracketSeal.Sixth: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.Single"]["BracketSeal.Sixth"])),
        },
        MaritalStatus.MarriedNoJoint: {
            BracketSeal.First: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedNoJoint"]["BracketSeal.First"])),
            BracketSeal.Second: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedNoJoint"]["BracketSeal.Second"])),
            BracketSeal.Third: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedNoJoint"]["BracketSeal.Third"])),
            BracketSeal.Fourth: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedNoJoint"]["BracketSeal.Fourth"])),
            BracketSeal.Fifth: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedNoJoint"]["BracketSeal.Fifth"])),
            BracketSeal.Sixth: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedNoJoint"]["BracketSeal.Sixth"])),
        },
        MaritalStatus.MarriedJoint: {
            BracketSeal.First: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedJoint"]["BracketSeal.First"])),
            BracketSeal.Second: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedJoint"]["BracketSeal.Second"])),
            BracketSeal.Third: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedJoint"]["BracketSeal.Third"])),
            BracketSeal.Fourth: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedJoint"]["BracketSeal.Fourth"])),
            BracketSeal.Fifth: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedJoint"]["BracketSeal.Fifth"])),
            BracketSeal.Sixth: Money(Decimal(dictionary["TaxesVariables.BracketSeal"]["MaritalStatus.MarriedJoint"]["BracketSeal.Sixth"])),
        },
    },
    TaxesVariables.Rate: {
        Rate.FirstBracket: Decimal(dictionary["TaxesVariables.Rate"]["Rate.FirstBracket"]),
        Rate.SecondBracket: Decimal(dictionary["TaxesVariables.Rate"]["Rate.SecondBracket"]),
        Rate.ThirdBracket: Decimal(dictionary["TaxesVariables.Rate"]["Rate.ThirdBracket"]),
        Rate.FourthBracket: Decimal(dictionary["TaxesVariables.Rate"]["Rate.FourthBracket"]),
        Rate.FifthBracket: Decimal(dictionary["TaxesVariables.Rate"]["Rate.FifthBracket"]),
        Rate.SixthBracket: Decimal(dictionary["TaxesVariables.Rate"]["Rate.SixthBracket"]),
        Rate.SeventhBracket: Decimal(dictionary["TaxesVariables.Rate"]["Rate.SeventhBracket"]),
        Rate.SocialSecurity: Decimal(dictionary["TaxesVariables.Rate"]["Rate.SocialSecurity"]),
        Rate.Medicare: Decimal(dictionary["TaxesVariables.Rate"]["Rate.Medicare"]),
    },
    TaxesVariables.Others: {
        Others.SSWageGap: Money(Decimal(dictionary["TaxesVariables.Others"]["Others.SSWageGap"])),
    }
}
def verify_dictionary_integrity(dictionary: dict):
    integrity = True
    while True:
        standard_ded_singles = dictionary.get("TaxesVariables.StandardDeduction", {}).get("StandardDeduction.Singles")
        standard_ded_married_no_joint = dictionary.get("TaxesVariables.StandardDeduction", {}).get(
            "StandardDeduction.MarriedNoJoint")
        standard_ded_married_joint = dictionary.get("TaxesVariables.StandardDeduction", {}).get(
            "StandardDeduction.MarriedJoint")

        bracket_seal_single_first = dictionary.get("TaxesVariables.BracketSeal", {}).get("MaritalStatus.Single",
                                                                                         {}).get(
            "BracketSeal.First")
        bracket_seal_single_second = dictionary.get("TaxesVariables.BracketSeal", {}).get("MaritalStatus.Single",
                                                                                          {}).get(
            "BracketSeal.Second")
        bracket_seal_single_third = dictionary.get("TaxesVariables.BracketSeal", {}).get("MaritalStatus.Single",
                                                                                         {}).get(
            "BracketSeal.Third")
        bracket_seal_single_fourth = dictionary.get("TaxesVariables.BracketSeal", {}).get("MaritalStatus.Single",
                                                                                          {}).get(
            "BracketSeal.Fourth")
        bracket_seal_single_fifth = dictionary.get("TaxesVariables.BracketSeal", {}).get("MaritalStatus.Single",
                                                                                         {}).get(
            "BracketSeal.Fifth")
        bracket_seal_single_sixth = dictionary.get("TaxesVariables.BracketSeal", {}).get("MaritalStatus.Single",
                                                                                         {}).get(
            "BracketSeal.Sixth")

        bracket_seal_married_no_joint_first = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedNoJoint", {}).get("BracketSeal.First")
        bracket_seal_married_no_joint_second = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedNoJoint", {}).get("BracketSeal.Second")
        bracket_seal_married_no_joint_third = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedNoJoint", {}).get("BracketSeal.Third")
        bracket_seal_married_no_joint_fourth = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedNoJoint", {}).get("BracketSeal.Fourth")
        bracket_seal_married_no_joint_fifth = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedNoJoint", {}).get("BracketSeal.Fifth")
        bracket_seal_married_no_joint_sixth = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedNoJoint", {}).get("BracketSeal.Sixth")

        bracket_seal_married_joint_first = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedJoint", {}).get("BracketSeal.First")
        bracket_seal_married_joint_second = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedJoint", {}).get("BracketSeal.Second")
        bracket_seal_married_joint_third = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedJoint", {}).get("BracketSeal.Third")
        bracket_seal_married_joint_fourth = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedJoint", {}).get("BracketSeal.Fourth")
        bracket_seal_married_joint_fifth = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedJoint", {}).get("BracketSeal.Fifth")
        bracket_seal_married_joint_sixth = dictionary.get("TaxesVariables.BracketSeal", {}).get(
            "MaritalStatus.MarriedJoint", {}).get("BracketSeal.Sixth")

        rate_first_bracket = dictionary.get("TaxesVariables.Rate", {}).get("Rate.FirstBracket")
        rate_second_bracket = dictionary.get("TaxesVariables.Rate", {}).get("Rate.SecondBracket")
        rate_third_bracket = dictionary.get("TaxesVariables.Rate", {}).get("Rate.ThirdBracket")
        rate_fourth_bracket = dictionary.get("TaxesVariables.Rate", {}).get("Rate.FourthBracket")
        rate_fifth_bracket = dictionary.get("TaxesVariables.Rate", {}).get("Rate.FifthBracket")
        rate_sixth_bracket = dictionary.get("TaxesVariables.Rate", {}).get("Rate.SixthBracket")
        rate_seventh_bracket = dictionary.get("TaxesVariables.Rate", {}).get("Rate.SeventhBracket")
        rate_social_security = dictionary.get("TaxesVariables.Rate", {}).get("Rate.SocialSecurity")
        rate_medicare = dictionary.get("TaxesVariables.Rate", {}).get("Rate.Medicare")

        others_ss_wage_gap = dictionary.get("TaxesVariables.Others", {}).get("Others.SSWageGap")
        break
    variables_to_check = [
    standard_ded_singles,
    standard_ded_married_no_joint,
    standard_ded_married_joint,

    bracket_seal_single_first,
    bracket_seal_single_second,
    bracket_seal_single_third,
    bracket_seal_single_fourth,
    bracket_seal_single_fifth,
    bracket_seal_single_sixth,

    bracket_seal_married_no_joint_first,
    bracket_seal_married_no_joint_second,
    bracket_seal_married_no_joint_third,
    bracket_seal_married_no_joint_fourth,
    bracket_seal_married_no_joint_fifth,
    bracket_seal_married_no_joint_sixth,

    bracket_seal_married_joint_first,
    bracket_seal_married_joint_second,
    bracket_seal_married_joint_third,
    bracket_seal_married_joint_fourth,
    bracket_seal_married_joint_fifth,
    bracket_seal_married_joint_sixth,

    rate_first_bracket,
    rate_second_bracket,
    rate_third_bracket,
    rate_fourth_bracket,
    rate_fifth_bracket,
    rate_sixth_bracket,
    rate_seventh_bracket,
    rate_social_security,
    rate_medicare,

    others_ss_wage_gap
]
    for variable in variables_to_check:
        if isinstance(variable, str):
            if not variable.replace(".", "").isdigit():
                integrity = False
        else:
            integrity = False
    return integrity
class Person:
    def __init__(self, first_name="", last_name="", pretax_income=Money(Decimal("0")), marital_status=MaritalStatus.NotSpecified, variables=None, state = State.NotSpecified, state_variables = None):
        self.first = first_name
        self.last = last_name
        self.income = pretax_income
        self.status = marital_status
        self.state = state
        if variables is None:
            self.variables = updatable_variables
        else:
            self.variables = variables
        default_state_variables = {
            State.California: california_variables, # Verified
            State.NewYork: new_york_variables, #ChatGPT crab
            State.Massachusetts: massachusetts_variables, #ChatGPT crab
            State.NewJersey: new_jersey_variables, #ChatGPT crab
        }
        if state_variables is None:
            if state in default_state_variables:
                self.state_variables = default_state_variables[self.state]
        else:
            self.state_variables = state_variables
    @property
    def state_bracket(self):
        order = self.state_variables[TaxesVariables.StateBiggestBracketOrder]
        while True:
            bracket = order_to_bracket(order)
            if order > 1:
                if self.state_taxable < self.state_variables[TaxesVariables.BracketSeal][self.status][
                    order_to_bracket(order - 1).seal]:
                    order -= 1
                else:
                    break
            else:
                break
        return bracket
    @property
    def state_exemption(self):
        if self.status == MaritalStatus.Single:
            return self.state_variables[TaxesVariables.PersonalExemption][PersonalExemption.Singles]
        elif self.status == MaritalStatus.MarriedNoJoint:
            return self.state_variables[TaxesVariables.PersonalExemption][PersonalExemption.MarriedNoJoint]
        elif self.status == MaritalStatus.MarriedJoint:
            return self.state_variables[TaxesVariables.PersonalExemption][PersonalExemption.MarriedJoint]
    @property
    def state_taxable(self):
        if self.income >= (self.state_deductions + self.state_exemption):
            return self.income - (self.state_deductions + self.state_exemption)
        else:
            return Money(Decimal("0"))
    @property
    def state_deductions(self):
        if self.status == MaritalStatus.Single:
            return self.state_variables[TaxesVariables.StandardDeduction][StandardDeduction.Singles]
        elif self.status == MaritalStatus.MarriedNoJoint:
            return self.state_variables[TaxesVariables.StandardDeduction][StandardDeduction.MarriedNoJoint]
        elif self.status == MaritalStatus.MarriedJoint:
            return self.state_variables[TaxesVariables.StandardDeduction][StandardDeduction.MarriedJoint]
    @property
    def deductions(self):
        if self.status == MaritalStatus.Single:
            return self.variables[TaxesVariables.StandardDeduction][StandardDeduction.Singles]
        elif self.status == MaritalStatus.MarriedNoJoint:
            return self.variables[TaxesVariables.StandardDeduction][StandardDeduction.MarriedNoJoint]
        elif self.status == MaritalStatus.MarriedJoint:
            return self.variables[TaxesVariables.StandardDeduction][StandardDeduction.MarriedJoint]

    @property
    def state_income(self):
        order = self.state_bracket.order
        taxable = self.state_taxable
        tax = Tax(Decimal("0"))
        while order >= 1:
            current_bracket_rate = self.state_variables[TaxesVariables.Rate][order_to_bracket(order).rate]
            if order > 1:
                previous_tax_seal = self.state_variables[TaxesVariables.BracketSeal][self.status][
                    order_to_bracket(order - 1).seal]
                # current_tax_seal = self.variables[TaxesVariables.BracketSeal][self.status][order_to_bracket(order-1).seal]
                tax += Tax(value=(taxable.value - previous_tax_seal.value) * current_bracket_rate)
                taxable = previous_tax_seal
            elif order == 1:
                added = taxable * self.state_variables[TaxesVariables.Rate][Rate.FirstBracket]
                tax += added
            order -= 1
        return tax
    @property
    def taxable(self):
        if self.income >= self.deductions:
            return self.income - self.deductions
        else:
            return Money(Decimal("0"))
    @property
    def bracket(self):
        order = 7
        while True:
            bracket = order_to_bracket(order)
            if order > 1:
                if self.taxable < self.variables[TaxesVariables.BracketSeal][self.status][order_to_bracket(order - 1).seal]:
                    order-=1
                else:
                    break
            else:
                break
        return bracket
    @property
    def total_state_tax(self):
        return Tax(value=Decimal(self.state_income.value))
    @property
    def federal_income(self):
        order = self.bracket.order
        taxable = self.taxable
        tax = Tax(Decimal("0"))
        while order >= 1:
            current_bracket_rate = self.variables[TaxesVariables.Rate][order_to_bracket(order).rate]
            if order > 1:
                previous_tax_seal = self.variables[TaxesVariables.BracketSeal][self.status][order_to_bracket(order-1).seal]
                # current_tax_seal = self.variables[TaxesVariables.BracketSeal][self.status][order_to_bracket(order-1).seal]
                tax += Tax(value=(taxable.value-previous_tax_seal.value) * current_bracket_rate)
                taxable = previous_tax_seal
            elif order == 1:
                added = taxable * self.variables[TaxesVariables.Rate][Rate.FirstBracket]
                tax += added
            order -= 1
        return tax
        # noinspection PyTypeChecker

    @property
    def medicare(self):
        return Tax(self.income.value * self.variables[TaxesVariables.Rate][Rate.Medicare])
    @property
    def social_security(self):
        if self.income < self.variables[TaxesVariables.Others][Others.SSWageGap]:
            return Tax(value=(self.income.value * self.variables[TaxesVariables.Rate][Rate.SocialSecurity]))
        else:
            return Tax(value=(self.variables[TaxesVariables.Others][Others.SSWageGap].value * self.variables[TaxesVariables.Rate][Rate.SocialSecurity]))
    @property
    def total_federal(self):
        return Tax(value=Decimal(self.federal_income.value + self.medicare.value + self.social_security.value))
    @property
    def total_tax(self):
        if self.state == State.NotSpecified:
            return self.total_federal
        else:
            return Tax(value=Decimal(self.total_federal.value + self.total_state_tax.value))
    @property
    def post_tax(self):
        return self.income - self.total_tax
    def dictionary_format(self):
        return {
            "first name": str(self.first),
            "last name": str(self.last),
            "status": str(self.status),
            "income": str(self.income.value),
            "tax deductions": str(self.deductions.value),
            "taxable income": str(self.taxable.value),
            "total federal taxes": str(self.total_federal.value),
            "income tax": str(self.federal_income.value),
            "social security tax": str(self.social_security.value),
            "medicare tax": str(self.medicare.value),
            "net income": str(self.post_tax.value),
        }
def str_to_money_usd(string: str):
    if string.replace("$", "").replace(".", "", 1).isdigit():
        plain_string = string.replace("$", "")
        return Money(value=Decimal(plain_string)*Decimal("100"))
    else:
        return None
def dictionary_to_person(dictionary: dict, identity: str):
    first_name = ""
    last_name = ""
    status = ""
    s_income = ""
    for a_id, details in dictionary.items():
        if a_id == identity:
            for key, value in details.items():
                if key == "first name":
                    first_name = value
                elif key == "last name":
                    last_name = value
                elif key == "status":
                    status = value
                elif key == "income":
                    s_income = value
    modified_status= MaritalStatus[status]
    income = Money(value=Decimal(s_income))
    # noinspection PyTypeChecker
    return Person(first_name, last_name,income, modified_status)
if __name__ == '__main__':
    # from Abdalla.My_Functions import read_simple_dictionary
    test = Person("Abdalla", "Elsoni", Money(Decimal("16050000")), MaritalStatus.Single, state=State.California)
    # print(test.variables[TaxesVariables.BracketSeal][test.status][BracketSeal.First])
    print(test.total_state_tax)
    # print(order_to_bracket(1).seal)

# test = Person("Abdalla", "Elsoni", Money(Decimal("5000000")), MaritalStatus.Single)
# print(test.post_tax)
# print(type(test.post_tax))
# print(type(test.total_tax))
# print(type(test.medicare))
# print(type(test.social_security))
# print(type(test.federal_income))
# unique = datetime.datetime(2025,2,15)
# loan = Debt(12000,0.36,unique)
# read_nested_dictionary(loan.records)
