letters = '''
Dear {salution} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.

Send us your receipt and {amount} for shipping and handing. We will send
you another {product} that, in pur tests, is {percent} % less likely to
have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
'''

response = {'salution' : 'testA', 'name' : 'solutionAAAA', 'product' : 'turai', 'verbed' : 'iroiro',
            'room' : 'roomA', 'animals' : 'AnimalsAA', 'amount' : 'trtrtr', 'percent' : 120, 'spokesman' : 'Robelt',
            'job_title' : 'nikki'}

print(letters.format(**response))
