num_of_el = int(input())
el_filled_atoms = []
atom = 1

while num_of_el > 0:
    filled_atom = 2 * (atom*atom)
    if num_of_el >= filled_atom:
        el_filled_atoms.append(filled_atom)
    else:
        el_filled_atoms.append(num_of_el)
    atom +=1
    num_of_el -= filled_atom

print(el_filled_atoms)