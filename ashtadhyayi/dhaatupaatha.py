from ashtadhyayi.it_samjna_prakarana import उपदेशसंज्ञकः, इत्


with open('ashtadhyayi/dhaatupaatha.txt') as dhaatupatha:
    count = 0
    for dhaatu in dhaatupatha:
        # Skip first two lines
        if count < 2:
            count += 1
        elif count < 6:
            count += 1
            dhaatu = dhaatu.split(',')
            dhaatu[8] = dhaatu[8].replace('\n', '')
            upadesha = dhaatu[2].replace(' ', '')
            upadesha = upadesha.split('(')
            upadesha[1] = upadesha[1].replace(')', '')
            dhaatu[2] = upadesha
            dhaatu.append(इत्(dhaatu[2][0], उपदेशसंज्ञकः.धातुः))
            print(dhaatu)
