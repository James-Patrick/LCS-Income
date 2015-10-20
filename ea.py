import math
import random
from enum import Enum

AGEMIN = 20
AGEMAX = 60
AGEDEV = 10

FNLMIN = 100000 
FNLMAX = 400000
FNLDEV = 50000

EDUMIN = 6
EDUMAX = 12
EDUDEV = 3

CAPITALMIN = 10000
CAPITALMAX = 24000
CAPITALDEV = 4000

HOURSMIN = 8
HOURSMAX = 40
HOURSDEV = 4


N_GENOME_CTS_ATTRIBUTES = 12
LEARNING_RATE = 1/math.sqrt(N_GENOME_CTS_ATTRIBUTES)
EPSILON = 0.5

CTS_ATTRIBUTES = ['AGE','FNLWGT','EDUCATION_NUM','CAPITAL_GAIN','CAPITAL_LOSS','HOURS_PER_WEEK']
ENUM_ATTRIBUTES = {'WORKCLASS':7, 'EDUCATION':15,'MARITAL_STATUS':6,'OCCUPATION':14,'RELATIONSHIP':5,'RACE':4,'SEX':1,'NATIVE_COUNTRY':40}
ALL_ATTRIBUTES = CTS_ATTRIBUTES + list(ENUM_ATTRIBUTES.keys())

class WORKCLASS(Enum):
    PRIVATE = 0
    SELF_EMP_NOT_INC = 1
    SELF_EMP_INC = 2
    FEDERAL_GOV = 3
    LOCAL_GOV = 4
    STATE_GOV = 5
    WITHOUT_PAY = 6
    NEVER_WORKED = 7

class EDUCATION(Enum):
    BACHELORS = 0
    SOME_COLLEGE = 1
    _11TH = 2
    HS_GRAD = 3
    PROF_SCHOOL = 4
    ASSOC_ACDM = 5
    ASSOC_VOC = 6
    _9TH = 7
    _7TH_8TH = 8
    _12TH = 9
    MASTERS = 10
    _1ST_4TH = 11
    _10TH = 12
    DOCTORATE = 13
    _5TH_6TH = 14
    PRESCHOOL = 15

class MARITAL_STATUS(Enum):
    MARRIED_CIV_SPOUSE = 0
    DIVORCED = 1
    NEVER_MARRIED = 2
    SEPARATED = 3
    WIDOWED = 4
    MARRIED_SPOUSE_ABSENT = 5
    MARRIED_AF_SPOUSE = 6

class OCCUPATION(Enum):
    TECH_SUPPORT = 0
    CRAFT_REPAIR = 1
    OTHER_SERVICE = 3
    SALES = 4
    EXEC_MANAGERIAL = 5
    PROF_SPECIALTY = 6
    HANDLERS_CLEANERS = 7
    MACHINE_OP_INSPCT = 8
    ADM_CLERICAL = 9
    FARMING_FISHING = 10
    TRANSPORT_MOVING = 11
    PRIV_HOUSE_SERV = 12
    PROTECTIVE_SERV = 13
    ARMED_FORCES = 14

class RELATIONSHIP(Enum):
    WIFE = 0
    OWN_CHILD = 1
    HUSBAND = 2
    NOT_IN_FAMILY = 3
    OTHER_RELATIVE = 4
    UNMARRIED = 5

class RACE(Enum):
    WHITE = 0
    ASIAN_PAC_ISLANDER = 1
    AMER_INDIAN_ESKIMO = 2
    OTHER = 3
    BLACK = 4

class SEX(Enum):
    FEMALE = 0
    MALE = 1

class NATIVE_COUNTRY(Enum):
    UNITED_STATES = 0
    CAMBODIA = 1
    ENGLAND = 2
    PUERTO_RICO = 3
    CANADA = 4
    GERMANY = 5
    OUTLYING_US = 6
    INDIA = 7
    JAPAN = 8
    GREECE = 9
    SOUTH = 10
    CHINA = 11
    CUBA = 12
    IRAN = 13
    HONDURAS = 14
    PHILIPPINES = 15
    ITALY = 16
    POLAND = 17
    JAMAICA = 18
    VIETNAM = 19
    MEXICO = 20
    PORTUGAL = 21
    IRELAND = 22
    FRANCE = 23
    DOMINICAN_REPUBLIC = 24
    LOAS = 25
    ECUADOR = 26
    TAIWAN = 27
    HAITI = 28
    COLOMBIA = 29
    HUNGARY = 30
    GUATEMALA = 31
    NICARAGUE = 32
    SCOTLAND = 33
    THAILAND = 34
    YUGOSLAVIA = 35
    EL_SALVADOR = 36
    TRINIDAD_TOBAGO = 37
    PERU = 38
    HONG = 39
    HOLAND_NETHERLANDS = 40

