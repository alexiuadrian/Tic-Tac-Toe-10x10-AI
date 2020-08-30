import time

def check_position(matr, linie1, coloana1, linie2, coloana2):
    if abs(linie1 - linie2) <= 1 and abs(coloana1 - coloana2) <= 1 and abs(abs(coloana1 - coloana2) + abs(linie1 - linie2)) != 2:
        check_X = False
        check_0 = False
        # Cauta daca exista minim un X si un 0 pe langa placuta


        # # Verific daca se afla pe prima linie
        # if min(linie1, linie2) == 0:
        #     # Verific daca cele doua elemente sunt pe aceeasi linie
        #     if linie1 == linie2:
        #         # Verific daca sunt primele de pe linie
        #         if min(coloana1, coloana2) == 0 and max(coloana1, coloana2) == 1:
        #             # Verific daca sub ele, pe diagonala sau in dreapta exista cel putin un X
        #             if matr[11] == 'x' or matr[12] == 'x' or matr[13] == 'x' or matr[2] == 'x':
        #                 check_X = True
        #             # Verific daca sub ele, pe diagonala sau in dreapta exista cel putin un 0
        #             if matr[11] == '0' or matr[12] == '0' or matr[13] == '0' or matr[2] == '0':
        #                 check_0 = True
        #             if check_X and check_0:
        #                 return True
        #         else:
        #             # Verific daca in stanga, sub ele, pe diagonala sau in dreapta exista cel putin un X
        #             if matr[linie1 * 10 + ]

        # Verific daca sunt pe orizontala
        if linie1 == linie2:
            print("Sunt pe orizontala")
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
                print("Sunt pe linii intermediare")
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
                    print("Sunt in mijlocul tablei")
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
                    if matr[20] == 'x' or matr[21] == 'x' or matr[2] == 'x' or matr[12] == 'x':
                        check_X = True
                    
                    # Verific vecinii de dedesubtul, diagonala dreapta si dreapta placutei (daca cel putin unul este 0)
                    if matr[20] == '0' or matr[21] == '0' or matr[2] == '0' or matr[12] == '0':
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
                    if matr[min(coloana1, coloana2) - 1] == 'x' or matr[10 + min(coloana1, coloana2) - 1] == 'x' or matr[10 + min(coloana1, coloana2) - 1] == 'x' or matr[20 + coloana1 - 1] or matr[20 + min(coloana1, coloana2)] == 'x' or matr[20 + max(coloana1, coloana2) + 1] == 'x' or matr[max(coloana1, coloana2) + 1] == 'x' or matr[10 + max(coloana1, coloana2) + 1]:
                        check_X = True

                    # Verific vecinii: stanga, diagonala stanga, dedesubt, diagonala dreapta, dreapta daca e cel putin un 0
                    if matr[min(coloana1, coloana2) - 1] == '0' or matr[10 + min(coloana1, coloana2) - 1] == '0' or matr[10 + min(coloana1, coloana2) - 1] == '0' or matr[20 + coloana1 - 1] or matr[20 + min(coloana1, coloana2)] == '0' or matr[20 + max(coloana1, coloana2) + 1] == '0' or matr[max(coloana1, coloana2) + 1] == '0' or matr[10 + max(coloana1, coloana2) + 1]:
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
        

def modif_joc(matr1, index, simbol):
    joc_generat = Joc()
    for i in range(0, len(matr1)):
        joc_generat.matr[i] = matr1[i]
    joc_generat.matr[index] = simbol
    return joc_generat


def elem_identice(lista):
    """ Primeste o lista si returneaza
	-> simbolul jucatorului castigator (daca lista contine doar acel simbol repetat)
	-> sau False (daca a fost remiza sau daca nu s-a terminat jocul)
	"""
    mt = set(lista)
    if len(mt) == 1:
        castigator = list(mt)[0]
        if castigator != Joc.GOL:
            return castigator
        else:
            return False
    else:
        return False


