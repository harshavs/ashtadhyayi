from ashtadhyayi.pratyahara import वर्णाः
from ashtadhyayi.utils import कु, स्वरात्_मात्रा


def आदेशप्रत्यययोः_८_३_५९(पदम्, आदेशप्रत्ययः):
    इण् = वर्णाः('इण्', True)
    इण्कु = इण् + स्वरात्_मात्रा(इण्) + कु()

    if (पदम्[-1] in इण्कु or (पदम्[-1] == '्' and पदम्[-2] in इण्कु)) and आदेशप्रत्ययः[0] == 'स':
        return आदेशप्रत्ययः.replace('स', 'ष', 1)