class CtsValue(object):
    def __init__(self, maxBound, sigmamax, minBound, sigmamin):
        self.maxBound = maxBound
        self.sigmamax = sigmamax
        self.minBound = minBound
        self.sigmamin = sigmamin

class Rule(object):
    def __init__(self, data):
        self.data = data
        self.prediction = false
        
    def getMutantChild(self):
        #create new rule object
        child = Rule(self.data)
        #iterate over the values in the dictionary
        for key, value in child.data:
            #mutate a continous value
            if (key in CTS_ATTRIBUTES):
                value.sigmamax = max(value.sigmamax * math.exp(LEARNING_RATE * random.normalvariate(0, 1)), EPSILON)
                value.sigmamin = max(value.sigmamin * math.exp(LEARNING_RATE * random.normalvariate(0, 1)), EPSILON)
                value.minBound = max(int(value.minBound + sigmamax * random.normalvariate(0, 1)), 0)
                value.maxBound = max(int(value.maxBound + sigmamax * random.normalvariate(0, 1)), value.minBound)
            else:
                #if not continuous, check probability and maybe add new entry
                if(random.random() < LEARNING_RATE/value.length):
                    newEntry = random.radint(0, maxEnumVal(key))
                    #make sure its not a duplicate
                    while(value.contains(newEntry)):
                          newEntry = random.radint(0, ENUM_ATTRIBUTES[KEY])
                    value.add(newEntry)
                    #if we didnt add one, maybe we should remmove one
                elif(random.random() < LEARNING_RATE/value.length and len(value) > 1):
                    value.remove(random.radint(0, ENUM_ATTRIBUTES[key]))
        if (random.random() < LEARNING_RATE/len(self.data)):
            newKey = random.randint(0, len(ALL_ATTRIBULTS))
            while (newKey in self.dict):
                newKey = random.randint(0, len(ALL_ATTRIBULTS))
            if (key in CTS_ATTRIBUTES):
                newValue = generateCtsInitial(newKey)
            else:
                newValue = random.radint(0, ENUM_ATTRIBUTES[KEY])
            child.data[newkey] = newValue
        child.precition = self.prediction
        return child

def generateCtsInitial(key):
    minBound = 0
    maxBound = 0
    sigmamax = 0
    sigmamin = 0
    if (key == 'AGE'):
        sigmamax = AGEDEV
        sigmamin = AGEDEV
        minBound = random.normalvariate(AGEMIN, AGEDEV)
        maxBound = random.normalvariate(AGEMAX, AGEDEV)
    elif (key == 'FNLWGT'):
        sigmamax = FNLDEV
        sigmamin = FNLDEV
        minBound = random.normalvariate(FNLMIN, FNLDEV)
        maxBound = random.normalvariate(FNLMAX, FNLDEV)
    elif (key == 'EDUCATION_NUM'):
        sigmamax = EDUDEV
        sigmamin = EDUDEV
        minBound = random.normalvariate(EDUMIN, EDUDEV)
        maxBound = random.normalvariate(EDUMAX, EDUDEV)
    elif ((key == 'CAPITAL_GAIN') or (key == 'CAPITAL_LOSS')):
        sigmamax = CAPITALDEV
        sigmamin = CAPITALDEV
        minBound = random.normalvariate(CAPITALMIN, CAPITALDEV)
        maxBound = random.normalvariate(CAPITALMAX, CAPITALDEV)
    elif (key == 'HOURS_PER_WEEK'):
        sigmamax = HOURSDEV
        sigmamin = HOURSDEV
        minBound = random.normalvariate(HOURSMIN, HOURSDEV)
        maxBound = random.normalvariate(HOURSMAX, HOURSDEV)
        
        
    return CtsValue(axBount, sigmamax, minBound, sigmamin)
