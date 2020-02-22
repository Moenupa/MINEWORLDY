unprinted_designs = ['iphone case','robot pendent','dodecahedron']
completed_designs = []

#print every design
while unprinted_designs:
    current_design = unprinted_designs.pop()

    print('Printing model:'+current_design)
    completed_designs.append(current_design)

#display all
print('\nThe following models has been printed:')
for completed_model in completed_designs:
    print('\t'+completed_model)
