'''Individual Programming Assignment 1

20 points

This assignment will develop your basic familiarity with Python.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    5 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.

    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def savings(gross_pay, tax_rate, expenses):
    after_tax = int(gross_pay * (1 - tax_rate))
    remaining = (after_tax - expenses)
    return remaining
    

def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    5 points.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def material_waste(total_material, material_units, num_jobs, job_consumption):
    gross_job_consumption = int(num_jobs * job_consumption)
    net_material = int(total_material - gross_job_consumption)
    remaining = str(net_material) + material_units
    return remaining



def interest(principal, rate, periods):
    '''Interest.
    5 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time).
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def interest(principal, rate, periods):
    simple_interest = (principal * (rate * periods))
    FV = int(principal + simple_interest)
    return FV

def body_mass_index(weight, height):
    '''Body Mass Index.
    5 points.

    This function calculates the body mass index (BMI) of a person
        given their weight and height.

    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)

    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.

    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].

    We have not yet discussed lists, but use the skills you developed
        in the command line exercise. How would you learn how to work with
        lists?

    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def body_mass_index(weight, height):
    weight_kg = weight * 0.45359237
    height_ft = height[0]
    height_in = height[1]
    height_m = ((height_ft * 12) + height_in) * 0.0254
    bmi = weight_kg / (height_m ** 2)
    return bmi
