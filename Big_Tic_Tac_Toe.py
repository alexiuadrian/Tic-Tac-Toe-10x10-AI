import time

# Verifica daca 
def check_exit(string):
    if string == 'exit':
        return True
    return False

# Verifica daca se poate plasa o placuta (daca nu el nu sunt pe diagonala si daca sunt langa minim un X si un 0)
def check_position(matr, linie1, coloana1, linie2, coloana2):
    if abs(linie1 - linie2) <= 1 and abs(coloana1 - coloana2) <= 1 and abs(abs(coloana1 - coloana2) + abs(linie1 - linie2)) != 2:
        check_X = False
        check_0 = False
        # Cauta daca exista minim un X si un 0 pe langa placuta

        # Verific daca sunt pe orizontala
        if linie1 == linie2:
            # Verific daca sunt pe prima linie
            if linie1 == 0:
                # Verific daca sunt in stanga de tot
                if min(coloana1, coloana2) == 0:
                    # Verific vecinii de dedesubtul, diagonala dreapta si dreapta placutei (daca cel putin unul este x)
                    if matr[10] == 'x' or matr[11] == 'x' or matr[12] == 'x' or matr[2] == 'x':
                        check_X = True
                    
                    # Verific vecinii de dedesubtul, diagonala dreapta si dreapta placutei (daca cel putin unul este 0)
                    if matr[10] == '0' or matr[11] == '0' or matr[12] == '0' or matr[2] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True

                # Verific daca sunt in dreapta de tot
                elif max(coloana1, coloana2) == 9:
                    # Verific vecinii din stanga, dedesubtul placutei si diagonala stanga (daca cel putin unul este x)
                    if matr[7] == 'x' or matr[18] == 'x' or matr[19] == 'x' or matr[17] == 'x':
                        check_X = True
                    
                    # Verific vecinii din stanga, dedesubtul placutei si diagonala stanga (daca cel putin unul este 0)
                    if matr[7] == '0' or matr[18] == '0' or matr[19] == '0' or matr[17] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True
                
                else:
                    # Verific vecinii: stanga, diagonala stanga, dedesubt, diagonala dreapta, dreapta daca e cel putin un x
                    if matr[min(coloana1, coloana2) - 1] == 'x' or matr[10 + min(coloana1, coloana2) - 1] == 'x' or matr[10 + min(coloana1, coloana2)] == 'x' or matr[10 + max(coloana1, coloana2)] == 'x' or matr[10 + max(coloana1, coloana2) + 1] == 'x' or matr[max(coloana1, coloana2) + 1] == 'x':
                        check_X == True

                    # Verific vecinii: stanga, diagonala stanga, dedesubt, diagonala dreapta, dreapta daca e cel putin un 0
                    if matr[min(coloana1, coloana2) - 1] == '0' or matr[10 + min(coloana1, coloana2) - 1] == '0' or matr[10 + min(coloana1, coloana2)] == '0' or matr[10 + max(coloana1, coloana2)] == '0' or matr[10 + max(coloana1, coloana2) + 1] == '0' or matr[max(coloana1, coloana2) + 1] == '0':
                        check_0 == True

                    if check_X and check_0:
                        return True

            # Verific daca sunt pe ultima linie
            elif linie1 == 9:
                # Verific daca sunt in stanga de tot
                if min(coloana1, coloana2) == 0:
                    # Verific vecinii de deasupra, diagonala dreapta si dreapta placutei (daca cel putin unul este x)
                    if matr[80] == 'x' or matr[81] == 'x' or matr[82] == 'x' or matr[92] == 'x':
                        check_X = True
                    
                    # Verific vecinii de deasupra, diagonala dreapta si dreapta placutei (daca cel putin unul este 0)
                    if matr[80] == '0' or matr[81] == '0' or matr[82] == '0' or matr[92] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True

                # Verific daca sunt in dreapta de tot
                elif max(coloana1, coloana2) == 9:
                    # Verific vecinii din stanga, deasupra placutei si diagonala stanga (daca cel putin unul este x)
                    if matr[97] == 'x' or matr[88] == 'x' or matr[89] == 'x' or matr[87] == 'x':
                        check_X = True
                    
                    # Verific vecinii din stanga, deasupra placutei si diagonala stanga (daca cel putin unul este 0)
                    if matr[97] == '0' or matr[88] == '0' or matr[89] == '0' or matr[87] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True
                
                else:
                    # Verific vecinii: stanga, diagonala stanga, dedesubt, diagonala dreapta, dreapta daca e cel putin un x
                    if matr[90 + min(coloana1, coloana2) - 1] == 'x' or matr[80 + min(coloana1, coloana2) - 1] == 'x' or matr[80 + min(coloana1, coloana2)] == 'x' or matr[80 + max(coloana1, coloana2)] == 'x' or matr[80 + max(coloana1, coloana2) + 1] == 'x' or matr[90 + max(coloana1, coloana2) + 1] == 'x':
                        check_X == True

                    # Verific vecinii: stanga, diagonala stanga, dedesubt, diagonala dreapta, dreapta daca e cel putin un 0
                    if matr[90 + min(coloana1, coloana2) - 1] == '0' or matr[80 + min(coloana1, coloana2) - 1] == '0' or matr[80 + min(coloana1, coloana2)] == '0' or matr[80 + max(coloana1, coloana2)] == '0' or matr[80 + max(coloana1, coloana2) + 1] == '0' or matr[90 + max(coloana1, coloana2) + 1] == '0':
                        check_0 == True

                    if check_X is True and check_0 is True:
                        return True

            # Daca sunt pe linii intermediare
            else:
                # Verific daca sunt in stanga de tot
                if min(coloana1, coloana2) == 0:
                    # Verific vecinii de deasupra, diagonala dreapta sus, dreapta, diagonala dreapta jos, dedesubtul placutei (daca cel putin unul este x)
                    if matr[(linie1 - 1) * 10 + min(coloana1, coloana2)] == 'x' or matr[(linie1 - 1) * 10 + max(coloana1, coloana2)] == 'x' or matr[(linie1 - 1) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[linie1 * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[(linie1 + 1) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[(linie1 + 1) * 10 + max(coloana1, coloana2)] == 'x' or matr[(linie1 + 1) * 10 + min(coloana1, coloana2)] == 'x':
                        check_X = True
                    
                    # Verific vecinii de deasupra, diagonala dreapta sus, dreapta, diagonala dreapta jos, dedesubtul placutei (daca cel putin unul este 0)
                    if matr[(linie1 - 1) * 10 + min(coloana1, coloana2)] == '0' or matr[(linie1 - 1) * 10 + max(coloana1, coloana2)] == '0' or matr[(linie1 - 1) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[linie1 * 10 + max(coloana1, coloana2) + 1] == '0' or matr[(linie1 + 1) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[(linie1 + 1) * 10 + max(coloana1, coloana2)] == '0' or matr[(linie1 + 1) * 10 + min(coloana1, coloana2)] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True

                # Verific daca sunt in dreapta de tot
                elif max(coloana1, coloana2) == 9:
                    # Verific vecinii din deasupra, diagonala stanga sus, stanga, diagonala stanga jos, dedesubt (daca cel putin unul este x)
                    if matr[(linie1 - 1) * 10 + max(coloana1, coloana2)] == 'x' or matr[(linie1 - 1) * 10 + min(coloana1, coloana2)] == 'x' or matr[(linie1 - 1) * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[(linie1) * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[(linie1 + 1) * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[(linie1 + 1) * 10 + min(coloana1, coloana2)] == 'x' or matr[(linie1 + 1) * 10 + max(coloana1, coloana2)] == 'x':
                        check_X = True
                    
                    # Verific vecinii din stanga, deasupra placutei si diagonala stanga (daca cel putin unul este 0)
                    if matr[(linie1 - 1) * 10 + max(coloana1, coloana2)] == '0' or matr[(linie1 - 1) * 10 + min(coloana1, coloana2)] == '0' or matr[(linie1 - 1) * 10 + min(coloana1, coloana2) - 1] == '0' or matr[(linie1) * 10 + min(coloana1, coloana2) - 1] == '0' or matr[(linie1 + 1) * 10 + min(coloana1, coloana2) - 1] == '0' or matr[(linie1 + 1) * 10 + min(coloana1, coloana2)] == '0' or matr[(linie1 + 1) * 10 + max(coloana1, coloana2)] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True
                
                else:
                    # Verific vecinii: stanga, diagonala stanga, dedesubt, diagonala dreapta, dreapta daca e cel putin un x
                    if matr[linie1 * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[(linie1 + 1) * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[(linie1 + 1) * 10 + min(coloana1, coloana2)] == 'x' or matr[(linie1 + 1) * 10 + max(coloana1, coloana2)] == 'x' or matr[(linie1 + 1) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[linie1 * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[(linie1 - 1) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[(linie1 - 1) * 10 + max(coloana1, coloana2)] == 'x' or matr[(linie1 - 1) * 10 + min(coloana1, coloana2)] == 'x' or matr[(linie1 - 1) * 10 + min(coloana1, coloana2) - 1] == 'x':
                        check_X = True

                    # Verific vecinii: stanga, diagonala stanga jos, dedesubt, diagonala dreapta jos, dreapta, diagonala dreapta sus, deasupra, diagonala stanga sus daca e cel putin un 0
                    if matr[linie1 * 10 + min(coloana1, coloana2) - 1] == '0' or matr[(linie1 + 1) * 10 + min(coloana1, coloana2) - 1] == '0' or matr[(linie1 + 1) * 10 + min(coloana1, coloana2)] == '0' or matr[(linie1 + 1) * 10 + max(coloana1, coloana2)] == '0' or matr[(linie1 + 1) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[linie1 * 10 + max(coloana1, coloana2) + 1] == '0' or matr[(linie1 - 1) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[(linie1 - 1) * 10 + max(coloana1, coloana2)] == '0' or matr[(linie1 - 1) * 10 + min(coloana1, coloana2)] == '0' or matr[(linie1 - 1) * 10 + min(coloana1, coloana2) - 1] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True
        
        # Verific daca sunt pe verticala
        if coloana1 == coloana2:
            # Verific daca sunt pe prima linie
            if min(linie1, linie2) == 0:
                # Verific daca sunt in stanga de tot
                if min(coloana1, coloana2) == 0:
                    # Verific vecinii de dedesubtul, diagonala dreapta si dreapta placutei (daca cel putin unul este x)
                    if matr[20] == 'x' or matr[21] == 'x' or matr[1] == 'x' or matr[11] == 'x':
                        check_X = True
                    
                    # Verific vecinii de dedesubtul, diagonala dreapta si dreapta placutei (daca cel putin unul este 0)
                    if matr[20] == '0' or matr[21] == '0' or matr[1] == '0' or matr[11] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True

                # Verific daca sunt in dreapta de tot
                elif max(coloana1, coloana2) == 9:
                    # Verific vecinii din stanga, dedesubtul placutei si diagonala stanga (daca cel putin unul este x)
                    if matr[8] == 'x' or matr[18] == 'x' or matr[29] == 'x' or matr[28] == 'x':
                        check_X = True
                    
                    # Verific vecinii din stanga, dedesubtul placutei si diagonala stanga (daca cel putin unul este 0)
                    if matr[8] == '0' or matr[18] == '0' or matr[29] == '0' or matr[28] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True
                
                else:
                    # Verific vecinii: stanga, diagonala stanga, dedesubt, diagonala dreapta, dreapta daca e cel putin un x
                    if matr[min(coloana1, coloana2) - 1] == 'x' or matr[10 + min(coloana1, coloana2) - 1] == 'x' or matr[20 + min(coloana1, coloana2) - 1] == 'x' or matr[20 + min(coloana1, coloana2)] == 'x' or matr[20 + max(coloana1, coloana2) + 1] == 'x' or matr[max(coloana1, coloana2) + 1] == 'x' or matr[10 + max(coloana1, coloana2) + 1] == 'x':
                        check_X = True

                    # Verific vecinii: stanga, diagonala stanga, dedesubt, diagonala dreapta, dreapta daca e cel putin un 0
                    if matr[min(coloana1, coloana2) - 1] == '0' or matr[10 + min(coloana1, coloana2) - 1] == '0' or matr[20 + min(coloana1, coloana2) - 1] == '0' or matr[20 + min(coloana1, coloana2)] == '0' or matr[20 + max(coloana1, coloana2) + 1] == '0' or matr[max(coloana1, coloana2) + 1] == '0' or matr[10 + max(coloana1, coloana2) + 1] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True

            # Verific daca sunt pe ultima linie
            elif max(linie1, linie2) == 9:
                # Verific daca sunt in stanga de tot
                if min(coloana1, coloana2) == 0:
                    # Verific vecinii de deasupra, diagonala dreapta si dreapta placutei (daca cel putin unul este x)
                    if matr[70] == 'x' or matr[71] == 'x' or matr[81] == 'x' or matr[91] == 'x':
                        check_X = True
                    
                    # Verific vecinii de deasupra, diagonala dreapta si dreapta placutei (daca cel putin unul este 0)
                    if matr[70] == '0' or matr[71] == '0' or matr[81] == '0' or matr[91] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True

                # Verific daca sunt in dreapta de tot
                elif max(coloana1, coloana2) == 9:
                    # Verific vecinii din stanga, deasupra placutei si diagonala stanga (daca cel putin unul este x)
                    if matr[87] == 'x' or matr[97] == 'x' or matr[79] == 'x' or matr[78] == 'x':
                        check_X = True
                    
                    # Verific vecinii din stanga, deasupra placutei si diagonala stanga (daca cel putin unul este 0)
                    if matr[87] == '0' or matr[97] == '0' or matr[79] == '0' or matr[78] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True
                
                else:
                    # Verific vecinii: stanga, diagonala stanga, deasupra, diagonala dreapta, dreapta daca e cel putin un x
                    if matr[90 + min(coloana1, coloana2) - 1] == 'x' or matr[80 + min(coloana1, coloana2) - 1] == 'x' or matr[70 + min(coloana1, coloana2) - 1] == 'x' or matr[70 + min(coloana1, coloana2)] == 'x' or matr[70 + max(coloana1, coloana2) + 1] == 'x' or matr[80 + max(coloana1, coloana2) + 1] == 'x' or matr[90 + max(coloana1, coloana2) + 1] == 'x':
                        check_X = True

                    # Verific vecinii: stanga, diagonala stanga, deasupra, diagonala dreapta, dreapta daca e cel putin un 0
                    if matr[90 + min(coloana1, coloana2) - 1] == '0' or matr[80 + min(coloana1, coloana2) - 1] == '0' or matr[70 + min(coloana1, coloana2) - 1] == '0' or matr[70 + min(coloana1, coloana2)] == '0' or matr[70 + max(coloana1, coloana2) + 1] == '0' or matr[80 + max(coloana1, coloana2) + 1] == '0' or matr[90 + max(coloana1, coloana2) + 1] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True

            # Daca sunt pe linii intermediare
            else:
                # Verific daca sunt in stanga de tot
                if min(coloana1, coloana2) == 0:
                    # Verific vecinii de deasupra, diagonala dreapta sus, dreapta, diagonala dreapta jos, dedesubtul placutei (daca cel putin unul este x)
                    if matr[(min(linie1, linie2) - 1) * 10 + min(coloana1, coloana2)] == 'x' or matr[(min(linie1, linie2) - 1) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[min(linie1, linie2) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[max(linie1, linie2) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[(max(linie1, linie2) + 1) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[(max(linie1, linie2) + 1) * 10 + max(coloana1, coloana2)] == 'x':
                        check_X = True
                    
                    # Verific vecinii de deasupra, diagonala dreapta sus, dreapta, diagonala dreapta jos, dedesubtul placutei (daca cel putin unul este 0)
                    if matr[(min(linie1, linie2) - 1) * 10 + min(coloana1, coloana2)] == '0' or matr[(min(linie1, linie2) - 1) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[min(linie1, linie2) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[max(linie1, linie2) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[(max(linie1, linie2) + 1) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[(max(linie1, linie2) + 1) * 10 + max(coloana1, coloana2)] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True

                # Verific daca sunt in dreapta de tot
                elif max(coloana1, coloana2) == 9:
                    # Verific vecinii din deasupra, diagonala stanga sus, stanga, diagonala stanga jos, dedesubt (daca cel putin unul este x)
                    if matr[(min(linie1, linie2) - 1) * 10 + max(coloana1, coloana2)] == 'x' or matr[(min(linie1, linie2) - 1) * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[(min(linie1, linie2)) * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[max(linie1, linie2) * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[(max(linie1, linie2) + 1) * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[(max(linie1, linie2) + 1) * 10 + min(coloana1, coloana2)] == 'x':
                        check_X = True
                    
                    # Verific vecinii din stanga, deasupra placutei si diagonala stanga (daca cel putin unul este 0)
                    if matr[(min(linie1, linie2) - 1) * 10 + max(coloana1, coloana2)] == '0' or matr[(min(linie1, linie2) - 1) * 10 + min(coloana1, coloana2) - 1] == '0' or matr[(min(linie1, linie2)) * 10 + min(coloana1, coloana2) - 1] == '0' or matr[max(linie1, linie2) * 10 + min(coloana1, coloana2) - 1] == '0' or matr[(max(linie1, linie2) + 1) * 10 + min(coloana1, coloana2) - 1] == '0' or matr[(max(linie1, linie2) + 1) * 10 + min(coloana1, coloana2)] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True
                
                else:
                    # Verific vecinii: stanga, diagonala stanga, dedesubt, diagonala dreapta, dreapta daca e cel putin un x
                    if matr[max(linie1, linie2) * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[min(linie1, linie2) * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[(min(linie1, linie2) - 1) * 10 + min(coloana1, coloana2) - 1] == 'x' or matr[(min(linie1, linie2) - 1) * 10 + max(coloana1, coloana2)] == 'x' or matr[(min(linie1, linie2) - 1) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[min(linie1, linie2) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[max(linie1, linie2) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[(max(linie1, linie2) + 1) * 10 + max(coloana1, coloana2) + 1] == 'x' or matr[(max(linie1, linie2) + 1) * 10 + min(coloana1, coloana2)] == 'x' or matr[(max(linie1, linie2) + 1) * 10 + min(coloana1, coloana2) - 1] == 'x':
                        check_X = True

                    # Verific vecinii: stanga, diagonala stanga jos, dedesubt, diagonala dreapta jos, dreapta, diagonala dreapta sus, deasupra, diagonala stanga sus daca e cel putin un 0
                    if matr[max(linie1, linie2) * 10 + min(coloana1, coloana2) - 1] == '0' or matr[min(linie1, linie2) * 10 + min(coloana1, coloana2) - 1] == '0' or matr[(min(linie1, linie2) - 1) * 10 + min(coloana1, coloana2) - 1] == '0' or matr[(min(linie1, linie2) - 1) * 10 + max(coloana1, coloana2)] == '0' or matr[(min(linie1, linie2) - 1) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[min(linie1, linie2) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[max(linie1, linie2) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[(max(linie1, linie2) + 1) * 10 + max(coloana1, coloana2) + 1] == '0' or matr[(max(linie1, linie2) + 1) * 10 + min(coloana1, coloana2)] == '0' or matr[(max(linie1, linie2) + 1) * 10 + min(coloana1, coloana2) - 1] == '0':
                        check_0 = True

                    if check_X and check_0:
                        return True

    else:
        return False
        

def modif_joc(matr1, index1, index2, simbol):
    joc_generat = Joc()
    for i in range(0, len(matr1)):
        joc_generat.matr[i] = matr1[i]
    joc_generat.matr[index1] = simbol
    joc_generat.matr[index2] = simbol
    return joc_generat


# Primeste o lista si returneaza numarul de puncte pentru fiecare simbol
def elem_identice(lista):
    score_x = 0
    score_0 = 0

    for index in range(0, len(lista) - 3):
        if lista[index] == lista[index + 1] == lista[index + 2]:
            if lista[index] != '#':    
                if lista[index] == 'x':
                    score_x = score_x + 1
                elif lista[index] == '0':
                    score_0 = score_0 + 1
    
    if len(lista) - 3 == 0:
        if lista[0] == lista[1] == lista[2]:
            if lista[0] != '#':
                if lista[0] == 'x':
                    score_x = score_x + 1
                elif lista[0] == '0':
                    score_0 = score_0 + 1

    return score_x, score_0

class Joc:
    """
	Clasa care defineste jocul. Se va schimba de la un joc la altul.
	"""
    NR_LINII = 10
    NR_COLOANE = 10
    JMIN = None
    JMAX = None
    GOL = '#'
    SCOR_X = 0
    SCOR_0 = 0

    def __init__(self, tabla=None):
        if tabla is not None:
            self.matr = tabla
        else:
            self.matr = [Joc.GOL] * 100
            self.matr[4 * 10 + 4] = 'x'
            self.matr[5 * 10 + 4] = 'x'
            self.matr[4 * 10 + 5] = '0'
            self.matr[5 * 10 + 5] = '0'

    def final(self):
        # Updatez scorul pentru fiecare diagonala

        rezultate_x, rezultate_0 = elem_identice(self.matr[0:100:11])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[10:99:11])
        
        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[20:98:11])
        
        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0
        
        rezultate_x, rezultate_0 = elem_identice(self.matr[30:97:11])
        
        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[40:96:11])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0
        
        rezultate_x, rezultate_0 = elem_identice(self.matr[50:95:11])
        
        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0        
        
        rezultate_x, rezultate_0 = elem_identice(self.matr[60:94:11])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0
        
        rezultate_x, rezultate_0 = elem_identice(self.matr[70:93:11])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[70:93:11])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[1:90:11])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[2:80:11])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[3:70:11])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[4:60:11])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[5:50:11])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[6:40:11])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[7:30:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0
        
        rezultate_x, rezultate_0 = elem_identice(self.matr[2:21:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[3:31:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0
        
        rezultate_x, rezultate_0 = elem_identice(self.matr[4:41:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[5:51:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0
        
        rezultate_x, rezultate_0 = elem_identice(self.matr[6:61:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[7:71:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0
        
        rezultate_x, rezultate_0 = elem_identice(self.matr[8:81:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[9:91:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[19:92:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[29:93:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[39:94:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[49:95:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[59:96:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[69:97:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        rezultate_x, rezultate_0 = elem_identice(self.matr[79:98:9])

        self.SCOR_X = self.SCOR_X + rezultate_x
        self.SCOR_0 = self.SCOR_0 + rezultate_0

        # Verific daca mai exista locuri de adaugat placute

        for i in range(0, 10):
            for j in range(0, 9):
                if check_position(self.matr, i, j, i, j + 1):
                    return False
        
        for i in range(0, 9):
            for j in range(0, 10):
                if check_position(self.matr, i, j, i + 1, j):
                    return False

        # Daca am ajuns aici inseamna ca nu se mai pot adauga placute deci se opreste jocul
        # Returnez simbolul jucatorului cu mai multe puncte sau remiza in caz de egalitate

        if self.SCOR_X > self.SCOR_0:
            return self.SCOR_X
        elif self.SCOR_0 > self.SCOR_X:
            return self.SCOR_0
        else:
            return 'remiza'
        


    def mutari_joc(self, jucator):
        l_mutari = []

        for i in range(0, 10):
            for j in range(0, 9):
                if self.matr[i * 10 + j] == self.matr[i * 10 + j + 1] == '#' and check_position(self.matr, i, j, i, (j + 1)):
                    l_mutari.append(modif_joc(self.matr, (i * 10 + j), (i * 10 + j + 1), jucator))

        for i in range(0, 9):
            for j in range(0, 10):
                if self.matr[i * 10 + j] == self.matr[(i + 1) * 10 + j] == '#' and check_position(self.matr, i, j, (i + 1), j):
                    l_mutari.append(modif_joc(self.matr, (i * 10 + j), ((i + 1) * 10 + j), jucator))

        return l_mutari

    # linie deschisa inseamna linie pe care jucatorul mai poate forma o configuratie castigatoare
    def linie_deschisa(self, lista, jucator):

        for i in range(0, len(lista) - 3):
            x = []
            x.append(lista[i])
            x.append(lista[i + 1])
            x.append(lista[i + 2])

            # obtin multimea simbolurilor de pe linie
            mt = set(x)
            # verific daca sunt maxim 2 simboluri
            if len(mt) <= 2:
                # daca multimea simbolurilor nu are alte simboluri decat pentru cel de "gol" si jucatorul curent
                if mt <= {Joc.GOL, jucator}:  # incluziune de seturi
                    # inseamna ca linia este deschisa
                    return 1
                else:
                    return 0
            else:
                return 0
            

        if len(lista) - 3 == 0:
            x = []
            x.append(lista[0])
            x.append(lista[1])
            x.append(lista[2])

            # obtin multimea simbolurilor de pe linie
            mt = set(x)
            # verific daca sunt maxim 2 simboluri
            if len(mt) <= 2:
                # daca multimea simbolurilor nu are alte simboluri decat pentru cel de "gol" si jucatorul curent
                if mt <= {Joc.GOL, jucator}:  # incluziune de seturi
                    # inseamna ca linia este deschisa
                    return 1
                else:
                    return 0
            else:
                return 0

    # Voi verifica pentru fiecare diagonala in parte (de minim 3 elemente)
    def linii_deschise(self, jucator):
        return (self.linie_deschisa(self.matr[0:100:11], jucator)
				+ self.linie_deschisa(self.matr[10:100:11], jucator)
				+ self.linie_deschisa(self.matr[20:98:11], jucator)
				+ self.linie_deschisa(self.matr[30:97:11], jucator)
				+ self.linie_deschisa(self.matr[40:96:11], jucator)
				+ self.linie_deschisa(self.matr[50:95:11], jucator)
				+ self.linie_deschisa(self.matr[60:94:11], jucator)
				+ self.linie_deschisa(self.matr[70:93:11], jucator)
                + self.linie_deschisa(self.matr[1:90:11], jucator)
                + self.linie_deschisa(self.matr[2:80:11], jucator)
                + self.linie_deschisa(self.matr[3:70:11], jucator)
                + self.linie_deschisa(self.matr[4:60:11], jucator)
                + self.linie_deschisa(self.matr[5:50:11], jucator)
                + self.linie_deschisa(self.matr[6:40:11], jucator)
                + self.linie_deschisa(self.matr[7:30:11], jucator)
                + self.linie_deschisa(self.matr[2:21:9], jucator)
                + self.linie_deschisa(self.matr[3:31:9], jucator)
                + self.linie_deschisa(self.matr[4:41:9], jucator)
                + self.linie_deschisa(self.matr[5:51:9], jucator)
                + self.linie_deschisa(self.matr[6:61:9], jucator)
                + self.linie_deschisa(self.matr[7:71:9], jucator)
                + self.linie_deschisa(self.matr[8:81:9], jucator)
                + self.linie_deschisa(self.matr[9:91:9], jucator)
                + self.linie_deschisa(self.matr[19:92:9], jucator)
                + self.linie_deschisa(self.matr[29:93:9], jucator)
                + self.linie_deschisa(self.matr[39:94:9], jucator)
                + self.linie_deschisa(self.matr[49:95:9], jucator)
                + self.linie_deschisa(self.matr[59:96:9], jucator)
                + self.linie_deschisa(self.matr[69:97:9], jucator)
                + self.linie_deschisa(self.matr[79:98:9], jucator)
                )

    def estimeaza_scor(self, adancime):
        t_final = self.final()
        if t_final == Joc.JMAX:
            return (99 + adancime)
        elif t_final == Joc.JMIN:
            return (-99 - adancime)
        elif t_final == 'remiza':
            return 0
        else:
            return self.linii_deschise(Joc.JMAX) - self.linii_deschise(Joc.JMIN)

    def __str__(self):
        sir = ""

        for i, element in enumerate(self.matr):
            if i % 10 == 0 and i != 0:
                sir = sir + '\n'
            sir = sir + element + " "

        sir = sir + '\n'

        return sir


class Stare:
    """
	Clasa folosita de algoritmii minimax si alpha-beta
	Are ca proprietate tabla de joc
	Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
	De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari_joc() care ofera lista cu
	configuratiile posibile in urma mutarii unui jucator
	"""

    ADANCIME_MAX = None

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc  # un obiect de tip Joc => „tabla_joc.matr”
        self.j_curent = j_curent  # simbolul jucatorului curent

        # adancimea in arborele de stari
        #	(scade cu cate o unitate din „tata” in „fiu”)
        self.adancime = adancime

        # scorul starii (daca e finala, adica frunza a arborelui)
        # sau scorul celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []  # lista va contine obiecte de tip Stare

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari_stare(self):
        l_mutari = self.tabla_joc.mutari_joc(self.j_curent)
        juc_opus = self.jucator_opus()

        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]
        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Joc curent:" + self.j_curent + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # Altfel, calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari_stare()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare

    # Conditia de retezare:
    if alpha >= beta:
        return stare  # este intr-un interval invalid, deci nu o mai procesez

    # Calculez toate mutarile posibile din starea curenta (toti „fiii”)
    stare.mutari_posibile = stare.mutari_stare()

    if stare.j_curent == Joc.JMAX:
        scor_curent = float('-inf')  # scorul „tatalui” de tip MAX

        # pentru fiecare „fiu” de tip MIN:
        for mutare in stare.mutari_posibile:
            # calculeaza scorul fiului curent
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (cresc) scorul si alfa
            # „tatalui” de tip MAX, folosind scorul fiului curent
            if scor_curent < stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if alpha < stare_noua.scor:
                alpha = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MIN


    elif stare.j_curent == Joc.JMIN:
        scor_curent = float('inf')  # scorul „tatalui” de tip MIN

        # pentru fiecare „fiu” de tip MAX:
        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (scad) scorul si beta
            # „tatalui” de tip MIN, folosind scorul fiului curent
            if scor_curent > stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if beta > stare_noua.scor:
                beta = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MAX

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor

    return stare


def afis_daca_final(stare_curenta):
    final = stare_curenta.tabla_joc.final()
    if (final):
        if (final == "remiza"):
            print("Remiza!")
        else:
            print("A castigat " + final)

        return True

    return False


def main():
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-Beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    # initializare ADANCIME_MAX in functie de dificultatea aleasa
    raspuns_valid = False
    while not raspuns_valid:
        dificultate = input("Selectati o dificultate\n 1. Usor\n 2. Mediu\n 3. Greu\n ")
        if dificultate in ['1', '2', '3']:
            raspuns_valid = True
            Stare.ADANCIME_MAX = int(dificultate)

        else:
            print("Nu ati ales o varianta corecta.")       

    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu x sau cu 0? ").lower()
        if (Joc.JMIN in ['x', '0']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie x sau 0.")
    Joc.JMAX = '0' if Joc.JMIN == 'x' else 'x'

    # initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'x', Stare.ADANCIME_MAX)

    while True:
        if stare_curenta.j_curent == Joc.JMIN:
            # Cronometrez timpul de mutare al jucatorului
            t_inainte_jucator = int(round(time.time() * 1000))
            # muta jucatorul
            raspuns_valid = False
            while not raspuns_valid:
                try:
                    linie1 = input("linie element 1 = ")
                    if check_exit(linie1):
                        print('Scorul lui x: ' + str(stare_curenta.tabla_joc.SCOR_X))
                        print('Scorul lui 0: ' + str(stare_curenta.tabla_joc.SCOR_0))
                        return
                    coloana1 = input("coloana element 1 = ")
                    if check_exit(coloana1):
                        print('Scorul lui x: ' + str(stare_curenta.tabla_joc.SCOR_X))
                        print('Scorul lui 0: ' + str(stare_curenta.tabla_joc.SCOR_0))
                        return
                    linie2 = input("linie element 2 = ")
                    if check_exit(linie2):
                        print('Scorul lui x: ' + str(stare_curenta.tabla_joc.SCOR_X))
                        print('Scorul lui 0: ' + str(stare_curenta.tabla_joc.SCOR_0))
                        return
                    coloana2 = input("coloana element 2 = ")
                    if check_exit(coloana2):
                        print('Scorul lui x: ' + str(stare_curenta.tabla_joc.SCOR_X))
                        print('Scorul lui 0: ' + str(stare_curenta.tabla_joc.SCOR_0))
                        return

                    linie1 = int(linie1)
                    coloana1 = int(coloana1)
                    linie2 = int(linie2)
                    coloana2 = int(coloana2)

                    positionCheck = False

                    if linie1 in range(0, 10) and coloana1 in range(0, 10) and linie2 in range(0, 10) and coloana2 in range(0, 10):
                        # Apelez position_check() pentru a vedea daca jucatorul a plasat piesele corespunzator
                        positionCheck = check_position(stare_curenta.tabla_joc.matr, linie1, coloana1, linie2, coloana2)
                        if stare_curenta.tabla_joc.matr[linie1 * 10 + coloana1] == Joc.GOL and stare_curenta.tabla_joc.matr[linie2 * 10 + coloana2] == Joc.GOL and positionCheck:
                            raspuns_valid = True
                        else:
                            print("Exista deja un simbol in pozitia ceruta, nu ati pus simbolurile unul langa celalalt, sunt pe diagonala sau nu le-ati pus langa minim un X si un 0.")
                    else:
                        print("Linie sau coloana invalida (trebuie sa fie unul dintre numerele 0,1,2,3,4,5,6,7,8,9).")

                except ValueError:
                    print("Linia si coloana trebuie sa fie numere intregi")

            # dupa iesirea din while sigur am valide atat linia cat si coloana
            # deci pot plasa simbolul pe "tabla de joc"
            stare_curenta.tabla_joc.matr[linie1 * 10 + coloana1] = Joc.JMIN
            stare_curenta.tabla_joc.matr[linie2 * 10 + coloana2] = Joc.JMIN

            # afisarea starii jocului in urma mutarii utilizatorului
            print("\nTabla dupa mutarea jucatorului")
            print(str(stare_curenta))

            # testez daca jocul a ajuns intr-o stare finala
            # si afisez un mesaj corespunzator in caz ca da
            # si afisez scorul
            if (afis_daca_final(stare_curenta)):
                print('Scorul lui x: ' + str(stare_curenta.tabla_joc.SCOR_X))
                print('Scorul lui 0: ' + str(stare_curenta.tabla_joc.SCOR_0))
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()

            t_dupa_jucator = int(round(time.time() * 1000))

        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator

            # preiau timpul in milisecunde de dinainte de mutare
            t_inainte_calculator = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))
            print('Scorul lui x: ' + str(stare_curenta.tabla_joc.SCOR_X))
            print('Scorul lui 0: ' + str(stare_curenta.tabla_joc.SCOR_0))

            # preiau timpul in milisecunde de dupa mutare
            t_dupa_calculator = int(round(time.time() * 1000))
            
            print("Jucatorul a gandit timp de " + str(t_dupa_jucator - t_inainte_jucator) + " milisecunde.")
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa_calculator - t_inainte_calculator) + " milisecunde.")
            
            if (afis_daca_final(stare_curenta)):
                print('Scorul lui x: ' + str(stare_curenta.tabla_joc.SCOR_X))
                print('Scorul lui 0: ' + str(stare_curenta.tabla_joc.SCOR_0))
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__":
    main()