class Joc:
    """
	Clasa care defineste jocul. Se va schimba de la un joc la altul.
	"""
    NR_LINII = 10
    NR_COLOANE = 10
    JMIN = None
    JMAX = None
    GOL = '#'

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
        # Folosim slice-uri pe lista de 9 elemente
        # pentru a gasi usor cele 3 linii, 3 coloane si 2 diagonale
        # si a verifica daca a castigat cineva (return simbolul castigatorului),
        # daca a fost remiza (return "remiza"),
        # sau daca nu s-a terminat jocul (return False)
        rez = (elem_identice(self.matr[0:3])
               or elem_identice(self.matr[3:6])
               or elem_identice(self.matr[6:9])
               or elem_identice(self.matr[0:9:3])
               or elem_identice(self.matr[1:9:3])
               or elem_identice(self.matr[2:9:3])
               or elem_identice(self.matr[0:9:4])
               or elem_identice(self.matr[2:8:2]))
        if (rez):
            return rez
        elif Joc.GOL not in self.matr:
            return 'remiza'
        else:
            return False

    def mutari_joc(self, jucator):
        """
		Pentru configuratia curenta de joc "self.matr" (de tip lista, cu 9 elemente),
		trebuie sa returnati o lista "l_mutari" cu elemente de tip Joc,
		corespunzatoare tuturor configuratiilor-succesor posibile.

		"jucator" este simbolul jucatorului care face mutarea
		"""
        l_mutari = []

        ### TO DO ...

        # locuri_libere = []

        for i in range(0, len(self.matr)):
            if self.matr[i] == '#':
                l_mutari.append(modif_joc(self.matr, i, jucator))

        return l_mutari

    # linie deschisa inseamna linie pe care jucatorul mai poate forma o configuratie castigatoare
    def linie_deschisa(self, lista, jucator):
        """
		# rezolvare alternativa:
		juc_opus = 'x' if jucator=='0' else '0'
		if juc_opus in lista:
			return 0
		return 1
		"""

        # obtin multimea simbolurilor de pe linie
        mt = set(lista)
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

    def linii_deschise(self, jucator):
        return (self.linie_deschisa(self.matr[0:3], jucator)
				+ self.linie_deschisa(self.matr[3:6], jucator)
				+ self.linie_deschisa(self.matr[6:9], jucator)
				+ self.linie_deschisa(self.matr[0:9:3], jucator)
				+ self.linie_deschisa(self.matr[1:9:3], jucator)
				+ self.linie_deschisa(self.matr[2:9:3], jucator)
				+ self.linie_deschisa(self.matr[0:9:4], jucator)  # prima diagonala
				+ self.linie_deschisa(self.matr[2:8:2], jucator))  # a doua diagonala

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
        # sir = (" ".join([str(x) for x in self.matr[0:3]]) + "\n" +
        #        " ".join([str(x) for x in self.matr[3:6]]) + "\n" +
        #        " ".join([str(x) for x in self.matr[6:9]]) + "\n")

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

    # initializare ADANCIME_MAX
    raspuns_valid = False
    while not raspuns_valid:
        n = input("Adancime maxima a arborelui: ")
        if n.isdigit():
            Stare.ADANCIME_MAX = int(n)
            raspuns_valid = True
        else:
            print("Trebuie sa introduceti un numar natural nenul.")

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
            # muta jucatorul
            raspuns_valid = False
            while not raspuns_valid:
                try:
                    linie1 = int(input("linie element 1 = "))
                    coloana1 = int(input("coloana element 1 = "))
                    linie2 = int(input("linie element 2 = "))
                    coloana2 = int(input("coloana element 2 = "))
                    positionCheck = False

                    if linie1 in range(0, 10) and coloana1 in range(0, 10) and linie2 in range(0, 10) and coloana2 in range(0, 10):
                        positionCheck = check_position(stare_curenta.tabla_joc.matr, linie1, coloana1, linie2, coloana2)
                        print(positionCheck)
                        if stare_curenta.tabla_joc.matr[linie1 * 10 + coloana1] == Joc.GOL and stare_curenta.tabla_joc.matr[linie2 * 10 + coloana2] == Joc.GOL and positionCheck is True:
                            # implementeaza check_position() de sus
                            raspuns_valid = True
                        else:
                            print("Exista deja un simbol in pozitia ceruta, nu ati pus simbolurile unul langa celalalt, sunt pe diagonala sau nu le-ati pus langa minim un X si un 0.")
                    else:
                        print("Linie sau coloana invalida (trebuie sa fie unul dintre numerele 0,1,2,3,4,5,6,7,8,9).")

                    # if

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
            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()

        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator

            # preiau timpul in milisecunde de dinainte de mutare
            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))

            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")

            if (afis_daca_final(stare_curenta)):
                break

            # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = stare_curenta.jucator_opus()


if __name__ == "__main__":
    main()