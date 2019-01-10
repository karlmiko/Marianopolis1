def findPayment(loan, r, m):
    '''Assumes: 'loan' and 'r' are floats, 'm' an int
       Returns the monthly payment for a mortgage of size
       'loan' at a monthly rate of 'r' for 'm' months.'''
    return loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1))

class Mortgage(object):
    '''Abstract class for building different types of mortgages.'''
    def __init__(self, loan, annualRate, months):
        '''Create a new mortgage object.'''
        self.loan = loan        # Initial loan amount.
        self.rate = annualRate / (12.0 * 100.0) # Monthly rate.
        self.months = months    # Duration of the loan in months.
        self.paid = [0.0]       # List of payments made.
        self.owed = [loan]      # List of loan balances.
        # The payment attribute is the minimum payment due each
        # month.
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None      # Description of the mortgage.

    def makePayment(self, extra = 0): # Question 1.6: Add extra = 0
        '''Make a payment to a mortgage.
        
        Applies the current minimum payment by appending it to
        the end of the 'paid' attribute, and updating the current
        balance to reflect the payment and interest charges.
        '''
        total_payment = self.payment + extra # Question 1.6: Add + extra
        remaining = self.owed[-1]
        # Never pay more than the amount owed!
        total_payment = min(total_payment, remaining)
        self.paid.append(total_payment)
        reduction = total_payment - remaining * self.rate
        self.owed.append(remaining - reduction)

    def getTotalPaid(self):
        '''Return the total amount paid so far.'''
        return sum(self.paid)

    def __str__(self):
        '''Returns a string representation of the mortgage.'''
        return self.legend

class FixedRate(Mortgage):
    '''Represents a standard 'fixed-rate' mortgage.'''
    def __init__(self, loan, r, months):
        super().__init__(loan, r, months)
        self.legend = 'Fixed, {:g}%'.format(r)

class FixedRateWithPoints(Mortgage):
    '''Represents a 'fixed-rate' mortgage that charges a certain
    percentage of the loan as an up-front cost.'''
    def __init__(self, loan, r, months, pts):
        super().__init__(loan, r, months)
        self.paid = [loan * (pts / 100.0)]
        self.legend = 'Fixed, {:g}%, {:g} points'.format(r, pts)

class TeaserRate(Mortgage):
    '''A 'teaser' rate mortgage has a lower rate for the first few months 
    (typically 1-4 years), but the rate rises after that time expires.
    Implementing this requires us to extend the makePayment method.
    '''
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        super().__init__(loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.nextRate = r / (12.0 * 100.0)
        self.legend = '{:g}% for {} months, then {:g}%'.format(teaserRate, teaserMonths, r)

    def makePayment(self, extra = 0): # Question 1.6: Add extra = 0
        '''Extended version of the method for the TeaserRate class.

        The idea is that once we have paid into the mortgage for teaserMonths,
        the rate changes to the nextRate value. We have to update the payment
        accordingly. Finally, we call the base class implementation of
        makePayment to actually finish the job.'''
        
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.owed[-1], self.rate,
                                       self.months - self.teaserMonths)
        super().makePayment(extra) # Question 1.6: Add extra

def compareMortgages(totMonths, adtPayment = 0, *args): # Question 1.6: Add adtPayment = 0
    '''Compare several mortgages over a period of totMonths.'''
    for m in range(totMonths):
        for mort in args:
            mort.makePayment(adtPayment) # Question 1.6: Add adtPayment
    for mort in args:
        print(mort, end=' ')
        print('Total payments = ${:g}'.format(mort.getTotalPaid()))

# 'Main' program - actually run the comparisons.
#
YEARS = 30
AMT = 200000
totMonths = YEARS * 12
adtPayment = 68 # Question 1.6: Add adtPayment = 68

# Create a fixed-rate mortgage at 7.0% annual interest.
fixed1 = FixedRate(AMT, 7.0, totMonths)

# Create a fixed-rate mortgage with points at 5.0% annual interest.
fixed2 = FixedRateWithPoints(AMT, 5.0, totMonths, 3.25)

# Create a two-rate mortgage with an initial rate of 4.5% and a
# final rate of 9.5%.
twoRate = TeaserRate(AMT, 9.5, totMonths, 4.5, 48)

#----1.5----#
fixed3 = FixedRate(AMT, 7.5, totMonths)
#----1.5----#

# Now run the comparison of all of the mortgages.
compareMortgages(totMonths, adtPayment, fixed1, fixed2, fixed3, twoRate)
