volume=float(input('Wie viel Knoop-Medium soll hergestellt werden?'))

mg_per_liter={
    'KH2PO4':250,
    'KCl':250,
    'MgSO4':250,
    'CaNO32':1000,
    'FeSO4':12.5
}

output='''
      Sie benötigen:
      KH\u2082PO\u2084:\t{KH2PO4} mg
      KCl:\t{KCl} mg
      MgSO\2084 - 7 H\u2082O:\t{MgSO4} mg
      Ca(NO\u2083)\u2082 - 4 H\u2082O:\t{CaNO32} mg
      FeSO\u2084 - 7 H\u2082O:\t{FeSO4} mg

      Stellen sie den pH mit 1 N NaOH auf 5.8 ein.
      '''

print(output.format(
    KH2PO4=round(volume*mg_per_liter['KH2PO4'],3),
    KCl=round(volume*mg_per_liter['KCl'],3),
    MgSO4=round(volume*mg_per_liter['MgSO4'],3),
    CaNO32=round(volume*mg_per_liter['CaNO32'],3),
    FeSO4=round(volume*mg_per_liter['FeSO4'],3)
))
