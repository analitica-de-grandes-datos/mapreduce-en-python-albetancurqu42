#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#checking_balance,months_loan_duration,credit_history,purpose,amount,savings_balance,employment_length,installment_rate,personal_status,other_debtors,residence_history,property,age,installment_plan,housing,existing_credits,default,dependents,telephone,foreign_worker,job

import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:

        sys.stdout.write(f"{line.split(',')[3]}\t{line.split(',')[4]}\n")